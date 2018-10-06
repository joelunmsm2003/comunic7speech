#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from app.models import *
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

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')


@admin.register(Campania)
class CampaniaAdmin(admin.ModelAdmin):
	list_display = ('id','archivo','fecha','nombre','estado','base')
	list_editable = ('estado',)



	def base(self, obj):

		return 'http://localhost:8000/admin/app/base/?campania__id__exact='+str(obj.id)

	def save_model(self, request, obj, form, change):
		
		super(CampaniaAdmin, self).save_model(request, obj, form, change)

		caption = str(Campania.objects.get(id=obj.id).archivo)

		df = pd.read_excel(caption)

		for i in range(df.shape[0]):

			print i

			fecha_promesa = df['fechapromesa'][i]
			nombres = df['nombre'][i]
			deuda = df['deuda'][i]
			telefono_1 = df['telefono'][i]

			#Base(campania_id=obj.id,nombres=nombres,telefono_1=telefono_1,deuda=deuda).save()

			DBlaster(tipo=3,oc7_2=0,cliente_id=1,dtmf=1,fh_inicio=datetime.datetime.today(),destino=telefono_1,campania_id=obj.id,lestado=0,parametro_1=deuda,parametro_2=nombres,parametro_3=fecha_promesa).save()



		
@admin.register(Estadocampania)
class EstadocampaniaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	


@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
	list_display = ('id','anexo')
	list_filter=('supervisor',)

@admin.register(Api)
class ApiAdmin(admin.ModelAdmin):
	list_display = ('id','host','url','metodo','header')

@admin.register(DBlaster)
class DBlasterAdmin(admin.ModelAdmin):
	list_display = ('id_d_blaster','dtmf','cliente','uid','fh_inicio','destino','lestado')
	list_filter =('campania','campania__estado')


@admin.register(DLlamadas)
class DLlamadasAdmin(admin.ModelAdmin):
	list_display = ('cliente','uid','destino','audio','derivacion','dtmf','despedida','flagfin')


	