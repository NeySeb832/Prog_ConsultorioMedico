# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : urls.py (módulo mainpage)
# Función del Archivo : Define las rutas públicas e informativas del sitio web (home, servicios, sobre nosotros).
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.urls import path
from . import views

# -----------------------------------------------------------------------------
# DEFINICIÓN DE RUTAS DEL MÓDULO MAINPAGE
# - '': Página principal
# - 'medicos/': Página informativa sobre los médicos
# - 'servicios/': Página con la lista de servicios disponibles
# - 'sobre_nosotros/': Página de presentación del consultorio
# -----------------------------------------------------------------------------
urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio

    path('medicos/', views.medicos, name='Nuestros Medicos'),  # Página de médicos

    path('servicios/', views.servicios, name='Nuestros Servicios'),  # Página de servicios

    path('sobre_nosotros/', views.sobre_nosotros, name='Sobre nosotros'),  # Página institucional
]