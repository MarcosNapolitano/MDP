from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Producto(models.Model):

    codigo = models.CharField(max_length = 7)
    nombre = models.CharField(max_length = 200)
    precio = models.DecimalField(max_digits = 8, decimal_places = 2)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.codigo + " | " + self.nombre

class Cliente(models.Model):

    nombre = models.CharField(max_length = 100)
    direccion = models.CharField(max_length = 60)
    Cuit = models.CharField(max_length = 15)
    condicion = models.CharField(max_length = 60)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add = True)
    aclaraciones = models.CharField(max_length = 100)
    cantidad = models.DecimalField(max_digits = 4, decimal_places = 0, default=0)
    codigo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 200)
    subtotal = models.DecimalField(max_digits = 8, decimal_places = 2)
    total = models.DecimalField(max_digits = 8, decimal_places = 2)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):

        return str(self.codigo) + " | " + str(self.subtotal) + " | "+ str(self.total) 


class Pruebaa(models.Model):
    
    aclaraciones = models.CharField(max_length = 100)

class Venta(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add = True)
    aclaraciones = models.CharField(max_length = 100)
    pedidos = models.ManyToManyField(Pedido)
    subtotal = models.DecimalField(max_digits = 8, decimal_places = 2)
    total = models.DecimalField(max_digits = 8, decimal_places = 2)

    def __str__(self):

        return "Venta de " + str(self.cliente) + " número " + str(self.id) 