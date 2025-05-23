# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : urls.py (módulo doctores)
# Función del Archivo : Define las rutas específicas del módulo de doctores (panel y detalle de citas).
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.urls import path
from .views import doctores_dashboard, detalle_cita

# -----------------------------------------------------------------------------
# DEFINICIÓN DE RUTAS DEL MÓDULO DE DOCTORES
# - 'dashboard/': Muestra el panel principal del doctor.
# - 'citas/<int:cita_id>/': Muestra los detalles de una cita específica según su ID.
# -----------------------------------------------------------------------------
urlpatterns = [
    path('dashboard/', doctores_dashboard, name='doctores_dashboard'),

    path('citas/<int:cita_id>/', detalle_cita, name='detalle_cita'),
]
