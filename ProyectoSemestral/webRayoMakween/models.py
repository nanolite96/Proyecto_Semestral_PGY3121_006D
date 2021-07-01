from django.db import models

# Create your models here.

class Trabajos (models.Model):
    nombre = models.CharField(primary_key=True,max_length=20)
    descripcion = models.TextField()
    materiales = models.TextField()

    def __str__(self):
        return self.nombre
