from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Usuarios(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)
	telefono=models.CharField(max_length=100,blank=True,null=True)
	direccion=models.CharField(max_length=100,blank=True,null=True)
	empresa=models.CharField(max_length=100,blank=True,null=True)
	distrito=models.CharField(max_length=100,blank=True,null=True)
	ruc=models.CharField(max_length=100,blank=True,null=True)

class Productos(models.Model):
    nombre=models.CharField(max_length=100,blank=True,null=True)
    prefijo=models.CharField(max_length=100,blank=True,null=True)

class Usuarios_Productos(models.Model):
	
    usuarios = models.ForeignKey(Usuarios, blank=True, null=True)
	