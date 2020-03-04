from django.db import models

class EmpresaVendedora(models.Model):
    lugar = models.CharField(max_length = 1000)
    nombre = models.CharField(max_length = 1000)

    def __str__(self):
        return self.lugar + ' ' + nombre


class EmpresaCompradora(models.Model):
    direccion = models.CharField(max_length = 1000)
    nombre = models.CharField(max_length = 1000)
    organismo_al_que_pertence = models.CharField(max_length = 1000)

    def __str__(self):
        return self.nombre + ' ' + direccion + ' ' + self.organismo_al_que_pertence;

class Fecha(models.Model):
    fecha = models.DateTimeField('fecha')

    def __str__(self):
        return str(self.fecha)

class Comercializdora(models.Model):
    empresa_vendedora = models.ForeignKey(EmpresaVendedora, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.empresa_vendedora)

class Productor(models.Model):
    empresa_vendedora = models.ForeignKey(EmpresaVendedora, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.empresa_vendedora)

class Vacuna(models.Model):
    precio_de_la_dosis = models.IntegerField(default=0)
    nombre = models.CharField(max_length = 1000)
    esquema_de_inmunizacion = models.CharField(max_length = 1000)

    def __str__(self):
        return self.nombre + ' ' + str(self.precio_de_la_dosis) + ' ' + self.esquema_de_inmunizacion

class Produccion(models.Model):
    productor = models.ForeignKey(Productor, on_delete=models.DO_NOTHING)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.productor) + ' ' + str(self.vacuna)

class Producto(models.Model):
    produccion = models.ForeignKey(Produccion, on_delete=models.DO_NOTHING)
    fecha_de_produccion = models.DateTimeField('fecha de produccion')
    fecha_de_caducidad = models.DateTimeField('fecha de caducidad')
    dosis_por_bulbo = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.produccion) + ' ' + str(self.fecha_de_produccion) + ' ' + str(self.fecha_de_caducidad) + ' ' + str(self.dosis_por_bulbo)

class Pedido(models.Model):
    empresa_vendedora = models.ForeignKey(EmpresaVendedora, on_delete=models.DO_NOTHING)
    empresa_compradora = models.ForeignKey(EmpresaCompradora, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    fecha = models.ForeignKey(Fecha, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.producto) + ' ' + str(self.empresa_vendedora) + ' ' + str(self.empresa_compradora) + ' ' + str(self.fecha)

class ProductoComprado(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.pedido)

class Entrega(models.Model):
    fecha = models.ForeignKey(Fecha, on_delete=models.DO_NOTHING)
    cantidad_entregada = models.IntegerField(default=0)
    empresa_compradora = models.ForeignKey(EmpresaCompradora, on_delete=models.DO_NOTHING)
    empresa_vendedora = models.ForeignKey(EmpresaVendedora, on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.producto) + ' ' + str(self.empresa_vendedora) + ' ' + str(self.empresa_compradora) + ' ' + str(self.fecha) + ' ' + str(self.cantidad_entregada)

class Ganado(models.Model):
    tipo_de_ganado = models.CharField(max_length = 1000)
    vacuna_que_se_le_aplica = models.CharField(max_length = 1000)

    def __str__(self):
        return self.tipo_de_ganado + ' ' + self.vacuna_que_se_le_aplica

class Cria(models.Model):
    empresa_compradora = models.ForeignKey(EmpresaCompradora, on_delete=models.DO_NOTHING)
    ganado = models.ForeignKey(Ganado, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.ganado) + ' ' + str(self.empresa_compradora)

class Veterinario(models.Model):
    empresa_compradora = models.ForeignKey(EmpresaCompradora, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length = 1000)
    ci = models.IntegerField(default=0)
    experiencia_laboral = models.CharField(max_length = 1000)

    def __str__(self):
        return self.nombre + ' ' + str(self.ci) + ' ' + str(self.empresa_compradora) + ' ' + self.experiencia_laboral

class Animal(models.Model):
    ganado = models.ForeignKey(Ganado, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length = 1000)

    def __str__(self):
        return self.nombre + ' ' + str(self.ganado)

class AplicacionDeVacuna(models.Model):
    veterinario = models.ForeignKey(Veterinario, on_delete=models.DO_NOTHING)
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    producto_comprado = models.ForeignKey(ProductoComprado, on_delete=models.DO_NOTHING)
    fecha = models.ForeignKey(Fecha, on_delete=models.DO_NOTHING)
    dosis_aplicada = models.IntegerField(default=0)

    def __str__(self):
        return str(self.veterinario) + ' ' + str(self.animal) + ' ' + str(self.producto_comprado) + ' ' + str(self.fecha) + ' ' + str(self.dosis_aplicada)

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)