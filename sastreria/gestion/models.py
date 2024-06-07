from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    total_prendas = models.IntegerField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.cliente.nombre} - {self.fecha_creacion}"
