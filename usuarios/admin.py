from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from .models import Profile

# Obtener el modelo de usuario activo
User = get_user_model()

# Mostrar el perfil en línea dentro del admin de usuario
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Perfil'
    verbose_name_plural = 'Perfiles'

# Extender UserAdmin para personalizarlo
class CustomUserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # Si es nuevo, asignar automáticamente el grupo según la lógica
        if not change:
            try:
                if obj.is_staff and not obj.is_superuser:
                    grupo_secretaria = Group.objects.get(name="Secretaria")
                    obj.groups.add(grupo_secretaria)
                elif obj.is_superuser:
                    grupo_admin = Group.objects.get(name="Administradores")
                    obj.groups.add(grupo_admin)
                elif hasattr(obj, 'is_doctor') and obj.is_doctor:  # por si agregas esta lógica en el modelo
                    grupo_doctor = Group.objects.get(name="Medicos")
                    obj.groups.add(grupo_doctor)
            except Group.DoesNotExist:
                pass  # Evita error si el grupo aún no fue creado

# Desregistrar el admin por defecto y registrar el personalizado
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
