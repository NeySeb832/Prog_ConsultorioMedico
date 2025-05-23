# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : models.py (módulo pacientes)
# Función del Archivo : Define el modelo de datos para las citas médicas entre pacientes y doctores.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.db import models
from django.contrib.auth.models import User

# -----------------------------------------------------------------------------
# MODELO: Cita
# Descripción:
#   Representa una cita médica entre un paciente y un doctor, incluyendo la fecha,
#   hora, sede, área médica, motivo y estado de la cita.
# -----------------------------------------------------------------------------
class Cita(models.Model):
    # Usuario paciente que solicita la cita
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas_paciente')

    # Usuario doctor asignado a la cita
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas_doctor')

    # Fecha de la cita médica
    fecha = models.DateField()

    # Hora de la cita médica
    hora = models.TimeField()

    # Lugar donde se llevará a cabo la cita (sede)
    lugar = models.CharField(
        max_length=100,
        choices=[
            ('Sede Norte', 'Sede Norte'),
            ('Sede Centro', 'Sede Centro'),
            ('Sede Sur', 'Sede Sur'),
        ]
    )

    # Área médica correspondiente a la cita
    area = models.CharField(
        max_length=100,
        choices=[
            ('Cardiología', 'Cardiología'),
            ('Neurología', 'Neurología'),
            ('Dermatología', 'Dermatología'),
        ]
    )

    # Motivo de la cita médica (opcional)
    motivo = models.TextField(blank=True, null=True)

    # Estado de la cita: activa o cancelada
    estado = models.CharField(
        max_length=10,
        choices=[
            ('ACTIVA', 'Activa'),
            ('CANCELADA', 'Cancelada'),
        ],
        default='ACTIVA'
    )

    # Fecha y hora de creación de la cita (automático)
    creado = models.DateTimeField(auto_now_add=True)

    # Representación legible de la cita
    def __str__(self):
        return f'Cita de {self.paciente.username} con {self.doctor.get_full_name()} ({self.area}) el {self.fecha} a las {self.hora}'
