from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# Create your models here.
