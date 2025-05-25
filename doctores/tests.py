from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from usuarios.models import Profile
from pacientes.models import Cita
from datetime import date, time

class DoctoresViewsTest(TestCase):
    def setUp(self):
        # Crear usuario doctor
        self.doctor = User.objects.create_user(username='doctor1', password='1234', first_name='María', last_name='Pérez')
        Profile.objects.create(
            user=self.doctor,
            role='DOCTOR',
            telefono='3222222222',
            direccion='Avenida Siempre Viva',
            especialidad='Cardiología'
        )

        # Crear paciente
        self.paciente = User.objects.create_user(username='paciente1', password='abcd')
        Profile.objects.create(
            user=self.paciente,
            role='PACIENTE',
            telefono='3111111111',
            direccion='Calle 1'
        )

        # Crear cita asociada
        self.cita = Cita.objects.create(
            paciente=self.paciente,
            doctor=self.doctor,
            fecha=date.today(),
            hora=time(10, 30),
            lugar='Sede Norte',
            area='Cardiología',
            motivo='Chequeo general'
        )

        # Iniciar sesión como doctor
        self.client = Client()
        self.client.login(username='doctor1', password='1234')

    def test_dashboard_acceso(self):
        url = reverse('doctores_dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bienvenido')
        self.assertContains(response, 'Citas Totales')
        self.assertContains(response, 'Chequeo general')

    def test_detalle_cita(self):
        url = reverse('detalle_cita', args=[self.cita.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Chequeo general')
        self.assertContains(response, self.paciente.username)
