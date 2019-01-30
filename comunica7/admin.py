from django.contrib import admin
from comunica7.models import *
from django.db.models import Sum
# Register your models here.

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
 	list_display = ('id','nombre','telefono','direccion','empresa','distrito','ruc')

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','prefijo')


@admin.register( Usuarios_Productos)
class  Usuarios_ProductosAdmin(admin.ModelAdmin):
 	list_display = ('id','usuario','producto')
   
@admin.register(Estadotareas)
class EstadotareasAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Programadores)
class ProgramadoresAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Tareas)
class TareasAdmin(admin.ModelAdmin):
	list_display = ('id','descripcion','costo','tiempo_estimado','estado','revisado')
	list_editable = ('revisado',)

	def changelist_view(self, request, extra_context=None):
		total = Tareas.objects.aggregate(total=Sum('costo'))['total']
		
		context = {
			'total': total
		
		}
		return super(TareasAdmin, self).changelist_view(request, extra_context=context)

