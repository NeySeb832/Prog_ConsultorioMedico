from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'Home/home.html')

def medicos(request):
    return render(request, 'nuestros_medicos/nuestros_medicos.html')

def servicios(request):
    return render(request, 'Servicios/servicios.html')

def sobre_nosotros(request):
    return render(request, 'Sobre_nosotros/sobre_nosotros.html')