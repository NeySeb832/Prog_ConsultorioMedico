from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def redirect_by_role(request):
    profile = request.user.profile  # Accede al perfil vinculado al usuario

    if profile.role == 'ADMIN':
        return redirect('admin_dashboard')  # nombre de tu URL
    elif profile.role == 'DOCTOR':
        return redirect('doctores_dashboard')
    elif profile.role == 'STAFF':
        return redirect('secretaria_dashboard')
    elif profile.role == 'PATIENT':
        return redirect('pacientes_dashboard')
    else:
        return redirect('no_permission')  # o puedes mostrar un mensaje de error



