# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : decorators.py (módulo usuarios)
# Función del Archivo : Define un decorador personalizado para restringir el acceso a vistas según el rol del usuario.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from functools import wraps

# -----------------------------------------------------------------------------
# DECORADOR: role_required
# Descripción:
#   Este decorador verifica que el usuario autenticado tenga un rol permitido
#   para acceder a la vista protegida. Si no tiene perfil o su rol no es válido,
#   devuelve un error 403 (Prohibido).
#
# Parámetros:
#   allowed_roles: lista de roles permitidos (ej. ['ADMIN', 'STAFF'])
#
# Uso:
#   @role_required(['ADMIN'])
#   def vista_admin(request):
#       ...
# -----------------------------------------------------------------------------
def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        @login_required  # Se asegura primero que el usuario esté autenticado
        def _wrapped_view(request, *args, **kwargs):
            # Verifica que el usuario tenga perfil
            if not hasattr(request.user, 'profile'):
                return HttpResponseForbidden("Perfil de usuario no configurado")

            # Verifica que el rol esté autorizado
            if request.user.profile.role not in allowed_roles:
                return HttpResponseForbidden("No tienes permiso para acceder a esta página")

            # Permite ejecutar la vista si cumple los requisitos
            return view_func(request, *args, **kwargs)

        return _wrapped_view
    return decorator
