# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : views.py (módulo mainpage)
# Función del Archivo : Define las vistas públicas e informativas como el home, médicos, servicios y sobre nosotros.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from django.shortcuts import render
from django.http import HttpResponse

# -----------------------------------------------------------------------------
# VISTA: home
# Descripción:
#   Renderiza la página principal del consultorio médico.
# -----------------------------------------------------------------------------
def home(request):
    return render(request, 'Home/home.html')

# -----------------------------------------------------------------------------
# VISTA: medicos
# Descripción:
#   Renderiza la página informativa que muestra los médicos disponibles.
# -----------------------------------------------------------------------------
def medicos(request):
    return render(request, 'nuestros_medicos/nuestros_medicos.html')

# -----------------------------------------------------------------------------
# VISTA: servicios
# Descripción:
#   Renderiza la página informativa con los servicios que ofrece el consultorio.
# -----------------------------------------------------------------------------
def servicios(request):
    return render(request, 'Servicios/servicios.html')

# -----------------------------------------------------------------------------
# VISTA: sobre_nosotros
# Descripción:
#   Renderiza la página institucional "Sobre Nosotros".
# -----------------------------------------------------------------------------
def sobre_nosotros(request):
    return render(request, 'Sobre_nosotros/sobre_nosotros.html')