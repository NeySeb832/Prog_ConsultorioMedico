# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : apps.py (módulo doctores)
# Función del Archivo : Configura y registra la aplicación "doctores" dentro del proyecto.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.apps import AppConfig

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA APLICACIÓN
# Esta clase define la configuración de la aplicación 'doctores'.
# Es utilizada por Django para registrar la app correctamente.
# -----------------------------------------------------------------------------
class DoctoresConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Tipo de clave primaria por defecto
    name = 'doctores'  # Nombre de la aplicación
