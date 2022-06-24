from django.shortcuts import render, redirect
from .models import Producto, Pedido, Cliente

# Create your views here.




def home(request):

    productos = Producto.objects.all()

    if request.method=='POST':

        for i in productos:
        
            if request.POST.get(str(i.id)+"N")!="":

                print(request.POST.get(str(i.id)+"T"))
                print(request.POST.get(str(i.id)+"N"))
                print(request.POST.get(str(i.id)+"C"))
       
        
        return redirect('home') #refreshea pasando el parametro del id



    
    

    context = {"productos":productos}
    
    return render(request, "MercadoDelPlata/productos.html", context)

