from django.contrib import admin

from .models import Productor, Vacuna, Producto, AplicacionDeVacuna, VentaSectores, DistribucionComercializadoras, ComercialProvincial, ProductoComercial, ComercialNacional, Sectores_Unidades

admin.site.register(VentaSectores)
admin.site.register(DistribucionComercializadoras)
admin.site.register(ComercialProvincial)
admin.site.register(ProductoComercial)
admin.site.register(Productor)
admin.site.register(Vacuna)
admin.site.register(Producto)
admin.site.register(ComercialNacional)
admin.site.register(Sectores_Unidades)
admin.site.register(AplicacionDeVacuna)