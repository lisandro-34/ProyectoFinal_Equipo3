"""
URL configuration for mi_proyecto project.

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
from django.urls import path
from . import views

# Nombres de rutas que usaremos en las plantillas y redirects
urlpatterns = [
    # READ: URL para listar todos los pacientes
    path('', views.paciente_lista, name='paciente_lista'), 
    
    # CREATE: URL para crear un nuevo paciente (sin pk)
    path('nuevo/', views.paciente_form, name='paciente_nuevo'), 
    
    # UPDATE: URL para editar un paciente existente (con pk)
    path('editar/<int:pk>/', views.paciente_form, name='paciente_editar'), 
    
    # DELETE: URL para eliminar un paciente
    path('eliminar/<int:pk>/', views.paciente_eliminar, name='paciente_eliminar'), 
]