from django.db import models
from django.contrib.auth.models import User

# =======================================================
# Definición de Opciones (fuera de las clases)
# =======================================================

# 1. ESTADOS para el Modelo Medico
# (Asumiendo que tienes un modelo Especialidad o quieres agregarlo)
class Especialidad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre


# 2. ESTADOS para el Modelo Cita
ESTADOS_CITA = (
    ('P', 'Pendiente'),
    ('C', 'Confirmada'),
    ('R', 'Realizada'),
    ('X', 'Cancelada'),
)


# =======================================================
# 3. Entidad: Paciente
# =======================================================
class Paciente(models.Model):
    # Relación 1:1 con Usuario
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    # Ejemplo de campo con blank=True, null=True
    telefono = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# =======================================================
# 4. Entidad: Medico
# =======================================================
class Medico(models.Model):
    # Relación 1:1 con Usuario
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    licencia = models.CharField(max_length=50, unique=True)
    
    # Relación N:M (Muchos Médicos pueden tener Muchas Especialidades)
    especialidades = models.ManyToManyField(Especialidad)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# =======================================================
# 5. Entidad: Cita
# =======================================================
class Cita(models.Model):
    # **CAMPOS OBLIGATORIOS Y RELACIONES**
    # Las claves foráneas se refieren a las clases definidas arriba
    paciente = models.ForeignKey(Medico, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    
    fecha_hora = models.DateTimeField() 
    
    # Campo 'estado' usando las opciones definidas
    estado = models.CharField(
        max_length=1,
        choices=ESTADOS_CITA,
        default='P',
    )
    
    # **MÉTODO __str__ CORREGIDO**
    def __str__(self):
        # Para evitar errores, accedemos al nombre directamente
        return f"Cita de {self.paciente.nombre} con {self.medico.nombre} el {self.fecha_hora.date()}"