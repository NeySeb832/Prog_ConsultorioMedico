from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('medicos/', views.medicos, name='Nuestros Medicos'),

    path('servicios/', views.servicios, name='Nuestros Servicios'),

    path('sobre_nosotros/', views.sobre_nosotros, name='Sobre nosotros'),
]