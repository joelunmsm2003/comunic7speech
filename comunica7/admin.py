from django.contrib import admin
from comunica7.models import *
# Register your models here.

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
 	list_display = ('id','nombre','telefono','direccion','empresa','distrito','ruc')

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','prefijo')


# @admin.register( Usuarios_Productos)
# class  Usuarios_ProductosAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre',' usuarios')
   

    