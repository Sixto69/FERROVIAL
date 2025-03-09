from django.db import models


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.nombre}"  # Muestra ID en el nombre

# Create your models here.
