# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : urls.py
# Función del Archivo : Configura y enruta las URL principales del proyecto a los módulos correspondientes.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.contrib import admin
from django.urls import path, include
from . import views

# -----------------------------------------------------------------------------
# DEFINICIÓN DE PATRONES DE URL
# Aquí se define la lista de rutas del proyecto y cómo se conectan con los distintos módulos
# -----------------------------------------------------------------------------
urlpatterns = [
    # Ruta al panel de administración de Django
    path('admin/', admin.site.urls),

    # Ruta a la página principal (módulo 'mainpage')
    path('', include('mainpage.urls')),

    # Rutas de autenticación (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Ruta para redireccionamiento según el rol del usuario autenticado
    path('redirigir/', views.redirect_by_role, name='redirect_by_role'),

    # Rutas específicas para los módulos por rol
    path('paciente/', include('pacientes.urls')),
    path('medico/', include('doctores.urls')),
    path('secretaria/', include('secretaria.urls')),
]
