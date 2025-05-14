
from usuarios.decorators import role_required
from django.shortcuts import render, redirect, get_object_or_404
from pacientes.models import Cita
from datetime import datetime, time, timedelta
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from usuarios.models import Profile





@login_required
@role_required(['STAFF', 'ADMIN'])
def secretaria_dashboard(request):
    return render(request, 'secretaria/secretaia_pantalla_inicio.html')

@login_required
@role_required(['STAFF', 'ADMIN'])
def ver_citas_secretaria(request):
    citas = Cita.objects.all().order_by('-fecha', '-hora')
    paciente_id = request.GET.get('paciente')
    doctor_id = request.GET.get('doctor')
    fecha = request.GET.get('fecha')
    estado = request.GET.get('estado')
    lugar = request.GET.get('lugar')

    if paciente_id:
        citas = citas.filter(paciente__id=paciente_id)
    if doctor_id:
        citas = citas.filter(doctor__id=doctor_id)
    if fecha:
        citas = citas.filter(fecha=fecha)
    if estado:
        citas = citas.filter(estado=estado)
    if lugar:
        citas = citas.filter(lugar=lugar)

    pacientes = User.objects.filter(groups__name='Pacientes')
    doctores = User.objects.filter(groups__name='Medicos')

    return render(request, 'secretaria/secretaria_ver_citas.html', {
        'citas': citas,
        'pacientes': pacientes,
        'doctores': doctores,
        'filtros': {
            'paciente': paciente_id,
            'doctor': doctor_id,
            'fecha': fecha,
            'estado': estado,
            'lugar': lugar,
        }
    })

@login_required
@role_required(['STAFF', 'ADMIN'])
def ver_detalle_cita_secretaria(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    return render(request, 'secretaria/secretaria_ver_detalle_cita.html', {'cita': cita})

@login_required
@role_required(['STAFF', 'ADMIN'])
def crear_citas_secretaria(request):
    pacientes = User.objects.filter(groups__name='Pacientes')
    doctores = User.objects.filter(groups__name='Medicos')
    horas_disponibles = generar_intervalos()

    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        doctor_id = request.POST.get('doctor')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        lugar = request.POST.get('lugar')
        motivo = request.POST.get('motivo', '')

        try:
            paciente = User.objects.get(id=paciente_id)
            doctor = User.objects.get(id=doctor_id)
            area = doctor.profile.especialidad

            conflicto = Cita.objects.filter(
                doctor=doctor,
                fecha=fecha,
                hora=hora,
                estado='CONFIRMADA'
            ).exists()

            if conflicto:
                horarios_ocupados = Cita.objects.filter(
                    doctor=doctor,
                    fecha=fecha,
                    estado='CONFIRMADA'
                ).values_list('hora', flat=True)

                return render(request, 'secretaria/secretaria_crear_cita.html', {
                    'error': 'El doctor ya tiene una cita en ese horario.',
                    'pacientes': pacientes,
                    'doctores': doctores,
                    'horas_disponibles': horas_disponibles,
                    'horarios_ocupados': horarios_ocupados
                })

            Cita.objects.create(
                paciente=paciente,
                doctor=doctor,
                fecha=fecha,
                hora=hora,
                lugar=lugar,
                area=area,
                motivo=motivo
            )
            messages.success(request, 'Cita creada exitosamente.')
            return redirect('ver_citas_secretaria')

        except User.DoesNotExist:
            return render(request, 'secretaria/secretaria_crear_cita.html', {
                'error': 'El paciente o doctor no existe.',
                'pacientes': pacientes,
                'doctores': doctores,
                'horas_disponibles': horas_disponibles
            })

    return render(request, 'secretaria/secretaria_crear_cita.html', {
        'pacientes': pacientes,
        'doctores': doctores,
        'horas_disponibles': horas_disponibles
    })


@login_required
@role_required(['STAFF', 'ADMIN'])
def editar_cita_secretaria(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)  # 👈 Corregido
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
            return render(request, 'secretaria/secretaria_editar_cita.html', {
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
        return redirect('ver_citas_secretaria')  # Asegúrate que este nombre de URL esté correcto

    return render(request, 'secretaria/secretaria_editar_cita.html', {
        'cita': cita,
        'doctores': doctores,
        'horas_disponibles': horas_disponibles,
        'horarios_ocupados': horarios_ocupados,
    })


from django.contrib import messages

@login_required
@role_required(['STAFF', 'ADMIN'])
def cancelar_cita_secretaria(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)

    if request.method == 'POST':
        cita.estado = 'CANCELADA'
        cita.save()
        messages.success(request, "La cita ha sido cancelada correctamente.")
        return redirect('ver_citas_secretaria')

    return render(request, 'secretaria/secretaria_cancelar_cita.html', {'cita': cita})

@login_required
@role_required(['STAFF', 'ADMIN'])
def gestionar_pacientes_secretaria(request):
    pacientes = User.objects.filter(groups__name='Pacientes').order_by('last_name')
    return render(request, 'secretaria/secretaria_gestionar_pacientes.html', {'pacientes': pacientes})

@login_required
def crear_paciente(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya está registrado.")
        else:
            usuario = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            # ✅ Agregar al grupo "pacientes"
            try:
                grupo_pacientes = Group.objects.get(name='pacientes')
                grupo_pacientes.user_set.add(usuario)
            except Group.DoesNotExist:
                messages.warning(request, "El grupo 'pacientes' no existe. El usuario fue creado sin grupo.")

            # ✅ Crear perfil con rol "PATIENT"
            Profile.objects.create(user=usuario, role='PATIENT')

            messages.success(request, f"Usuario {usuario.username} creado exitosamente.")
            return redirect('gestionar_pacientes')

    return render(request,'secretaria/secretaria_crear_usuario.html')

@login_required
@role_required(['STAFF', 'ADMIN'])
def editar_paciente(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        # Validaciones básicas si quieres evitar conflictos
        if User.objects.exclude(id=usuario.id).filter(username=username).exists():
            messages.error(request, "Ya existe un usuario con ese nombre de usuario.")
        elif User.objects.exclude(id=usuario.id).filter(email=email).exists():
            messages.error(request, "Ya existe un usuario con ese correo.")
        else:
            usuario.username = username
            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            if password:
                usuario.set_password(password)  # Solo si se quiere actualizar la contraseña
            usuario.save()
            messages.success(request, "Usuario actualizado correctamente.")
            return redirect('gestionar_pacientes')

    return render(request, 'secretaria/secretaria_editar_paciente.html', {'usuario': usuario})

@login_required
def eliminar_paciente(request, paciente_id):
    usuario = get_object_or_404(User, id=paciente_id)

    if request.method == 'POST':
        usuario.delete()
        messages.success(request, "Paciente eliminado correctamente.")
        return redirect('gestionar_pacientes')  # asegúrate de que exista esta URL

    messages.error(request, "La solicitud para eliminar no es válida.")
    return redirect('gestionar_pacientes')

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