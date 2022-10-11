from email.policy import default
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.forms import BooleanField

# Create your models here.


class Producto(models.Model):

    codigo = models.CharField(max_length = 7, unique = True)
    nombre = models.CharField(max_length = 200)
    costo = models.DecimalField(max_digits = 8, decimal_places = 2)
    costo_anterior = models.DecimalField(max_digits = 8, decimal_places = 2,default=0)
    created = models.DateTimeField(auto_now_add = True)
    empresa = models.CharField(max_length = 100)
    bodega = models.CharField(max_length = 100, default="", blank=True)
    incremento = models.DecimalField(max_digits = 4, decimal_places = 3)
    unidades = models.IntegerField()
    estado = models.CharField(max_length = 100, blank=True)

    def __str__(self):
        return self.codigo

    def __str__(self):
        return self.codigo

    def propiedades(self):
        return [self.codigo + self.nombre + str(self.costo) + str(self.created)]

class Cliente(models.Model):

    consumidor_final="CF"
    responsable_inscripto="RI"
    excento="EX"
    condicion_opciones = [
        (responsable_inscripto,"Responsable Inscripto"),
        (consumidor_final,"Consumidor Final"),
        (excento,"Excento")]

    nombre = models.CharField(max_length = 100, unique = True)
    direccion = models.CharField(max_length = 60, unique = True)
    cuit = models.CharField(max_length = 15, unique = True, default=0)
    condicion = models.CharField(max_length = 60, choices=condicion_opciones)

    def __str__(self):
        return self.nombre + " " + self.direccion

class Pedido(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add = True)
    aclaraciones = models.CharField(max_length = 100, blank=True)
    cantidad = models.DecimalField(max_digits = 4, decimal_places = 0, default=0)
    codigo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 200)
    subtotal = models.DecimalField(max_digits = 8, decimal_places = 2)
    total = models.DecimalField(max_digits = 8, decimal_places = 2)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):

        return " x " + str(self.cantidad) + " | " + str(self.codigo) + " | "+ str(self.nombre) + " | "+ str(self.total) 


class Venta(models.Model):

    efectivo="EF"
    transferencia="TF"
    cheque="CH"
    condicion_opciones = [
        (efectivo,"Efectivo"),
        (transferencia,"Transferencia"),
        (cheque,"Cheque")]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add = True)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    fecha_cobrado = models.DateTimeField(blank=True, null=True)
    fecha_facturacion = models.DateTimeField(blank=True, null=True)
    pago = models.CharField(max_length = 60, choices=condicion_opciones,blank=True)
    entregado = models.BooleanField(default=False)
    aclaraciones = models.CharField(max_length = 100, blank=True)
    pedidos = models.ManyToManyField(Pedido)
    subtotal = models.DecimalField(max_digits = 8, decimal_places = 2)
    total = models.DecimalField(max_digits = 8, decimal_places = 2)

    def __str__(self):

        return "Venta de " + str(self.cliente) + " número " + str(self.id) 


class Pruebaa(models.Model):
    
    aclaraciones = models.CharField(max_length = 100)
