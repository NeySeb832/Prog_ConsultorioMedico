from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Opción 1: Mostrar Profile en línea (dentro del User)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Perfil'
    verbose_name_plural = 'Perfiles'

# Extender el UserAdmin
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]  # 👈 Añade el Profile al editar User

# Re-registrar UserAdmin
admin.site.unregister(User)  # Desregistrar el admin por defecto
admin.site.register(User, CustomUserAdmin)  # Registrar con la versión personalizada
admin.site.register(Profile)  # 👈 Opcional: para editar perfiles por separado