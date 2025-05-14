from usuarios.decorators import role_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cita
from django.contrib.auth.models import User
from datetime import datetime, time, timedelta

@login_required(login_url='/accounts/login/')
@role_required(['PATIENT', 'ADMIN'])
def pacientes_dashboard(request):
    context = {
        'user': request.user,
        'role': request.user.profile.role if hasattr(request.user, 'profile') else None,
    }
    return render(request, 'pacientes/pacientes_pantalla_inicio.html', context)

@login_required
@role_required(['PATIENT', 'ADMIN'])
def ver_citas(request):
    citas = Cita.objects.filter(paciente=request.user, estado='ACTIVA').order_by('fecha', 'hora')
    return render(request, 'pacientes/pacientes_ver_citas.html', {'citas': citas})

@login_required
@role_required(['PATIENT', 'ADMIN'])
def crear_cita(request):
    doctores = User.objects.filter(profile__role='DOCTOR')
    horas_disponibles = generar_intervalos()

    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        lugar = request.POST.get('lugar')
        doctor_id = request.POST.get('doctor')
        motivo = request.POST.get('motivo', '')

        try:
            doctor = User.objects.get(id=doctor_id)
            area = doctor.profile.especialidad

            conflicto = Cita.objects.filter(
                doctor=doctor,
                fecha=fecha,
                hora=hora,
                estado='CONFIRMADA'
            ).exists()

            if conflicto:
                citas_conflicto = Cita.objects.filter(doctor=doctor, fecha=fecha, estado='CONFIRMADA')
                horarios_ocupados = [c.hora.strftime("%I:%M %p") for c in citas_conflicto]

                return render(request, 'pacientes/pacientes_crear_citas.html', {
                    'error': 'El doctor ya tiene una cita en ese horario.',
                    'doctores': doctores,
                    'horarios_ocupados': horarios_ocupados,
                    'horas_disponibles': horas_disponibles
                })

            Cita.objects.create(
                paciente=request.user,
                doctor=doctor,
                fecha=fecha,
                hora=hora,
                lugar=lugar,
                area=area,
                motivo=motivo
            )
            return redirect('ver_citas')

        except User.DoesNotExist:
            return render(request, 'pacientes/pacientes_crear_citas.html', {
                'error': 'El doctor seleccionado no existe.',
                'doctores': doctores,
                'horas_disponibles': horas_disponibles
            })

    return render(request, 'pacientes/pacientes_crear_citas.html', {
        'doctores': doctores,
        'horas_disponibles': horas_disponibles
    })

@login_required
@role_required(['PATIENT', 'ADMIN'])
def editar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, paciente=request.user)
    doctores = User.objects.filter(profile__role='DOCTOR')
    horas_disponibles = generar_intervalos()

    horarios_ocupados = Cita.objects.filter(
        doctor=cita.doctor,
        fecha=cita.fecha,
        estado='CONFIRMADA'
    ).exclude(id=cita.id).values_list('hora', flat=True)

    horas_disponibles = [h for h in horas_disponibles if h not in horarios_ocupados]

    if request.method == 'POST':
        cita.fecha = request.POST.get('fecha')
        cita.hora = request.POST.get('hora')
        cita.lugar = request.POST.get('lugar')
        doctor_id = request.POST.get('doctor')
        motivo = request.POST.get('motivo', '')

        doctor = get_object_or_404(User, id=doctor_id)

        conflicto = Cita.objects.filter(
            doctor=doctor,
            fecha=cita.fecha,
            hora=cita.hora,
            estado='CONFIRMADA'
        ).exclude(id=cita.id).exists()

        if conflicto:
            return render(request, 'pacientes/pacientes_editar_cita.html', {
                'cita': cita,
                'doctores': doctores,
                'error': 'Ese horario ya está ocupado por otra cita.',
                'horas_disponibles': horas_disponibles,
                'horarios_ocupados': horarios_ocupados,
            })

        cita.doctor = doctor
        cita.area = doctor.profile.especialidad
        cita.motivo = motivo
        cita.save()
        return redirect('ver_citas')

    return render(request, 'pacientes/pacientes_editar_cita.html', {
        'cita': cita,
        'doctores': doctores,
        'horas_disponibles': horas_disponibles,
        'horarios_ocupados': horarios_ocupados,
    })

@login_required
@role_required(['PATIENT', 'ADMIN'])
def eliminar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, paciente=request.user)
    if request.method == 'POST':
        cita.estado = 'CANCELADA'
        cita.save()
        return redirect('ver_citas')
    return render(request, 'pacientes/pacientes_eliminar_citas.html', {'cita': cita})

def generar_intervalos():
    inicio = datetime.strptime("07:00", "%H:%M")
    fin = datetime.strptime("20:00", "%H:%M")
    intervalo = timedelta(minutes=15)
    horarios = []
    actual = inicio
    while actual < fin:
        horarios.append(actual.time())
        actual += intervalo
    return horarios
