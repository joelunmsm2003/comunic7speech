#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from discador.models import *

from django.contrib.admin import RelatedOnlyFieldListFilter

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
import os.path
import json
import requests
from django.contrib.admin.filters import DateFieldListFilter
import pandas as pd
from django.utils.html import format_html
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin



@admin.register(Subresultado,)
class SubresultadoAdmin(ImportExportModelAdmin):
	list_display = ('id','nombre')
	pass


# @admin.register(Subresultado,)
# class SubresultadoAdmin(admin.ModelAdmin,):
# 	list_display = ('id','nombre')

@admin.register(Negocio)
class NegocioAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Industria)
class IndustriaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')


@admin.register(Gestion)
class GestionAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

# Register your models here.
@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

	#readonly_fields = ('nombre',)

	# def nombre(self, instance):
	# 	# assuming get_full_address() returns a list of strings
	# 	# for each line of the address and you want to separate each
	# 	# line by a linebreak
	# 	return format_html_join(
	# 		mark_safe('<br/>'),
	# 		'{}',
	# 		((line,) for line in instance.get_full_address()),
	# 	) or mark_safe("<span class='errors'>I can't determine this address.</span>")


	# nombre.short_description = "Address"


@admin.register(Cartera)
class CarteraAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(IDGestion)
class IDGestionAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')



@admin.register(ProveedorCarteras)
class ProveedorCarterasAdmin(admin.ModelAdmin):
	list_display = ('id','cartera','proveedor','negocio')
	list_display_links = ('cartera',)
	list_filter = ('proveedor',)


@admin.register(Tipo_cartera)
class Tipo_carteraAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','cod_dpto','cod_prov','cod_dist','dpto','provincia')

@admin.register(Ubigeo)
class UbigeoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')



@admin.register(Cuadrante)
class CuadranteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Estado_cliente)
class Estado_clienteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')






@admin.register(Tipo_contacto)
class Tipo_contactoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Resultado)
class ResultadoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

# @admin.register(Score)
# class ScoreAdmin(admin.ModelAdmin):
# 	list_display = ('id','negocio','gestion','id_gestion','resultado','subresultado')
# 	list_editable=('negocio')
# 	list_filter=('resultado',)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
	list_display = ('id','negocio','gestion','id_gestion','resultado','subresultado')
	

@admin.register(Tipo_persona)
class Tipo_personaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')


@admin.register(ScoreProveedor)
class ScoreProveedorAdmin(admin.ModelAdmin):
	list_display = ('id','proveedor','negocio','gestion','peso_tipo_gestion','id_gestion','peso_id_gestion')
	list_editable = ('peso_tipo_gestion',)

# @admin.register(Estado_cliente)
# class Estado_clienteAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')




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

@admin.register(EstadoScore)
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
	list_display = ('id','nombre','cartera')


	def cartera(self, obj):

		print self
		print '.....'
		print obj.id
		return format_html(
			'<a class="button"  href="/admin/discador/proveedorcarteras/?proveedor__id__exact='+str(obj.id)+'">Cartera</a>'
		)





@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id','user','dni','operacion','telefono','razon_social','tipo_persona','tipo_documento','numero_documento','nombres','observacion','fecha','estado')

@admin.register(Cuentas)
class CuentasAdmin(admin.ModelAdmin):
	list_display = ('id','cliente','numero_cuenta','moneda' )


@admin.register(Segmentacion)
class SegmentacionAdmin(admin.ModelAdmin):
	list_display = ('id','telefono','orden','cliente','base')


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
	list_display = ('id','correo','observacion','tipo_contacto','fuente','estado','cliente')







