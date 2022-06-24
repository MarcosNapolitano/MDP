from django.contrib import admin
from.models import Producto, Pedido, Cliente, Pruebaa, Venta

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields=('fecha', "id")


admin.site.register(Producto)
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Cliente)
admin.site.register(Pruebaa)
admin.site.register(Venta,PedidoAdmin)


