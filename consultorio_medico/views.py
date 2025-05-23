# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : views.py (módulo principal)
# Función del Archivo : Redirige al usuario autenticado a su panel correspondiente según su rol.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# -----------------------------------------------------------------------------
# FUNCIÓN: redirect_by_role
# Descripción:
#   Esta vista recibe la petición de un usuario autenticado y, según el rol
#   almacenado en su perfil, lo redirige al panel correspondiente (Admin, Doctor,
#   Secretaria o Paciente). Si el rol no es reconocido, lo redirige a una vista
#   de error o sin permiso.
# -----------------------------------------------------------------------------
@login_required
def redirect_by_role(request):
    profile = request.user.profile  # Accede al perfil del usuario

    if profile.role == 'ADMIN':
        return redirect('admin_dashboard')  # Redirección para administradores
    elif profile.role == 'DOCTOR':
        return redirect('doctores_dashboard')  # Redirección para doctores
    elif profile.role == 'STAFF':
        return redirect('secretaria_dashboard')  # Redirección para secretarias
    elif profile.role == 'PATIENT':
        return redirect('pacientes_dashboard')  # Redirección para pacientes
    else:
        return redirect('no_permission')  # Rol no reconocido o sin permisos
