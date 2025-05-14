from django.urls import path
from .views import secretaria_dashboard, crear_citas_secretaria, ver_citas_secretaria, editar_cita_secretaria, gestionar_pacientes_secretaria, ver_detalle_cita_secretaria, cancelar_cita_secretaria, crear_paciente, editar_paciente, eliminar_paciente

urlpatterns = [
    path('dashboard_secretaria/', secretaria_dashboard, name='secretaria_dashboard'),
    path('ver_citas_secretaria/', ver_citas_secretaria, name='ver_citas_secretaria'),
    path('crear_cita_secretaria/', crear_citas_secretaria, name='crear_cita_secretaria'),
    path('editar_cita_secretaria/<int:cita_id>/', editar_cita_secretaria, name='editar_cita_secretaria'),
    path('getionar_pacientes/', gestionar_pacientes_secretaria, name='gestionar_pacientes'),
    path('ver_detalle_cita_secretaria/<int:cita_id>/', ver_detalle_cita_secretaria, name='ver_detalle_cita_secretaria'),
    path('cancelar_cita_secretaria/<int:cita_id>/', cancelar_cita_secretaria, name='cancelar_cita_secretaria'),
    path('crear_paciente', crear_paciente, name='crear_paciente'),
    path('editar_paciente/<int:user_id>/', editar_paciente, name='editar_paciente'),

    path('eliminar_paciente/<int:paciente_id>/', eliminar_paciente, name='eliminar_paciente'),



]