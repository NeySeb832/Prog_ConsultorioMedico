from django.db import models
from django.contrib.auth.models import User


class Cita(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas_paciente')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='citas_doctor')
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=100, choices=[
        ('Sede Norte', 'Sede Norte'),
        ('Sede Centro', 'Sede Centro'),
        ('Sede Sur', 'Sede Sur'),
    ])
    area = models.CharField(max_length=100, choices=[
        ('Cardiología', 'Cardiología'),
        ('Neurología', 'Neurología'),
        ('Dermatología', 'Dermatología'),
    ])
    motivo = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=10, choices=[
        ('ACTIVA', 'Activa'),
        ('CANCELADA', 'Cancelada'),
    ], default='ACTIVA')
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cita de {self.paciente.username} con {self.doctor.get_full_name()} ({self.area}) el {self.fecha} a las {self.hora}'
