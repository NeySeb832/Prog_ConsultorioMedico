from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('DOCTOR', 'Doctor'),
        ('STAFF', 'Secretaría'),
        ('PATIENT', 'Paciente'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    especialidad = models.CharField(max_length=50, blank=True, null=True)  # si aplica

    def __str__(self):
        return f"{self.user.username} - {self.role}"
