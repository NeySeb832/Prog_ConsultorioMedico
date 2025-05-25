from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from usuarios.models import Profile
from pacientes.models import Cita
from datetime import date, time

class SecretariaViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

        # Crear usuario y perfil de secretaria
        self.secretaria = User.objects.create_user(username='secretaria', password='1234')
        Profile.objects.create(user=self.secretaria, role='STAFF', telefono='123', direccion='Dirección')

        # Crear usuario y perfil de doctor
        self.doctor = User.objects.create_user(username='doctor', password='1234', first_name='Luis', last_name='Gómez')
        Profile.objects.create(user=self.doctor, role='DOCTOR', especialidad='Cardiología')

        # Crear usuario y perfil de paciente
        self.paciente = User.objects.create_user(username='paciente', password='1234', first_name='Ana', last_name='Díaz')
        Profile.objects.create(user=self.paciente, role='PATIENT', telefono='111', direccion='Calle 1')

        # Crear cita
        self.cita = Cita.objects.create(
            paciente=self.paciente,
            doctor=self.doctor,
            fecha=date(2025, 6, 20),
            hora=time(10, 0),
            lugar='Sede Norte',
            motivo='Chequeo general',
            area='Cardiología'
        )

        self.client.login(username='secretaria', password='1234')

    def test_dashboard_secretaria(self):
        response = self.client.get(reverse('secretaria_dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_ver_citas_secretaria(self):
        response = self.client.get(reverse('ver_citas_secretaria'))
        self.assertEqual(response.status_code, 200)

    def test_ver_detalle_cita_secretaria(self):
        response = self.client.get(reverse('ver_detalle_cita_secretaria', args=[self.cita.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chequeo general')

    def test_crear_cita_get(self):
        response = self.client.get(reverse('crear_cita_secretaria'))
        self.assertEqual(response.status_code, 200)

    def test_crear_cita_post_correcta(self):
        response = self.client.post(reverse('crear_cita_secretaria'), {
            'paciente': self.paciente.id,
            'doctor': self.doctor.id,
            'fecha': '2025-07-10',
            'hora': '11:00',
            'lugar': 'Sede Centro',
            'motivo': 'Control general'
        })
        self.assertEqual(response.status_code, 302)

    def test_crear_cita_conflicto(self):
        response = self.client.post(reverse('crear_cita_secretaria'), {
            'paciente': self.paciente.id,
            'doctor': self.doctor.id,
            'fecha': self.cita.fecha,
            'hora': '10:00',
            'lugar': 'Sede Norte',
            'motivo': 'Doble'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ya tiene una cita en ese horario')

    def test_editar_cita_get(self):
        response = self.client.get(reverse('editar_cita_secretaria', args=[self.cita.id]))
        self.assertEqual(response.status_code, 200)

    def test_editar_cita_post(self):
        response = self.client.post(reverse('editar_cita_secretaria', args=[self.cita.id]), {
            'paciente': self.paciente.id,
            'doctor': self.doctor.id,
            'fecha': '2025-06-21',
            'hora': '12:00',
            'lugar': 'Sede Sur',
            'motivo': 'Cambio'
        })
        self.assertEqual(response.status_code, 302)

    def test_cancelar_cita_get(self):
        response = self.client.get(reverse('cancelar_cita_secretaria', args=[self.cita.id]))
        self.assertEqual(response.status_code, 200)

    def test_cancelar_cita_post(self):
        response = self.client.post(reverse('cancelar_cita_secretaria', args=[self.cita.id]))
        self.assertEqual(response.status_code, 302)

    def test_gestionar_pacientes(self):
        response = self.client.get(reverse('gestionar_pacientes'))
        self.assertEqual(response.status_code, 200)

    def test_crear_paciente(self):
        response = self.client.post(reverse('crear_paciente'), {
            'username': 'nuevo',
            'password': 'pass',
            'email': 'nuevo@ejemplo.com',
            'first_name': 'Pepe',
            'last_name': 'González',
            'telefono': '3010000000',
            'direccion': 'Calle 10'
        })
        self.assertEqual(response.status_code, 302)

    def test_editar_paciente(self):
        response = self.client.post(reverse('editar_paciente', args=[self.paciente.id]), {
            'username': 'paciente_editado',
            'email': 'editado@ejemplo.com',
            'first_name': 'Ana',
            'last_name': 'Díaz',
            'telefono': '333',
            'direccion': 'Nueva dirección',
            'password': ''
        })
        self.assertEqual(response.status_code, 302)

    def test_eliminar_paciente(self):
        user_nuevo = User.objects.create_user(username='eliminarme', password='1234')
        response = self.client.post(reverse('eliminar_paciente', args=[user_nuevo.id]))
        self.assertEqual(response.status_code, 302)
