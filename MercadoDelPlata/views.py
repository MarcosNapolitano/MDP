from django.shortcuts import render, redirect
from .models import Producto, Pedido, Cliente

# Create your views here.




def home(request):

    if request.method=='POST':

    
        #aca hay que hacer un bucle for con los id de productos
        #y reemplazar el 1 por "i"

        #si la cantidad!=0 entonces agregar en una lista los 3 valores
        #luego por cada una de las listas crear un nuevo "pedido"    
        
        print(request.POST.get("1"+"T"))
        print(request.POST.get("1"+"N"))
        print(request.POST.get("1"+"C"))
       
        
        return redirect('home') #refreshea pasando el parametro del id



    
    productos = Producto.objects.all()

    context = {"productos":productos}
    
    return render(request, "MercadoDelPlata/productos.html", context)

