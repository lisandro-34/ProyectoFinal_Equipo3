from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Paciente
from .forms import PacienteForm # type: ignore

# R - READ (Lista de Pacientes)
def paciente_lista(request):
    pacientes = Paciente.objects.all()
    # Pasa la lista de pacientes a la plantilla paciente_lista.html
    return render(request, 'pacientes/paciente_lista.html', {'pacientes': pacientes})

# C - CREATE / U - UPDATE (Crear y Editar)
def paciente_form(request, pk=None):
    # Si pk es None, es un nuevo registro (CREAR)
    # Si pk tiene valor, carga el objeto existente (ACTUALIZAR)
    paciente = None
    if pk:
        paciente = get_object_or_404(Paciente, pk=pk)
    
    # Crea una instancia del formulario, pasándole los datos POST si existen
    form = PacienteForm(request.POST or None, instance=paciente)

    if request.method == 'POST' and form.is_valid():
        # Guarda los datos en la base de datos
        form.save()
        return redirect('paciente_lista')
        
    # Renderiza la plantilla del formulario
    return render(request, 'pacientes/paciente_form.html', {'form': form, 'paciente': paciente})

# D - DELETE (Eliminar)
def paciente_eliminar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    
    if request.method == 'POST':
        # Confirma la eliminación
        paciente.delete()
        return redirect('paciente_lista')
        
    # Renderiza una página de confirmación de eliminación
    return render(request, 'pacientes/paciente_confirm_delete.html', {'paciente': paciente})