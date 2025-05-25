from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from pacientes.models import Cita
from usuarios.models import Profile
from datetime import date, time


class PacientesTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='paciente1', password='1234')
        self.profile = Profile.objects.create(user=self.user, role='PATIENT')
        self.client.login(username='paciente1', password='1234')

        self.doctor = User.objects.create_user(username='doctor1', password='pass', first_name='Luis', last_name='Gómez')
        self.doctor_profile = Profile.objects.create(user=self.doctor, role='DOCTOR', especialidad='Neurología')

        self.cita = Cita.objects.create(
            paciente=self.user,
            doctor=self.doctor,
            fecha=date(2025, 6, 15),
            hora=time(10, 0),
            lugar='Sede Norte',
            area='Neurología',
            motivo='Chequeo general'
        )

    def test_model_str(self):
        esperado = f'Cita de {self.user.username} con Luis Gómez (Neurología) el 2025-06-15 a las 10:00:00'
        self.assertEqual(str(self.cita), esperado)

    def test_model_estado_por_defecto(self):
        self.assertEqual(self.cita.estado, 'ACTIVA')

    def test_dashboard_view(self):
        response = self.client.get(reverse('pacientes_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bienvenido')

    def test_ver_citas(self):
        response = self.client.get(reverse('ver_citas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chequeo general')

    def test_crear_cita_get(self):
        response = self.client.get(reverse('crear_cita'))
        self.assertEqual(response.status_code, 200)

    def test_crear_cita_post_exitosa(self):
        response = self.client.post(reverse('crear_cita'), {
            'fecha': '2025-07-01',
            'hora': '15:00',
            'lugar': 'Sede Sur',
            'doctor': self.doctor.id,
            'motivo': 'Consulta'
        })
        self.assertRedirects(response, reverse('ver_citas'))
        self.assertEqual(Cita.objects.filter(paciente=self.user).count(), 2)

    def test_crear_cita_post_conflicto(self):
        response = self.client.post(reverse('crear_cita'), {
            'fecha': self.cita.fecha,
            'hora': self.cita.hora.strftime("%H:%M"),
            'lugar': self.cita.lugar,
            'doctor': self.doctor.id,
            'motivo': 'Duplicada'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'El doctor ya tiene una cita en ese horario.')

    def test_crear_cita_doctor_inexistente(self):
        response = self.client.post(reverse('crear_cita'), {
            'fecha': '2025-07-01',
            'hora': '14:00',
            'lugar': 'Sede Centro',
            'doctor': 9999,
            'motivo': 'Error'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'El doctor seleccionado no existe.')

    def test_editar_cita_get(self):
        response = self.client.get(reverse('editar_cita', args=[self.cita.id]))
        self.assertEqual(response.status_code, 200)

    def test_editar_cita_post_sin_conflicto(self):
        response = self.client.post(reverse('editar_cita', args=[self.cita.id]), {
            'fecha': '2025-06-20',
            'hora': '13:00',
            'lugar': 'Sede Centro',
            'doctor': self.doctor.id,
            'motivo': 'Cambio'
        })
        self.assertRedirects(response, reverse('ver_citas'))
        self.cita.refresh_from_db()
        self.assertEqual(self.cita.hora.strftime("%H:%M"), '13:00')

    def test_editar_cita_post_con_conflicto(self):
        nueva = Cita.objects.create(
            paciente=self.user,
            doctor=self.doctor,
            fecha='2025-06-22',
            hora='12:00',
            lugar='Sede Norte',
            area='Cardiología',
            motivo='Conflicto'
        )
        response = self.client.post(reverse('editar_cita', args=[nueva.id]), {
            'fecha': '2025-06-22',
            'hora': '12:00',
            'lugar': 'Sede Norte',
            'doctor': self.doctor.id,
            'motivo': 'Actualización'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ese horario ya está ocupado por otra cita.')

    def test_eliminar_cita_get(self):
        response = self.client.get(reverse('eliminar_cita', args=[self.cita.id]))
        self.assertEqual(response.status_code, 200)

    def test_eliminar_cita_post(self):
        response = self.client.post(reverse('eliminar_cita', args=[self.cita.id]))
        self.assertRedirects(response, reverse('ver_citas'))
        self.cita.refresh_from_db()
        self.assertEqual(self.cita.estado, 'CANCELADA')
