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
	list_display = ('id','fecha','nombre','estado')
	list_editable = ('estado',)

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



			Base(campania_id=obj.id,nombres=nombres,telefono_1=telefono_1,deuda=deuda).save()


		
@admin.register(Estadocampania)
class EstadocampaniaAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')
	
@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
	list_display = ('id','nombres','telefono_1','deuda','fecha_promesa')
	list_filter=('campania',)

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
	list_display = ('id','anexo')
	list_filter=('supervisor',)

@admin.register(Api)
class ApiAdmin(admin.ModelAdmin):
	list_display = ('id','host','url','metodo','header')



	