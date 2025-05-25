# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : urls.py (módulo secretaria)
# Función del Archivo : Define las rutas para la gestión de citas y pacientes por parte del personal de secretaría.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.urls import path
from .views import (
    secretaria_dashboard,
    crear_citas_secretaria,
    ver_citas_secretaria,
    editar_cita_secretaria,
    gestionar_pacientes_secretaria,
    ver_detalle_cita_secretaria,
    cancelar_cita_secretaria,
    crear_paciente,
    editar_paciente,
    eliminar_paciente
)

# -----------------------------------------------------------------------------
# DEFINICIÓN DE RUTAS DEL MÓDULO SECRETARÍA
# Estas rutas permiten al personal administrativo gestionar citas y pacientes.
# -----------------------------------------------------------------------------
urlpatterns = [
    path('dashboard_secretaria/', secretaria_dashboard, name='secretaria_dashboard'),  # Panel principal

    path('ver_citas_secretaria/', ver_citas_secretaria, name='ver_citas_secretaria'),  # Ver citas agendadas
    path('crear_cita_secretaria/', crear_citas_secretaria, name='crear_cita_secretaria'),  # Crear cita
    path('editar_cita_secretaria/<int:cita_id>/', editar_cita_secretaria, name='editar_cita_secretaria'),  # Editar cita
    path('ver_detalle_cita_secretaria/<int:cita_id>/', ver_detalle_cita_secretaria, name='ver_detalle_cita_secretaria'),  # Ver detalle de cita
    path('cancelar_cita_secretaria/<int:cita_id>/', cancelar_cita_secretaria, name='cancelar_cita_secretaria'),  # Cancelar cita

    path('gestionar_pacientes/', gestionar_pacientes_secretaria, name='gestionar_pacientes'),  # Gestionar pacientes
    path('crear_paciente', crear_paciente, name='crear_paciente'),  # Registrar paciente
    path('editar_paciente/<int:user_id>/', editar_paciente, name='editar_paciente'),  # Editar paciente
    path('eliminar_paciente/<int:paciente_id>/', eliminar_paciente, name='eliminar_paciente'),  # Eliminar paciente
]

