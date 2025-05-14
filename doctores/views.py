from usuarios.decorators import role_required
from datetime import date
from django.shortcuts import render, get_object_or_404
from pacientes.models import Cita
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
@role_required(['DOCTOR', 'ADMIN'])  # 👈 Solo doctores y admin pueden acceder
def doctores_dashboard(request):
    doctor = request.user
    citas = Cita.objects.filter(doctor=doctor).order_by('fecha', 'hora')
    citas_hoy = citas.filter(fecha=date.today())
    pacientes_unicos = citas.values('paciente').distinct().count()

    context = {
        'doctor': doctor,
        'citas': citas,
        'citas_hoy': citas_hoy,
        'total_citas': citas.count(),
        'pacientes_unicos': pacientes_unicos,
    }
    return render(request, 'medicos/medicos_pantalla_inicio.html', context)


@login_required
@role_required(['DOCTOR', 'ADMIN'])
def detalle_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, doctor=request.user)
    return render(request, 'medicos/medicos_detalle_cita.html', {'cita': cita})

