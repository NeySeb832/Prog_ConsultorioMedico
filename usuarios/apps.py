# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : apps.py (módulo usuarios)
# Función del Archivo : Configura la app 'usuarios' y registra señales al iniciar el proyecto.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.apps import AppConfig

# -----------------------------------------------------------------------------
# CLASE: UsuariosConfig
# Descripción:
#   Configura la app 'usuarios' y asegura la carga de señales (signals) al inicio.
# -----------------------------------------------------------------------------
class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

    # Método que se ejecuta cuando la app está lista
    def ready(self):
        import usuarios.signals  # Registro de señales para creación automática de perfiles
