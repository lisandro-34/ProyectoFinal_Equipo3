from django.db import models
from django.contrib.auth.models import User

# =======================================================
# 1. Entidad: Paciente
# =======================================================
class Paciente(models.Model):
    """Define los datos personales del paciente."""
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        # Muestra el nombre completo
        return f"Paciente: {self.nombre} {self.apellido}"

    class Meta:
        # Ordenar por apellido y luego por nombre
        ordering = ['apellido', 'nombre']


# =======================================================
# 2. Entidad: Especialidad (para Médicos)
# =======================================================
class Especialidad(models.Model):
    """Define las especialidades médicas."""
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Especialidades"


# =======================================================
# 3. Entidad: Medico
# =======================================================
class Medico(models.Model):
    """Define los datos de un médico y su relación con un usuario del sistema."""
    # Relación 1:1 con Usuario (para login y permisos)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    licencia = models.CharField(max_length=50, unique=True)
    
    # Relación N:M (Muchos Médicos pueden tener Muchas Especialidades)
    especialidades = models.ManyToManyField(Especialidad)
    
    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"

    class Meta:
        verbose_name_plural = "Médicos"


# =======================================================
# 4. Entidad: Cita
# =======================================================

# Opciones de estado de la cita
ESTADOS_CITA = (
    ('P', 'Pendiente'),
    ('C', 'Confirmada'),
    ('R', 'Realizada'),
    ('X', 'Cancelada'),
)

class Cita(models.Model):
    """Define una cita médica relacionando un paciente y un médico."""
    
    # Clave Foránea CORRECTA: Un Paciente tiene Muchas Citas (1:N)
    # IMPORTANTE: Se apunta al modelo Paciente, NO al modelo Medico
    paciente = models.ForeignKey(
        Paciente, 
        on_delete=models.CASCADE,
        related_name='citas_como_paciente' # Nombre de la relación inversa
    ) 
    
    # Clave Foránea: Un Médico tiene Muchas Citas (1:N)
    medico = models.ForeignKey(
        Medico, 
        on_delete=models.CASCADE,
        related_name='citas_asignadas' # Nombre de la relación inversa
    )
    
    fecha_hora = models.DateTimeField() 
    
    # Campo 'estado' usando las opciones definidas
    estado = models.CharField(
        max_length=1,
        choices=ESTADOS_CITA,
        default='P',
    )
    
    def __str__(self):
        # Muestra un resumen de la cita
        return f"Cita de {self.paciente.apellido} con Dr. {self.medico.apellido} el {self.fecha_hora.strftime('%d/%m/%Y a las %H:%M')}"

    class Meta:
        # Garantiza que no haya dos citas para el mismo médico a la misma hora exacta
        unique_together = ('medico', 'fecha_hora')
ordering = ('fecha_hora',)