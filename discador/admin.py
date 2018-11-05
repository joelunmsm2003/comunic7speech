from django.contrib import admin
from discador.models import *
# Register your models here.

@admin.register(Estado_cliente)
class Estado_clienteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')



@admin.register(Tipo_contacto)
class Tipo_contactoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Tipo_persona)
class Tipo_personaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

# @admin.register(Estado_cliente)
# class Estado_clienteAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')


@admin.register(Cartera)
class CarteraAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')


@admin.register(Tipo_direccion)
class Tipo_direccionAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Direcciones)
class DireccionesAdmin(admin.ModelAdmin):
	list_display = ('id','cliente','ubigeo','direccion','observacion','tipo_direccion','plano','cuadrante','fuente','estado','tipo_domicilio')

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','supervisor','anexo','estado','user','t_inicio_gestion','t_fin_gestion','t_inicio_llamada','t_fin_llamada','t_inicio_espera','t_fin_espera','contactadas','contactadas')





@admin.register(Tipo_telefono)
class Tipo_telefonoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')



@admin.register(Fuente_telefono)
class Fuente_telefonoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')



@admin.register(Telefonos)
class TelefonosAdmin(admin.ModelAdmin):
	list_display = ('id','numero_documento','discado','numero_telefono','observacion','tipo_contacto','tipo_telefono','fuente_telefono','estado','cliente')



@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')




@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id','user','dni','operacion','telefono','razon_social','tipo_persona','tipo_documento','numero_documento','nombres','observacion','fecha','estado')

@admin.register(Cuentas)
class CuentasAdmin(admin.ModelAdmin):
	list_display = ('id','cliente','capital','numero_cuenta','total','compania','mora','interes','dias_mora','tramo','fecha_vencimiento','estado','Proveedor','cartera' )


@admin.register(Segmentacion)
class SegmentacionAdmin(admin.ModelAdmin):
	list_display = ('id','telefono','orden','cliente','base')


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
	list_display = ('id','correo','observacion','tipo_contacto','fuente','estado','cliente')








