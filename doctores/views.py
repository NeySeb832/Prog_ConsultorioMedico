from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.decorators import role_required
from django.shortcuts import render

@login_required(login_url='/accounts/login/')
@role_required(['DOCTOR', 'ADMIN'])  # 👈 Solo doctores y admin pueden acceder
def dashboard(request):
    # Define el contexto primero
    context = {
        'user': request.user,
        'role': request.user.profile.role if hasattr(request.user, 'profile') else None,
        # Agrega más variables aquí si las necesitas
    }
    return render(request, 'medicos/medicos_pantalla_inicio.html', context)  # 👈 Pasa el contexto
