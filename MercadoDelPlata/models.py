from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Producto(models.Model):

    codigo = models.CharField(max_length = 7)
    nombre = models.CharField(max_length = 200)
    precio = models.DecimalField(max_digits = 8, decimal_places = 2)
    created = models.DateTimeField(auto_now_add = True)

