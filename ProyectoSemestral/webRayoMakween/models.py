from django.db import models

# Create your models here.

class Trabajos (models.Model):
    nombre = models.CharField(primary_key=True,max_length=20)
    descripcion = models.CharField(max_length=200)
    materiales = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

