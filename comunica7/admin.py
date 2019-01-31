from django.contrib import admin
from comunica7.models import *
from django.db.models import Sum
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
# Register your models here.



User.add_to_class('gender', models.BooleanField(default=False))

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
 	list_display = ('id','nombre','telefono','direccion','empresa','distrito','ruc')


class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('gender',)



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)



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

