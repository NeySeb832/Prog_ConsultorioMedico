# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : signals.py (módulo usuarios)
# Función del Archivo : Crea y guarda automáticamente el perfil asociado a cada usuario del sistema.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# -----------------------------------------------------------------------------
# SEÑAL: create_user_profile
# Descripción:
#   Se ejecuta justo después de crear un nuevo objeto User.
#   Crea automáticamente un perfil (Profile) asociado al nuevo usuario.
# -----------------------------------------------------------------------------
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

# -----------------------------------------------------------------------------
# SEÑAL: save_user_profile
# Descripción:
#   Se ejecuta cada vez que se guarda un objeto User.
#   Si el usuario tiene perfil asociado, lo guarda también.
# -----------------------------------------------------------------------------
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
