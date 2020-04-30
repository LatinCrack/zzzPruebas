import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from graphql import GraphQLError
from msMantenimientos.models import *

# TYPEs
class PadronGeneralType(DjangoObjectType):
    class Meta:
        model = PadronGeneral

class PersonaJuridicaType(DjangoObjectType):
    class Meta:
        model = PersonaJuridica

class PersonaNaturalType(DjangoObjectType):
    class Meta:
        model = PersonaNatural

class ZonaType(DjangoObjectType):
    class Meta:
        model = Zona

class PuestoType(DjangoObjectType):
    class Meta:
        model = Puesto

class RubroType(DjangoObjectType):
    class Meta:
        model = Rubro

class CostoType(DjangoObjectType):
    class Meta:
        model = Costo

class CatalogoType(DjangoObjectType):
    class Meta:
        model = Catalogo

class PuntoVentaType(DjangoObjectType):
    class Meta:
        model = PuntoVenta

class EquipoPosType(DjangoObjectType):
    class Meta:
        model = EquipoPos

class EmpresaType(DjangoObjectType):
    class Meta:
        model = Empresa


### QUERYs ###
class Query(ObjectType):

    # PERSONA JURÍDICA
    personajuridica = graphene.Field(PersonaJuridicaType, id=graphene.ID())
    personasjuridicas = graphene.List(PersonaJuridicaType)

    def resolve_personajuridica(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return PersonaJuridica.objects.get(pk=id)
    
    def resolve_personasjuridicas(self, info, **kwargs):
        return PersonaJuridica.objects.all()


    # PERSONA NATURAL
    personanatural = graphene.Field(PersonaNaturalType, id=graphene.ID())
    personasnaturales = graphene.List(PersonaNaturalType)

    def resolve_personanatural(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return PersonaNatural.objects.get(pk=id)
    
    def resolve_personasnaturales(self, info, **kwargs):
        return PersonaNatural.objects.all()


    # ZONA
    zona = graphene.Field(ZonaType, id=graphene.ID())
    zonas = graphene.List(ZonaType)

    def resolve_zona(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Zona.objects.get(pk=id)
    
    def resolve_zonas(self, info, **kwargs):
        return Zona.objects.all()
    

    # PUESTO
    puesto = graphene.Field(PuestoType, id=graphene.ID())
    puestos = graphene.List(PuestoType)
    puestosxpjuridica = graphene.List(PuestoType, pjuridica=graphene.ID())
    puestosxpnatural = graphene.List(PuestoType, pnatural=graphene.ID())

    def resolve_puesto(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Puesto.objects.get(pk=id)
    
    def resolve_puestos(self, info, **kwargs):
        return Puesto.objects.all()

    def resolve_puestosxpjuridica(self, info, **kwargs):
        pjuridica = kwargs.get('pjuridica')

        if pjuridica is not None:
            return Puesto.objects.filter(pjuridica=pjuridica)
    
    def resolve_puestosxpnatural(self, info, **kwargs):
        pnatural = kwargs.get('pnatural')

        if pnatural is not None:
            return Puesto.objects.filter(pnatural=pnatural)
    
    # RUBRO
    rubro = graphene.Field(RubroType, id=graphene.ID())
    rubros = graphene.List(RubroType)

    def resolve_rubro(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Rubro.objects.get(pk=id)
    
    def resolve_rubros(self, info, **kwargs):
        return Rubro.objects.all()


    # COSTO
    costo = graphene.Field(CostoType, id=graphene.ID())
    costos = graphene.List(CostoType)
    costosxpuesto = graphene.List(CostoType, puesto=graphene.ID())

    def resolve_costo(self, info, **kwargs):
        id = kwargs.get('id')
        
        if id is not None:
            return Costo.objects.get(pk=id)
    
    def resolve_costos(self, info, **kwargs):
        return Costo.objects.all()

    def resolve_costosxpuesto(self, info, **kwargs):
        puesto = kwargs.get('puesto')

        if puesto is not None:
            return Costo.objects.filter(puesto=puesto)

# CATALOGO
    catalogo = graphene.Field(CatalogoType, id=graphene.ID())
    catalogos = graphene.List(CatalogoType)

    def resolve_catalogo(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Catalogo.objects.get(pk=id)
    
    def resolve_catalogos(self, info, **kwargs):
        return Catalogo.objects.all()


# PUNTO DE VENTA
    puntoventa = graphene.Field(PuntoVentaType, id=graphene.ID())
    puntoventas = graphene.List(PuntoVentaType)

    def resolve_puntoventa(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return PuntoVenta.objects.get(pk=id)
    
    def resolve_puntoventas(self, info, **kwargs):
        return PuntoVenta.objects.all()


# EQUIPO POS
    equipopos = graphene.Field(EquipoPosType, id=graphene.ID())
    equipoposs = graphene.List(EquipoPosType)

    def resolve_equipopos(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return EquipoPos.objects.get(pk=id)
    
    def resolve_equipoposs(self, info, **kwargs):
        return EquipoPos.objects.all()


# EMPRESA
    empresa = graphene.Field(EmpresaType, id=graphene.ID())
    empresas = graphene.List(EmpresaType)

    def resolve_empresa(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Empresa.objects.get(pk=id)
    
    def resolve_empresas(self, info, **kwargs):
        return Empresa.objects.all()


### MUTACIONES ###
# PERSONA JURIDICA
    # INPUTs #
class PersonaJuridicaInput(graphene.InputObjectType):
    id = graphene.ID()
    idUbigeo = graphene.String()
    desDep = graphene.String()
    desProv = graphene.String()
    desDist = graphene.String()
    direccion = graphene.String()
    telefono_fijo = graphene.String()
    telefono_movil = graphene.String()
    condicion = graphene.String()
    correo_electronico = graphene.String()
    usuario_alta = graphene.String()    
    tipo_documento_identidad = graphene.String()
    numero_ruc = graphene.String()
    razon_social = graphene.String()
    nombre_representante = graphene.String()
        
    
    

class CreatePersonaJuridica(graphene.Mutation):
    class Arguments:
        input = PersonaJuridicaInput(required=True)
    
    ok = graphene.Boolean()
    personajuridica = graphene.Field(PersonaJuridicaType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        personajuridica_instance = PersonaJuridica(
            idUbigeo = input.idUbigeo,
            desDep = input.desDep,
            desProv = input.desProv,
            desDist = input.desDist,
            direccion = input.direccion,
            telefono_fijo = input.telefono_fijo,
            telefono_movil = input.telefono_movil,
            condicion = input.condicion,
            correo_electronico = input.correo_electronico,
            usuario_alta = input.usuario_alta,    
            tipo_documento_identidad = input.tipo_documento_identidad,
            numero_ruc = input.numero_ruc,
            razon_social = input.razon_social,
            nombre_representante = input.nombre_representante,
        )
        personajuridica_instance.save()

        return CreatePersonaJuridica(ok=ok,personajuridica=personajuridica_instance)

# PERSONA NATURAL
    # INPUTs #
class PersonaNaturalInput(graphene.InputObjectType):
    id = graphene.ID()
    idUbigeo = graphene.String()
    desDep = graphene.String()
    desProv = graphene.String()
    desDist = graphene.String()
    direccion = graphene.String()
    telefono_fijo = graphene.String()
    telefono_movil = graphene.String()
    condicion = graphene.String()
    correo_electronico = graphene.String()
    usuario_alta = graphene.String()
    tipo_documento_identidad = graphene.String()
    numero_documento = graphene.String()
    apellido_paterno = graphene.String()
    apellido_materno = graphene.String()
    nombres = graphene.String()   
    

class CreatePersonaNatural(graphene.Mutation):
    class Arguments:
        input = PersonaNaturalInput(required=True)
    
    ok = graphene.Boolean()
    personanatural = graphene.Field(PersonaNaturalType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        personanatural_instance = PersonaNatural(
            idUbigeo = input.idUbigeo,
            desDep = input.desDep,
            desProv = input.desProv,
            desDist = input.desDist,
            direccion = input.direccion,    
            telefono_fijo = input.telefono_fijo,
            telefono_movil = input.telefono_movil,
            condicion = input.condicion,
            correo_electronico = input.correo_electronico,
            usuario_alta = input.usuario_alta,
            tipo_documento_identidad = input.tipo_documento_identidad,
            numero_documento = input.numero_documento,
            apellido_paterno = input.apellido_paterno,
            apellido_materno = input.apellido_materno,
            nombres = input.nombres,     
        )
        personanatural_instance.save()

        return CreatePersonaNatural(ok=ok,personanatural=personanatural_instance)


# CATALOGO
    # INPUTs #
class CatalogoInput(graphene.InputObjectType):
    id = graphene.ID()
    tipo = graphene.String()
    codigo_sunat = graphene.String()
    nombre = graphene.String()
    descripcion = graphene.String()
    precio_publico = graphene.String()
    usuario_alta = graphene.String()

class CreateCatalogo(graphene.Mutation):
    class Arguments:
        input = CatalogoInput(required=True)
    
    ok = graphene.Boolean()
    catalogo = graphene.Field(CatalogoType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        catalogo_instance = Catalogo(
            tipo = input.tipo,
            codigo_sunat = input.codigo_sunat,
            nombre = input.nombre,
            descripcion = input.descripcion,
            precio_publico = input.precio_publico,
            usuario_alta = input.usuario_alta,
        )
        catalogo_instance.save()
        return CreateCatalogo(ok=ok,catalogo=catalogo_instance)


# EMPRESA
    # INPUTs #
class EmpresaInput(graphene.InputObjectType):
    id = graphene.ID()
    idUbigeo = graphene.String()
    desDep = graphene.String()
    desProv = graphene.String()
    desDist = graphene.String()
    direccion = graphene.String()
    telefono_fijo = graphene.String()
    telefono_movil = graphene.String()
    condicion = graphene.String()
    correo_electronico = graphene.String()
    usuario_alta = graphene.String()    
    tipo_documento_identidad = graphene.String()
    numero_ruc = graphene.String()
    razon_social = graphene.String()
    nombre_representante = graphene.String()
    contrato = graphene.String()
    estado = graphene.String()       
    catalogos = graphene.List(CatalogoInput)

class CreateEmpresa(graphene.Mutation):
    class Arguments:
        input = EmpresaInput(required=True)
    
    ok = graphene.Boolean()
    empresa = graphene.Field(EmpresaType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        catalogos = []

        for catalogo_input in input.catalogos:
            catalogo = Catalogo.objects.get(pk=catalogo_input.id)
            if catalogo is None:
                
                return CreateEmpresa(ok=False, catalogo=None)
            catalogos.append(catalogo)
        
        empresa_instance = Empresa(
            idUbigeo = input.idUbigeo,
            desDep = input.desDep,
            desProv = input.desProv,
            desDist = input.desDist,
            direccion = input.direccion,
            telefono_fijo = input.telefono_fijo,
            telefono_movil = input.telefono_movil,
            condicion = input.condicion,
            correo_electronico = input.correo_electronico,
            usuario_alta = input.usuario_alta,    
            tipo_documento_identidad = input.tipo_documento_identidad,
            numero_ruc = input.numero_ruc,
            razon_social = input.razon_social,
            nombre_representante = input.nombre_representante,
            contrato = input.contrato,
            estado = input.estado                        
        )
        empresa_instance.save()
        empresa_instance.catalogos.set(catalogos)
        return CreateEmpresa(ok=ok, empresa=empresa_instance)


# DECLARACIÒN DE MUTACIONES #
class Mutation(graphene.ObjectType):
    create_personajuridica = CreatePersonaJuridica.Field()
    create_personanatural = CreatePersonaNatural.Field()
    create_catalogo = CreateCatalogo.Field()
    create_empresa = CreateEmpresa.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)