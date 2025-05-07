from django.urls import path
from .views import doctores_dashboard, detalle_cita
urlpatterns = [
    path('dashboard/', doctores_dashboard, name='doctores_dashboard'),

    path('citas/<int:cita_id>/', detalle_cita, name='detalle_cita'),
    ]