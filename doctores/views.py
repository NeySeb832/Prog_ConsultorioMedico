# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : views.py (módulo doctores)
# Función del Archivo : Define las vistas relacionadas con los doctores: panel principal y detalle de cita.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from datetime import date
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from usuarios.decorators import role_required  # Decorador personalizado para control de acceso
from pacientes.models import Cita

# -----------------------------------------------------------------------------
# VISTA: doctores_dashboard
# Descripción:
#   Muestra al doctor un resumen de sus citas programadas, incluyendo las del día,
#   total de citas, y cantidad de pacientes únicos.
# Restricciones:
#   - Requiere que el usuario esté autenticado.
#   - Solo accesible por usuarios con rol 'DOCTOR' o 'ADMIN'.
# -----------------------------------------------------------------------------
@login_required(login_url='/accounts/login/')
@role_required(['DOCTOR', 'ADMIN'])
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

# -----------------------------------------------------------------------------
# VISTA: detalle_cita
# Descripción:
#   Muestra los detalles de una cita médica específica a la que el doctor está asignado.
# Restricciones:
#   - Requiere autenticación.
#   - Solo accesible por usuarios con rol 'DOCTOR' o 'ADMIN'.
# -----------------------------------------------------------------------------
@login_required
@role_required(['DOCTOR', 'ADMIN'])
def detalle_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, doctor=request.user)
    return render(request, 'medicos/medicos_detalle_cita.html', {'cita': cita})
