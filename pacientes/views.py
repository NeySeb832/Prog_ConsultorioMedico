from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def dashboard(request):
    context = {
        'user': request.user,
        'clinic_name': 'Nombre de tu Clínica'
    }
    return render(request, 'pacientes/pacientes_pantalla_inicio.html', context)

