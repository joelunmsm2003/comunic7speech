# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# from django.contrib import admin
# from app.models import *
# from django.contrib.admin import RelatedOnlyFieldListFilter

# from django.contrib.admin import AdminSite
# from django.utils.translation import ugettext_lazy
# from django.http import HttpResponse,JsonResponse
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# import os.path
# import json
# import requests
# from django.contrib.admin.filters import DateFieldListFilter
# import pandas as pd

# @admin.register(Cliente)
# class ClienteAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')


# @admin.register(Campania)
# class CampaniaAdmin(admin.ModelAdmin):
# 	list_display = ('id','archivo','fecha','nombre','estado')
# 	list_editable = ('estado',)




# 	def save_model(self, request, obj, form, change):
		
# 		super(CampaniaAdmin, self).save_model(request, obj, form, change)

# 		caption = str(Campania.objects.get(id=obj.id).archivo)

# 		df = pd.read_excel(caption)

# 		for i in range(df.shape[0]):

# 			print i

# 			fecha_promesa = df['fechapromesa'][i]
# 			nombres = df['nombre'][i]
# 			deuda = df['deuda'][i]
# 			telefono_1 = df['telefono'][i]

# 			#Base(campania_id=obj.id,nombres=nombres,telefono_1=telefono_1,deuda=deuda).save()

# 			DBlaster(tipo=3,oc7_2=0,cliente_id=1,dtmf=1,fh_inicio=datetime.datetime.today(),destino=telefono_1,campania_id=obj.id,lestado=0,parametro_1=deuda,parametro_2=nombres,parametro_3=fecha_promesa).save()



		
# @admin.register(Estadocampania)
# class EstadocampaniaAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')
	
# @admin.register(Estado)
# class EstadoAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')
	


# @admin.register(Agente)
# class AgenteAdmin(admin.ModelAdmin):
# 	list_display = ('id','anexo')
# 	list_filter=('supervisor',)

# @admin.register(Api)
# class ApiAdmin(admin.ModelAdmin):
# 	list_display = ('id','host','url','metodo','header')

# @admin.register(DBlaster)
# class DBlasterAdmin(admin.ModelAdmin):
# 	list_display = ('id_d_blaster','dtmf','cliente','uid','fh_inicio','destino','lestado')
# 	list_filter =('campania','campania__estado')


# class ListFilter(admin.SimpleListFilter):
# 	# Human-readable title which will be displayed in the
# 	# right admin sidebar just above the filter options.
# 	title ='Resultado de llamada'

# 	# Parameter for the filter that will be used in the URL query.
# 	parameter_name = 'resultado'



# 	def lookups(self, request, model_admin):
# 		"""
# 		Returns a list of tuples. The first element in each
# 		tuple is the coded value for the option that will
# 		appear in the URL query. The second element is the
# 		human-readable name for the option that will appear
# 		in the right sidebar.
# 		"""
# 		return (
# 			('Dijo Si', 'Dijo Si'),
# 			('Dijo No', 'Dijo No'),
# 			('Escucho Gracias', 'Escucho Gracias'),
# 			('Disculpa', 'Disculpa'),
# 			('No entiendo', 'No entiendo'),
# 			('Corta rapido < 2 Seg', 'Corta rapido < 2 Seg'),
# 		)

# 	def queryset(self, request, queryset):

		
# 		for r in request.GET:

# 			if r=='resultado':

# 				if request.GET['resultado']=='Dijo Si':

# 					return queryset.filter(respuesta01=1,respuesta02=0)

# 				if request.GET['resultado']=='Dijo No':

# 					return queryset.filter(respuesta01=2,respuesta02=0)

# 				if request.GET['resultado']=='Escucho Gracias':

# 					return queryset.filter(respuesta01=1,respuesta02=1)

# 				if request.GET['resultado']=='Disculpa':

# 					return queryset.filter(respuesta01=2,respuesta02=2)

# 				if request.GET['resultado']=='No entiendo':

# 					return queryset.filter(respuesta01=3,respuesta02=0)

# 				if request.GET['resultado']=='Corta rapido < 2 Seg':

# 					return queryset.filter(respuesta01=0,respuesta02=0)

# @admin.register(DLlamadas)
# class DLlamadasAdmin(admin.ModelAdmin):
# 	list_display = ('cliente','destino','audio','dtmf','despedida','respuesta01','respuesta02','respuesta')
# 	list_filter = (ListFilter,)

# 	def respuesta(self, obj):

# 		if obj.respuesta01==1 and obj.respuesta02==0:

# 			return 'Dijo Si'

# 		if obj.respuesta01==2 and obj.respuesta02==0:

# 			return 'Dijo No'

# 		if obj.respuesta01==1 and obj.respuesta02==1:

# 			return 'Escucho Gracias'

# 		if obj.respuesta01==2 and obj.respuesta02==2:

# 			return 'Disculpa'

# 		if obj.respuesta01==3 and obj.respuesta02==0:

# 			return 'No entiendo'

# 		if obj.respuesta01==0 and obj.respuesta02==0:

# 			return 'Corta rapido < 2 Seg'









# 	