# views.py (CORREGIDO)

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Asegúrate de que las importaciones de tus modelos son correctas (incluyendo Especialidad)
from .models import Paciente, Medico, Cita, Especialidad 


# ----------------------------------------------------
# 1. VISTAS PARA PACIENTE (PROTEGIDAS)
# ----------------------------------------------------

# CRUD de Paciente (Todas usan LoginRequiredMixin para protegerlas)
class PacienteListar(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'pacientes/lista_pacientes.html'
    context_object_name = 'pacientes'

class PacienteCrear(LoginRequiredMixin, CreateView):
    model = Paciente
    template_name = 'pacientes/paciente_form.html'
    # Campos del modelo Paciente
    fields = ['tipo_documento', 'numero_documento', 'nombres', 'apellidos', 'fecha_nacimiento', 'telefono', 'email'] 
    success_url = reverse_lazy('pacientes:listar_pacientes') 

class PacienteEditar(LoginRequiredMixin, UpdateView):
    model = Paciente
    template_name = 'pacientes/paciente_form.html'
    # Campos del modelo Paciente
    fields = ['tipo_documento', 'numero_documento', 'nombres', 'apellidos', 'fecha_nacimiento', 'telefono', 'email']
    success_url = reverse_lazy('pacientes:listar_pacientes') 

class PacienteEliminar(LoginRequiredMixin, DeleteView):
    model = Paciente
    template_name = 'pacientes/paciente_confirm_delete.html'
    success_url = reverse_lazy('pacientes:listar_pacientes') 

# ----------------------------------------------------
# 2. VISTAS PARA MÉDICO (PROTEGIDAS)
# ----------------------------------------------------

# CRUD de Médico (Todas usan LoginRequiredMixin para protegerlas)

class MedicoListar(LoginRequiredMixin, ListView):
    model = Medico
    template_name = 'medicos/lista_medicos.html'
    context_object_name = 'medicos'

class MedicoCrear(LoginRequiredMixin, CreateView):
    model = Medico
    template_name = 'medicos/medico_form.html'
    # Campos del modelo Medico
    fields = ['nombres', 'apellidos', 'especialidad', 'licencia_medica', 'telefono', 'email']
    success_url = reverse_lazy('medicos:listar_medicos')

class MedicoEditar(LoginRequiredMixin, UpdateView):
    model = Medico
    template_name = 'medicos/medico_form.html'
    # Campos del modelo Medico
    fields = ['nombres', 'apellidos', 'especialidad', 'licencia_medica', 'telefono', 'email']
    success_url = reverse_lazy('medicos:listar_medicos')

class MedicoEliminar(LoginRequiredMixin, DeleteView):
    model = Medico
    template_name = 'medicos/medicos_confirm_delete.html' 
    success_url = reverse_lazy('medicos:listar_medicos')


class CitaListar(LoginRequiredMixin, ListView):
    model = Cita
    template_name = 'citas/lista_citas.html'
    context_object_name = 'citas'

class CitaCrear(LoginRequiredMixin, CreateView):
    model = Cita
    template_name = 'citas/cita_form.html'
    # CORRECCIÓN: Los campos en models.py son 'fecha_cita' y 'hora_cita', no 'fecha_hora'
    fields = ['paciente', 'medico', 'fecha_cita', 'hora_cita', 'motivo']
    success_url = reverse_lazy('citas:listar_citas')
    
class CitaEditar(LoginRequiredMixin, UpdateView):
    model = Cita
    template_name = 'citas/cita_form.html'
    # CORRECCIÓN: Los campos en models.py son 'fecha_cita' y 'hora_cita', no 'fecha_hora'
    fields = ['paciente', 'medico', 'fecha_cita', 'hora_cita', 'motivo']
    success_url = reverse_lazy('citas:listar_citas')

class CitaEliminar(LoginRequiredMixin, DeleteView):
    model = Cita
    template_name = 'citas/citas_confirm_delete.html'
    success_url = reverse_lazy('citas:listar_citas')
