from django.shortcuts import render, redirect
from .models import Producto, Pedido, Cliente, Venta

# Create your views here.




def home(request):

    productos = Producto.objects.all()

    if request.method=='POST':

        lista_pedidos=[]

        for i in productos:
        
            if request.POST.get(str(i.id)+"N")!="":
               
                pedido = Pedido.objects.create(

                    cliente = Cliente.objects.get(id=1), #va por ID
                    aclaraciones = request.POST.get(str(i.id)+"T"),
                    cantidad = request.POST.get(str(i.id)+"N"),
                    codigo = i,
                    nombre = "hola",
                    subtotal = int(request.POST.get(str(i.id)+"N"))*2,
                    total = 300.5
                )

                

                lista_pedidos.append(pedido.id)

        venta = Venta.objects.create(

            cliente = Cliente.objects.get(id=1),
            aclaraciones = "a",
            subtotal = 1,
            total = 1

        )

        for i in lista_pedidos:
        
            venta.pedidos.add(i)
       
        #print(lista_pedidos)

        return redirect('home')


    context = {"productos":productos}
    
    return render(request, "MercadoDelPlata/productos.html", context)

def detalle_pedidos(request):

    tabla=False
    
    if request.method == "POST":

        tabla=True

    context={'tabla':tabla}
    return render(request, "MercadoDelPlata/detalle_pedidos.html", context)

