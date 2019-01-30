from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.


class Usuarios(models.Model):
	user = models.ForeignKey(User, db_column='user', blank=True, null=True,related_name='user')
	nombre=models.CharField(max_length=100,blank=True,null=True)
	telefono=models.CharField(max_length=100,blank=True,null=True)
	direccion=models.CharField(max_length=100,blank=True,null=True)
	empresa=models.CharField(max_length=100,blank=True,null=True)
	distrito=models.CharField(max_length=100,blank=True,null=True)
	ruc=models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.nombre

class Productos(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)
	prefijo=models.CharField(max_length=100,blank=True,null=True)
	url=models.CharField(max_length=100,blank=True,null=True)

	
	def __unicode__(self):
		return self.nombre

class Usuarios_Productos(models.Model):
	
	usuario = models.ForeignKey(Usuarios, blank=True, null=True)
	producto = models.ForeignKey(Productos, blank=True, null=True)
	
class Estadotareas(models.Model):

    
    nombre  =models.CharField(max_length=1000,blank=True, null=True)


    def __unicode__(self):
        return self.nombre


class Programadores(models.Model):
	
	nombre = models.CharField(max_length=100,blank=True,null=True)
	edad = models.CharField(max_length=100,blank=True,null=True)
	telefono = models.CharField(max_length=100,blank=True,null=True)
	user = models.ForeignKey(User, blank=True, null=True)

	def __unicode__(self):
		return self.nombre
	

class Tareas(models.Model):

    nombre=models.CharField(max_length=1000,blank=True, null=True)
    programador =models.ForeignKey(Programadores, models.DO_NOTHING, db_column='programador', blank=True, null=True)
    descripcion=models.TextField(max_length=1000,blank=True, null=True)
    estado  =models.ForeignKey(Estadotareas, models.DO_NOTHING, db_column='estado_tarea', blank=True, null=True)
    fecha_inicio=models.DateField(blank=True, null=True)
    fecha_fin=models.DateField(blank=True, null=True)
    tiempo_estimado=models.TimeField(blank=True, null=True)
    costo=models.CharField(max_length=1000,blank=True, null=True)
    revisado=models.BooleanField(blank=True, default=False)
    comentario=models.TextField(max_length=1000,blank=True, null=True)

    @property
    def monto(self):
        return self.tiempo_estimado


    class Meta:
        managed = True
        verbose_name = 'Tareas / Incidencias'

    def __unicode__(self):
        return self.nombre


