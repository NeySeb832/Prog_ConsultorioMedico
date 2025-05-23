# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : urls.py (módulo pacientes)
# Función del Archivo : Define las rutas para la gestión de citas desde el módulo del paciente.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.urls import path
from .views import pacientes_dashboard, ver_citas, crear_cita, editar_cita, eliminar_cita

# -----------------------------------------------------------------------------
# DEFINICIÓN DE RUTAS DEL MÓDULO DE PACIENTES
# Incluye las vistas para el dashboard y CRUD de citas del paciente.
# -----------------------------------------------------------------------------
urlpatterns = [
    path('dashboard/', pacientes_dashboard, name='pacientes_dashboard'),  # Panel del paciente

    path('citas/', ver_citas, name='ver_citas'),                          # Lista de citas del paciente
    path('citas/crear/', crear_cita, name='crear_cita'),                 # Crear nueva cita
    path('citas/editar/<int:cita_id>/', editar_cita, name='editar_cita'),# Editar cita existente
    path('citas/eliminar/<int:cita_id>/', eliminar_cita, name='eliminar_cita'),  # Eliminar cita
]
