# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : models.py (módulo usuarios)
# Función del Archivo : Define el modelo Profile que extiende el modelo de usuario con rol, contacto y especialidad.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 23/05/2025
# Versión             : 1.1
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.db import models
from django.contrib.auth.models import User

# -----------------------------------------------------------------------------
# CONSTANTE: ROLE_CHOICES
# Descripción:
#   Define las opciones válidas para el campo de rol del perfil.
# -----------------------------------------------------------------------------
ROLE_CHOICES = (
    ('ADMIN', 'Administrador'),
    ('DOCTOR', 'Doctor'),
    ('STAFF', 'Secretaria'),
    ('PATIENT', 'Paciente'),
)

# -----------------------------------------------------------------------------
# MODELO: Profile
# Descripción:
#   Extiende el modelo User para añadir información adicional como:
#   - Rol del usuario.
#   - Teléfono de contacto.
#   - Dirección de residencia.
#   - Especialidad médica (opcional, para doctores).
#
# Relación:
#   - Uno a Uno con el modelo User (cada usuario tiene un perfil único).
#
# Campos:
#   - user: Relación uno a uno con el usuario.
#   - role: Rol asignado al usuario (ADMIN, DOCTOR, STAFF, PATIENT).
#   - telefono: Número de contacto (opcional).
#   - direccion: Dirección de residencia (opcional).
#   - especialidad: Campo opcional para la especialidad médica (solo doctores).
# -----------------------------------------------------------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    especialidad = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
