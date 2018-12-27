from django.contrib import admin
from colasIN.models import *
from django.contrib.admin import RelatedOnlyFieldListFilter
from daterange_filter.filter import DateRangeFilter
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from PIL import Image
from resizeimage import resizeimage
import os.path
import json
import requests
from django.contrib import admin
from django.contrib.admin.filters import DateFieldListFilter
import xlwt
from datetime import datetime
import csv

from django.shortcuts import redirect
#from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from import_export import resources

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
import time



class VehiculosResource(resources.ModelResource):

    class Meta:
        model = Vehiculo


class AniosResource(resources.ModelResource):

    class Meta:
        model = Anio_v



from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
import time


@admin.register(Casos)
class CasosAdmin(admin.ModelAdmin):
	list_display = ('id','caso','sub_caso')

@admin.register(EstadoAgente)
class EstadoAgenteAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
	list_display = ('id','anexo','estado')


# @admin.register(Person)
# class PersonAdmin(ImportExportModelAdmin):
#     list_display = ('id','name','email','birth_date','location')
#     list_filter=('name',)

#     pass






# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('id','name')
#     list_filter=('name',)



# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title', 'status']
#     ordering = ['title']
#     actions = [make_published]

# admin.site.register(Article, ArticleAdmin)



def Reporte(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/xls')
    response['Content-Disposition'] = 'attachment; filename="books.xls"'
    writer = csv.writer(response)
    writer.writerow(['Id','Fecha','cliente','apellido_p','apellido_m','DNI','telefono_1','telefono_2','Marca del Vehiculo','Modelo','Version','Anio','Color','Motor', 'placa','Kilometraje','cantidad','marca_producto','modelo_bateria',
    'distrito','referencia','nombre_boleta','m_apellido_p','m_apellido_m','dni_c',
    'ruc','razon_social','direccion_rs','pago','correo',' atiende','almacen','gmail','status'
    ,'observaciones','usuario'])
    books = queryset.values_list('fecha','status','marca_vehiculo','modelo','anio','color__nombre','cilindrada', 'placa','cantidad','marca_producto','modelo_bateria','id','usuario__username','telefono_1','telefono_2','cliente','apellido_p','apellido_m')
    for book in books:
        writer.writerow(book)
    return response
Reporte.short_description = 'Reporte en  csv'




def export_books(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/xls')
    response['Content-Disposition'] = 'attachment; filename="books.xls"'
    writer = csv.writer(response)
    writer.writerow(['Id','Fecha','cliente','apellido_p','apellido_m','DNI','telefono_1','telefono_2','Marca del Vehiculo','Modelo','Version','Anio','Color','Motor', 'placa','Kilometraje','cantidad','marca_producto','modelo_bateria',
    'distrito','referencia','nombre_boleta','m_apellido_p','m_apellido_m','dni_c',
    'ruc','razon_social','direccion_rs','pago','correo',' atiende','almacen','gmail','status'
    ,'observaciones','usuario'])
    books = queryset.values_list('id','fecha','cliente','apellido_p','apellido_m','dni','telefono_1','telefono_2','marca_vehiculo','modelo','version','anio__nombre','color__nombre','cilindrada', 'placa','kilometraje','cantidad','marca_producto','modelo_bateria',
    'distrito__nombre','referencia','nombre_boleta','m_apellido_p','m_apellido_m','dni_c',
    'ruc','razon_social','direccion_rs','pago__nombre','correo','atiende__nombre','almacen__nombre','gmail','status__nombre','observaciones','usuario__username'
        )
    for book in books:

        print 'csv....',book
        writer.writerow(book)
    return response
export_books.short_description = 'Export to excel'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title',]
    actions = [export_books]



admin.site.register(Article, ArticleAdmin)



class MyAdminSite(AdminSite):
    site_header = 'POS Administrador'

admin_site = MyAdminSite(name='myadmin')
#admin_site.register(Pos)



# Register your models here.


class ColoresResource(resources.ModelResource):
    class Meta:
        model = Colores_v

@admin.register(Colores_v)
class Colores_vAdmin(ImportExportModelAdmin):
    list_display = ('id','nombre')
    list_filter=('nombre',)
    resource_class=ColoresResource


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
	list_display = ('id','nombres')
	list_filter=('nombres',)


@admin.register(Anio_v)
class Anio_vAdmin(ImportExportModelAdmin):
    list_display = ('id','nombre')
    list_filter=('nombre',)
    resource_class = AniosResource

class DistritoResource(resources.ModelResource):

    class Meta:
        model = Distrito


@admin.register(Distrito)
class DistritoAdmin(ImportExportModelAdmin):
	list_display = ('id','nombre')
	list_filter=('nombre',)




@admin.register(Vehiculo)
class VehiculoAdmin(ImportExportModelAdmin):
    list_display = ('id','nombre','modelo')
    list_filter=('nombre',)
    resource_class = VehiculosResource



@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):

    list_display = ('id','fecha','atiende','fecha_atencion','cliente','apellido_p','ruc','marca_vehiculo','modelo')
    search_fields=('id','cliente','dni')
    #a= User=request.user
    list_editable =('atiende',)
    #list_filter = (('fecha', DateRangeFilter),'usuario','marca_vehiculo','modelo')
    
    actions = [export_books,'enviar_whatssap' ]

    def enviar_whatssap(modeladmin, request, queryset):
    #queryset.update(status='p')
        for q in queryset:

            print q.cliente
            ## representacion del tiempo
            print "Fecha FORMAO "  + time.strftime("%x")
            print "LA HORAAA.....",(time.strftime("%d/%m/%y"))

            return redirect('https://wa.me/'+str(q.atiende.celular)+'?text=FECHA INSTALACION++++++++:++++++++'+str(q.fecha_atencion.strftime("%d/%m/%y"))+'%0D%0A'+
            '%20HORA++++++++:++++++++'+str(q.hora_instalacion.strftime("%I :%M %p"))+'%0D%0A'+
            '%20SERVICIO++++++++:++++++++'+str(q.status)+'%0D%0A'+
            '%20VEHICULO++++++++:++++++++'+str(q.marca_vehiculo)+'%0D%0A'+
            '%20MODELO++++++++:++++++++'+str(q.modelo)+'%0D%0A'+
            '%20ANIO++++++++:++++++++'+str(q.anio.nombre)+'%0D%0A'+
            '%20COLOR++++++++:++++++++'+str(q.color.nombre)+'%0D%0A'+
            '%20MOTOR++++++++:++++++++'+str(q.cilindrada)+'%0D%0A'+
            '%20PLACA++++++++:++++++++'+str(q.placa)+'%0D%0A'+
            '%20CANTIDAD++++++++:++++++++'+str(q.cantidad)+'%0D%0A'+
            '%20BATERIA++++++++:++++++++'+str(q.marca_producto)+'%0D%0A'+
            '%20MODELO++++++++:++++++++'+str(q.modelo_bateria)+'%0D%0A'+
            '%20PRECIO++++++++:++++++++'+str(q.precio)+'%0D%0A'+
            '%20CLIENTE++++++++:++++++++'+str(q.cliente)+'%20  %20'+str(q.apellido_p)+'%20  %20'+str(q.apellido_m)+'%0D%0A'+
            '%20DNI++++++++:++++++++'+str(q.dni)+'%0D%0A'+
            '%20TELEFONOS++++++++:++++++++'+str(q.telefono_1)+'%20  %20'+str(q.telefono_2)+'%0D%0A'+
            '%20DIRECCION++++++++:++++++++'+str(q.direccion)+'%0D%0A'+
            '%20REFERENCIA++++++++:++++++++'+str(q.referencia)+'%0D%0A'+
            '%20PAGO++++++++:++++++++'+str(q.pago)+'%0D%0A'+
            #'%20DOCUMENTO++++++++:++++++++'+str(q.documento)+'%0D%0A'+
            '%20RUC++++++++:++++++++'+str(q.ruc)+'%0D%0A'+
            '%20RAZON+SOCIAL++++++++:++++++++'+str(q.razon_social)+'%0D%0A'+
            '%20DIRECCION_RAZON_SOCIAL++++++++'+str(q.direccion_rs)+'%0D%0A'+
            # '%20DIRECCION++++++++:++++++++'+str(q.direccion1)+'%0D%0A'+
            '%20CLIENTE++++++++:++++++++'+str(q.nombre_boleta)+'%20  %20'+str(q.m_apellido_p)+'%20  %20'+str(q.dni_c)+'%0D%0A'+
            '%20GMAP++++++++:++++++++'+str(q.gmail)+'%0D%0A'+
            '%20ATIENDE++++++++:++++++++'+str(q.atiende.nombre)+'%0D%0A')





class BateriasResource(resources.ModelResource):

    class Meta:
        model = Bateria


@admin.register(Bateria)
class BateriaAdmin(ImportExportModelAdmin):

    list_display = ('id','codigo','marca','modelo','precio','descuento','equivalencia')
    search_fields=('cantidad',)
    list_filter = (('marca', DropdownFilter),)
    resource_class = BateriasResource

@admin.register(Pago)
class PagoAdmin(ImportExportModelAdmin):
    list_display = ('id','nombre')
    search_fields=('nombre',) 
    pass     


# @admin.register(Atiende)
# class AtiendeAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre','celular')
#     search_fields=('nombre',)


@admin.register(Atiende)
class AtiendeAdmin(ImportExportModelAdmin):
    list_display = ('id','nombre','celular')
    search_fields=('nombre',) 
    pass     

 
# @admin.register(Almacen)
# class AlmacenAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     search_fields=('nombre',) 


@admin.register(Almacen)
class AlmacenAdmin(ImportExportModelAdmin):
    list_display = ('id','nombre')
    search_fields=('nombre',) 
    pass     


# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     search_fields=('nombre',)


@admin.register(Status)
class StatusAdmin(ImportExportModelAdmin):
    list_display = ('id','nombre')
    search_fields=('nombre',) 
    pass     




def bulksms(audience):

	url ="http://smsbulk.pe/SmsBulk/rest/ws/bulkSms"
	username = 'xiencias'
	password = '9nG4SB'


	for recipient in audience:
		
		phone_number = recipient

		message = audience[recipient]

		if phone_number[:3] == '+51':

			phone_number = phone_number[1:12]

		else:

			if phone_number[:2] != '51':

				phone_number = '51%s' % phone_number





		params = {'usr' : username,'pas' : password,'msg' : message ,'num' : phone_number}


		print 'params...',params

		reply = requests.get(url, params=params)

		result1 = reply.text

		return result1






