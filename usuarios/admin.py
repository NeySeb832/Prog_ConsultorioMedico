# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : admin.py (módulo usuarios)
# Función del Archivo : Personaliza el panel de administración para gestionar usuarios y perfiles.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from .models import Profile

# Obtener el modelo de usuario personalizado (si aplica)
User = get_user_model()

# -----------------------------------------------------------------------------
# CLASE: ProfileInline
# Descripción:
#   Permite visualizar y editar el perfil del usuario (modelo Profile)
#   directamente desde el formulario del usuario en el panel de administración.
# -----------------------------------------------------------------------------
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Perfil'
    verbose_name_plural = 'Perfiles'

# -----------------------------------------------------------------------------
# CLASE: CustomUserAdmin
# Descripción:
#   Extiende el UserAdmin estándar para incluir el modelo Profile en línea
#   y asignar automáticamente grupos según el tipo de usuario creado.
# -----------------------------------------------------------------------------
class CustomUserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Si es un usuario nuevo, asignar grupo automáticamente
        if not change:
            try:
                if obj.is_staff and not obj.is_superuser:
                    grupo_secretaria = Group.objects.get(name="Secretaria")
                    obj.groups.add(grupo_secretaria)
                elif obj.is_superuser:
                    grupo_admin = Group.objects.get(name="Administradores")
                    obj.groups.add(grupo_admin)
                elif hasattr(obj, 'is_doctor') and obj.is_doctor:
                    grupo_doctor = Group.objects.get(name="Medicos")
                    obj.groups.add(grupo_doctor)
            except Group.DoesNotExist:
                pass  # Evita error si el grupo aún no ha sido creado

# -----------------------------------------------------------------------------
# REGISTRO PERSONALIZADO EN EL ADMIN
# Desregistra el modelo de usuario por defecto y lo vuelve a registrar con la configuración personalizada.
# También registra el modelo Profile por separado.
# -----------------------------------------------------------------------------
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
