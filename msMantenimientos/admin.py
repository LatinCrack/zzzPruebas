from django.contrib import admin
from .models import *

# Register your models here.

#@admin.register(PadronGeneral)
#class PadronGeneralAdmin(admin.ModelAdmin):
#    pass

@admin.register(PersonaNatural)
class PersonaNaturalAdmin(admin.ModelAdmin):
    list_display = ('padrongeneral_ptr_id','numero_documento','nombres','apellido_paterno','apellido_materno')

@admin.register(PersonaJuridica)
class PersonaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('padrongeneral_ptr_id','numero_ruc','razon_social','nombre_representante')

@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion','pjuridica','pnatural','zona')

@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion')

@admin.register(Rubro)
class RubroAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion')

@admin.register(Costo)
class CostoAdmin(admin.ModelAdmin):
    list_display = ('id','puesto','rubro','precio')