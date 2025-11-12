# models.py 

from django.db import models


class Medicina(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre Comercial")
    principio_activo = models.CharField(max_length=100, verbose_name="Principio Activo")
    stock = models.IntegerField(default=0, verbose_name="Stock Disponible")
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")
    necesita_receta = models.BooleanField(default=False, verbose_name="Requiere Receta Médica")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Medicina"
        verbose_name_plural = "Medicinas"


class Paciente(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('RC', 'Registro Civil'),
    ]

    tipo_documento = models.CharField(max_length=2, choices=TIPO_DOCUMENTO_CHOICES, default='CC')
    numero_documento = models.CharField(max_length=20, unique=True, verbose_name="Número de Documento")
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.numero_documento})"

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Especialidad")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción General")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"


class Medico(models.Model):
    especialidad = models.ForeignKey(
        Especialidad, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name="Especialidad"
    )
    licencia_medica = models.CharField(max_length=50, unique=True, verbose_name="Licencia Médica")
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
       
        especialidad_str = str(self.especialidad) if self.especialidad else "Sin asignar"
        return f"Dr(a). {self.nombres} {self.apellidos} ({especialidad_str})"

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

class Cita(models.Model):
    paciente = models.ForeignKey(
        Paciente, 
        on_delete=models.CASCADE, 
        verbose_name="Paciente"
    )
    medico = models.ForeignKey(
        Medico, 
        on_delete=models.CASCADE, 
        verbose_name="Médico Asignado"
    )
    fecha_cita = models.DateField(verbose_name="Fecha de la Cita")
    hora_cita = models.TimeField(verbose_name="Hora de la Cita")
    motivo = models.TextField(verbose_name="Motivo de la Cita")
    estado = models.CharField(max_length=20, default='Pendiente') 

    def __str__(self):
        return f"Cita de {self.paciente} con {self.medico} el {self.fecha_cita} a las {self.hora_cita}"

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
       
        unique_together = ('medico', 'fecha_cita', 'hora_cita')
  