import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Producto, Pedido, Cliente, Venta
from django.forms.widgets import DateInput 
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
from django import forms


# Create your views here.



class ventaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['fecha_entrega' , 'fecha_cobrado', 'fecha_facturacion', 'pago','entregado','total']
        widgets = {
            'fecha_cobrado': DateInput(attrs={'type': 'date'}),
            'fecha_entrega': DateInput(attrs={'type': 'date'}),
            'fecha_facturacion': DateInput(attrs={'type': 'date'}),
        }


def home(request):

    productos = Producto.objects.all()

    

    if request.method=='POST':

        try:

            rango = len(request.POST.getlist("Codigo"))

            pedidos = []

            total = 0

            for i in range(rango):
            
                if request.POST.getlist("Numero")[i]!="":  

                    Pedido.objects.create(

                        cliente = Cliente.objects.get(direccion__icontains=request.POST["Cliente"][0:-2]),
                        aclaraciones = request.POST.getlist("Aclaracion")[i],
                        cantidad = request.POST.getlist("Numero")[i],
                        codigo = Producto.objects.get(codigo= request.POST.getlist("Codigo")[i]),
                        nombre = request.POST.getlist("Nombre")[i], 
                        subtotal = float(request.POST.getlist("Bulto")[i]),
                        total = float(request.POST.getlist("Bulto")[i])*
                                    int(request.POST.getlist("Numero")[i])
                    )

                    total+= float(request.POST.getlist("Bulto")[i])* int(request.POST.getlist("Numero")[i])
                    pedidos.append(Pedido.objects.latest("id").id)
                    

            Venta.objects.create(

                cliente = Cliente.objects.get(direccion__icontains=request.POST["Cliente"][0:-2]),
                aclaraciones = "",
                subtotal = total/1.21,
                total = total

            )

            for i in pedidos:
                Venta.objects.latest("id").pedidos.add(i)

        except ObjectDoesNotExist:

            advertencia = True
            
            context = {"productos":productos, "advertencia":advertencia}
    
            return render(request, "MercadoDelPlata/productos.html", context)
            
            
           

        return redirect('home')

    
    context = {"productos":productos}
    
    return render(request, "MercadoDelPlata/productos.html", context)

def Mventa(request):

    ventas=Venta.objects.all()
    
    print(request.POST)
    
    context = {"ventas":ventas}

    return render(request, "MercadoDelPlata/mventa.html", context)


def Eventa(request, pk):

    venta=Venta.objects.get(id=pk)
    form = ventaForm(instance=venta)

    if request.method=="POST":
        form = ventaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()

            return redirect('mventa')


    context = {"form":form , "venta":venta}

    

def Apedir(request):

    fecha = date.today()

    pedidos = Pedido.objects.all().filter(fecha__contains = fecha)

    cantidades = {}

    for i in range(len(pedidos)): 
        if str(pedidos[i].codigo) in cantidades:
            cantidades.update({str(pedidos[i].codigo) : int(pedidos[i].cantidad)+cantidades[str(pedidos[i].codigo)]})
        
        else:
            cantidades.update({str(pedidos[i].codigo) : int(pedidos[i].cantidad)})

    ventas = Venta.objects.all().filter(fecha__contains = fecha)
    
    print(ventas[0].pedidos.all())
    
    context = {"cantidades":cantidades , "ventas":ventas}

    return render(request, "MercadoDelPlata/apedir.html", context)

def Scripts(request):

    productos = Producto.objects.all()

    context= {"resultado":productos}

    return render(request, "MercadoDelPlata/scripts.html",context)