from django.db import models

# Create your models here.
class PadronGeneral(models.Model):
    idUbigeo = models.CharField(max_length=6,null=True)
    desDep = models.CharField(max_length=60,null=True)
    desProv = models.CharField(max_length=60,null=True)
    desDist = models.CharField(max_length=60,null=True)
    direccion = models.CharField(max_length=100)    
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    telefono_movil = models.CharField(max_length=15, blank=True, null=True)
    condicion = models.CharField(max_length=15, blank=True, null=True)
    correo_electronico = models.CharField(max_length=50, blank=True, null=True)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    usuario_alta = models.CharField(max_length=15, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True, null=True)
    usuario_baja = models.CharField(max_length=15, blank=True, null=True)

    #def __str__(self):
    #    return self.nombres

    class Meta:
        #managed = False
        db_table = 'PadronGeneral'

class PersonaNatural(PadronGeneral):
    tipo_documento_identidad = models.CharField(max_length=2, default='1')
    numero_documento = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20, blank=True, null=True)
    nombres = models.CharField(max_length=50)

    def __str__(self):
        return self.nombres

    class Meta:
        #managed = False
        db_table = 'PersonaNatural'

class PersonaJuridica(PadronGeneral):
    tipo_documento_identidad = models.CharField(max_length=2, default='6')
    numero_ruc = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=50)
    nombre_representante = models.CharField(max_length=50)

    def __str__(self):
        return self.razon_social

    class Meta:
        #managed = False
        db_table = 'PersonaJuridica'


class Zona(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    usuario_alta = models.CharField(max_length=15, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True, null=True)
    usuario_baja = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
       return self.nombre

    class Meta:
        #managed = False
        db_table = 'Zona'

class Puesto(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    nota_observacion = models.CharField(max_length=200, blank=True, null=True)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    usuario_alta = models.CharField(max_length=15, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True, null=True)
    usuario_baja = models.CharField(max_length=15, blank=True, null=True)
    pjuridica = models.ForeignKey(PersonaJuridica, on_delete=models.CASCADE, blank=True, null=True)
    pnatural = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE, blank=True, null=True)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        #managed = False
        db_table = 'Puesto'

class Rubro(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    codigo_sunat = models.CharField(max_length=8, default='80131502')
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    usuario_alta = models.CharField(max_length=15, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True, null=True)
    usuario_baja = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        #managed = False
        db_table = 'Rubro'

class Catalogo(models.Model):
    tipo = models.CharField(max_length=30)
    codigo_sunat = models.CharField(max_length=8)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio_publico = models.DecimalField(max_digits=9,decimal_places=4, default=0.00)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    usuario_alta = models.CharField(max_length=15, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True, null=True)
    usuario_baja = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        #managed = False
        db_table = 'Catalogo'


class Empresa(PersonaJuridica):
    contrato = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    catalogos = models.ManyToManyField(Catalogo)

    #def __str__(self):
    #    return self.razon_social

    class Meta:
        #managed = False
        db_table = 'Empresa'


class PuntoVenta(models.Model):
    nombre = models.CharField(max_length=50)
    serie_boleta = models.CharField(max_length=4)
    numero_boleta = models.CharField(max_length=9)
    serie_factura = models.CharField(max_length=4)
    numero_factura = models.CharField(max_length=9)
    serie_ticket = models.CharField(max_length=4)
    numero_ticket = models.CharField(max_length=9)
    serie_nota_credito = models.CharField(max_length=4)
    numero_nota_credito = models.CharField(max_length=9)
    serie_nota_debito = models.CharField(max_length=4)
    numero_nota_debito = models.CharField(max_length=9)
    tocken_punto_venta = models.CharField(max_length=256)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    usuario_alta = models.CharField(max_length=15, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True, null=True)
    usuario_baja = models.CharField(max_length=15, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        #managed = False
        db_table = 'PuntoVenta'

class EquipoPos(models.Model):
    codigo_barra = models.CharField(max_length=30)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    usuario_alta = models.CharField(max_length=15, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True, null=True)
    usuario_baja = models.CharField(max_length=15, blank=True, null=True)
    puntoventa = models.OneToOneField(PuntoVenta, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.codigo_barra

    class Meta:
        #managed = False
        db_table = 'EquipoPos'



class Costo(models.Model):
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_alta = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    fecha_baja = models.DateTimeField(blank=True, null=True)
    usuario_alta = models.CharField(max_length=15, blank=True, null=True)
    usuario_modificacion = models.CharField(max_length=15, blank=True, null=True)
    usuario_baja = models.CharField(max_length=15, blank=True, null=True)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE)

    #def __str__(self):
    #    return self.rubro

    class Meta:
        #managed = False
        db_table = 'Costo'


