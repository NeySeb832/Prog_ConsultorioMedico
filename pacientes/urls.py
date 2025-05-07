from django.urls import path
from .views import pacientes_dashboard, ver_citas, crear_cita, editar_cita, eliminar_cita
urlpatterns = [
    path('dashboard/', pacientes_dashboard, name='pacientes_dashboard'),

    path('citas/', ver_citas, name='ver_citas'),
    path('citas/crear/', crear_cita, name='crear_cita'),
    path('citas/editar/<int:cita_id>/', editar_cita, name='editar_cita'),
    path('citas/eliminar/<int:cita_id>/', eliminar_cita, name='eliminar_cita'),
]