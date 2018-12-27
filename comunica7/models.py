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
	