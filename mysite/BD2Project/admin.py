from django.contrib import admin

from .models import EmpresaVendedora, EmpresaCompradora, Comercializdora, Productor, Vacuna, Produccion, Producto, Pedido, ProductoComprado, Entrega, Ganado, Cria, Veterinario, Animal, AplicacionDeVacuna, Fecha

admin.site.register(Fecha)
admin.site.register(EmpresaVendedora)
admin.site.register(EmpresaCompradora)
admin.site.register(Comercializdora)
admin.site.register(Productor)
admin.site.register(Vacuna)
admin.site.register(Produccion)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ProductoComprado)
admin.site.register(Entrega)
admin.site.register(Ganado)
admin.site.register(Cria)
admin.site.register(Veterinario)
admin.site.register(Animal)
admin.site.register(AplicacionDeVacuna)