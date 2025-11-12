# core/urls.py (Archivo de URLs del proyecto)

from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
  
    path('pacientes/crear/', views.PacienteCrear.as_view(), name='pacientes:crear_paciente'),
    path('pacientes/', views.PacienteListar.as_view(), name='pacientes:listar_pacientes'), 
    path('pacientes/editar/<int:pk>/', views.PacienteEditar.as_view(), name='pacientes:editar_paciente'),
    path('pacientes/eliminar/<int:pk>/', views.PacienteEliminar.as_view(), name='pacientes:eliminar_paciente'),


    path('medicos/crear/', views.MedicoCrear.as_view(), name='medicos:crear_medico'),
    path('medicos/', views.MedicoListar.as_view(), name='medicos:listar_medicos'),
    path('medicos/editar/<int:pk>/', views.MedicoEditar.as_view(), name='medicos:editar_medico'),
    path('medicos/eliminar/<int:pk>/', views.MedicoEliminar.as_view(), name='medicos:eliminar_medico'),


    path('citas/crear/', views.CitaCrear.as_view(), name='citas:crear_cita'),
    path('citas/', views.CitaListar.as_view(), name='citas:listar_citas'), # Este es el 'citas:listar_citas'
    path('citas/editar/<int:pk>/', views.CitaEditar.as_view(), name='citas:editar_cita'),
    path('citas/eliminar/<int:pk>/', views.CitaEliminar.as_view(), name='citas:eliminar_cita'),


    path('admin/', admin.site.urls),
    
    
    path('api/', include('ClinicaAPI.urls')), 
    
  
    path('cuentas/', include('django.contrib.auth.urls')), 
]





