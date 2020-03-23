from django.db import models


class Vacuna(models.Model):
    nombre = models.CharField(max_length = 1000)
    esquema_de_inmunizacion = models.CharField(max_length = 1000)
    tipo_ganado = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre + ' ' + str(self.tipo_ganado) + ' ' + self.esquema_de_inmunizacion

class Productor(models.Model):
    lugar = models.CharField(max_length = 1000)
    nombre = models.CharField(max_length = 1000)

    def __str__(self):
        return self.nombre + ' ' + self.lugar

class Producto(models.Model):
    productor = models.ForeignKey(Productor, on_delete = models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete = models.CASCADE)
    fecha_produccion = models.DateTimeField('Fecha de Produccion')
    fecha_caducidad = models.DateTimeField('Fecha de Caducidad')
    lote = models.IntegerField(default = 0)
    dosis_bulbo = models.IntegerField(default = 0)
    cantidad = models.IntegerField(default = 0)

    def __str__(self):
        return self.productor + ' ' + self.vacuna + ' ' + str(self.lote)


class Sectores_Unidades(models.Model):
    provincia = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 1000)

    def __str__():
        return self.nombre + ' ' + self.provincia



class ComercialNacional(models.Model):
    lugar = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 1000)

    def __str__():
        return self.nombre


class ProductoComercial(models.Model):
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    comercializadora = models.ForeignKey(ComercialNacional, on_delete = models.CASCADE)
    cantidad = models.IntegerField(default = 0)
    fecha = models.DateTimeField('fecha de distribucion')

    def __str__():
        return self.comercializadora + ' ' + self.producto + ' ' + str(self.fecha) + ' ' + str(self.cantidad)

class ComercialProvincial(models.Model):
    provincia = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 1000)

    def __str__():
        return self.nombre + ' ' + self.provincia

class DistribucionComercializadoras(models.Model):
    c_nacional = models.ForeignKey(ComercialNacional, on_delete = models.CASCADE)
    c_provincial = models.ForeignKey(ComercialProvincial, on_delete = models.CASCADE)
    producto = models.ForeignKey(ProductoComercial, on_delete = models.CASCADE)
    fecha = models.DateTimeField('fecha de venta entre comercializadoras')
    cantidad = models.IntegerField(default = 0)

    def __str__():
        return  self.c_nacional + ' ' + self.c_provincial + ' ' + self.producto + ' ' + str(self.fecha) + ' ' + str(self.cantidad)


class VentaSectores(models.Model):
    c_provincial = models.ForeignKey(ComercialProvincial, on_delete = models.CASCADE)
    sector_unidad = models.ForeignKey(Sectores_Unidades, on_delete = models.CASCADE)
    producto = models.ForeignKey(DistribucionComercializadoras, on_delete = models.CASCADE)
    fecha = models.DateTimeField('fecha de venta a sectores')
    cantidad = models.IntegerField(default = 0)

    def __str__():
        return self.c_provincial + ' ' + self.sector_unidad + ' ' + self.producto + ' ' + str(self.fecha) + ' ' + str(self.cantidad)

class AplicacionDeVacuna(models.Model):
    sector_unidad = models.ForeignKey(Sectores_Unidades, on_delete = models.CASCADE)
    producto = models.ForeignKey(VentaSectores, on_delete = models.CASCADE)
    fecha = models.DateTimeField('fecha de aplicacion de vacuna')
    cantidad = models.IntegerField(default = 0)

    def __str__():
        return self.sector_unidad + ' ' + self.producto + ' ' + str(self.fecha) + ' ' + str(self.cantidad)

