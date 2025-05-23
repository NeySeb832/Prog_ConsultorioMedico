# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : models.py (módulo usuarios)
# Función del Archivo : Define el modelo Profile que extiende el modelo de usuario con rol y especialidad.
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
# MODELO: Profile
# Descripción:
#   Extiende el modelo User para añadir un campo de rol y, si aplica,
#   una especialidad médica (para los doctores).
#
# Relación:
#   - Uno a Uno con el modelo User (cada usuario tiene un perfil único).
#
# Campos:
#   - role: Rol del usuario (ADMIN, DOCTOR, STAFF, PATIENT).
#   - especialidad: Campo opcional para la especialidad médica (solo doctores).
# -----------------------------------------------------------------------------
class Profile(models.Model):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('DOCTOR', 'Doctor'),
        ('STAFF', 'Secretaría'),
        ('PATIENT', 'Paciente'),
    )

    # Asociación uno a uno con el usuario del sistema
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # Rol asignado al usuario
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Especialidad médica (solo aplicable si el rol es DOCTOR)
    especialidad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
