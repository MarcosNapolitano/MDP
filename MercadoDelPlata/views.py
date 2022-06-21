from django.shortcuts import render
from .models import Producto

# Create your views here.




def home(request):

    productos = Producto.objects.all()

    context = {"productos":productos}
    
    return render(request, "MercadoDelPlata/productos.html", context)

