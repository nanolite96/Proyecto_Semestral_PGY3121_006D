from django.db import models

# Create your models here.
class mecanico (models.Model):
    nombre_mec = models.CharField(primary_key=True,max_length=10)

    def __str__(self):
        return self.nombre_mec

class Trabajos (models.Model):
    diagnostico = models.CharField(max_length=20)
    nombre = models.ForeignKey(mecanico,on_delete=models.CASCADE)
    fecha = models.TextField()
    materiales = models.TextField()
    categoria = models.TextField()
    imagen = models.ImageField(upload_to='atenciones', null=True)

    def __str__(self):
        return self.nombre

class comentario(models.Model):
    nombre_cl=models.TextField()
    correo=models.TextField()
    asunto=models.TextField()
    sugerencia=models.TextField()
    
    def __str__(self):
        return self.nombre_cl