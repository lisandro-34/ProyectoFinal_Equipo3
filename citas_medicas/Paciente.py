# =======================================================
# 3. Entidad: Paciente
# =======================================================
from django.contrib.auth.models import User
from django.db import models


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