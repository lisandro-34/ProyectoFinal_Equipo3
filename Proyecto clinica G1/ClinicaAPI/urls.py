"""
URL configuration for ClinicaAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
]
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# proyecto_app/urls.py

from django.urls import path
from . import views

app_name = 'pacientes' # Namespace para esta app

urlpatterns = [
    # C: Create
    path('crear/', views.PacienteCrear.as_view(), name='crear_paciente'), 
    
    # R: Read (Listar)
    path('', views.PacienteListar.as_view(), name='listar_pacientes'),
    
    # U: Update
    # <pk> es la llave primaria que identifica al objeto a editar
    path('editar/<int:pk>/', views.PacienteEditar.as_view(), name='editar_paciente'), 
    
    # D: Delete
    path('eliminar/<int:pk>/', views.PacienteEliminar.as_view(), name='eliminar_paciente'),
]

# NOTA: Recuerda incluir estas URLs en el urls.py principal de tu proyecto.