# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
import datetime

from django.conf import settings

from django.db import models


from import_export.admin import ImportExportModelAdmin




STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)

class EstadoAgente(models.Model):
    nombre= models.CharField(max_length=1000,blank=True, null=True)
    id_estado = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.nombre



class LogEstadoAgente(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    estado = models.ForeignKey(EstadoAgente, db_column='estado', blank=True, null=True)
    fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today())

    def __unicode__(self):
        return self.nombre

class Agente(models.Model):


    nombre= models.CharField(max_length=1000,blank=True, null=True)
    anexo = models.IntegerField(blank=True, null=True)
    fono = models.IntegerField(blank=True, null=True)
    destino = models.IntegerField(blank=True, null=True)
    duracion = models.TimeField(blank=True, null=True)
    atendidas = models.IntegerField(blank=True, null=True)
    contactadas = models.IntegerField(blank=True, null=True)
    estado = models.ForeignKey('EstadoAgente', db_column='estado', blank=True, null=True,related_name='_estadorelated')
    id_estado = models.IntegerField(blank=True, null=True)
    est_ag_predictivo = models.IntegerField(blank=True, null=True)
    canal = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, db_column='user', blank=True, null=True,related_name='userrelated')
    fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today())
    t_estado = models.DateTimeField(db_column='t_estado', default=datetime.datetime.today())
    acd = models.CharField(max_length=100, blank=True)

class ColasinAcd(models.Model):
    id_acd = models.AutoField(primary_key=True)
    did_campana = models.CharField(db_column='DID_Campana', max_length=45)  # Field name made lowercase.
    numero_llamado = models.CharField(db_column='Numero_Llamado', max_length=45)  # Field name made lowercase.
    numero_entrante = models.CharField(db_column='Numero_Entrante', max_length=45)  # Field name made lowercase.
    channel_entrante = models.CharField(db_column='Channel_Entrante', max_length=50)  # Field name made lowercase.
    tiempo = models.IntegerField(db_column='Tiempo')  # Field name made lowercase.
    flag = models.IntegerField()
    uniqueid = models.CharField(max_length=30)
    fin = models.IntegerField()
    age_nombre = models.CharField(max_length=100, blank=True, null=True)
    tie_ing = models.DateTimeField()
    tie_acd = models.DateTimeField()
    tie_tra = models.DateTimeField()
    tie_con = models.DateTimeField()
    tie_fin = models.DateTimeField()
    tie_acw = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    sql = models.IntegerField()
    codhu = models.IntegerField(db_column='CodHU')  # Field name made lowercase.
    bill = models.IntegerField()
    asterisk = models.IntegerField()
    audio = models.CharField(unique=True, max_length=100)
    valorllamada = models.CharField(max_length=200)
    id_ori_usuario = models.IntegerField()
    llam_estado = models.IntegerField()
    anexo = models.IntegerField()
    duration = models.IntegerField()
    espera = models.IntegerField()
    pais = models.CharField(max_length=10)
    g_id1 = models.CharField(max_length=100)
    g_id2 = models.CharField(max_length=100)
    g_id3 = models.CharField(max_length=100)
    g_id4 = models.CharField(max_length=100)
    g_id5 = models.CharField(max_length=100)
    g_id6 = models.CharField(max_length=100)
    g_id7 = models.CharField(max_length=100)
    g_id8 = models.CharField(max_length=100)
    g_id9 = models.CharField(max_length=100)
    g_id10 = models.CharField(max_length=100)
    accountcode = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'colasIN_acd'

        
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title


class Album(models.Model):
    nombre= models.CharField(max_length=1000,blank=True, null=True)


class Anio_v(models.Model):
    nombre= models.CharField(max_length=1000,blank=True, null=True)

    def __unicode__(self):
        return self.nombre


class Colores_v(models.Model):
    nombre= models.CharField(max_length=1000,blank=True, null=True)

    def __unicode__(self):
        return self.nombre

class Distrito(models.Model):
    nombre= models.CharField(max_length=1000,blank=True, null=True)

    def __unicode__(self):
        return self.nombre


class Bateria(models.Model):
    codigo = models.CharField(max_length=1000,blank=True, null=True)
    equivalencia = models.CharField(max_length=1000,blank=True, null=True)
    cantidad = models.CharField(max_length=1000,blank=True, null=True)
    marca = models.CharField(max_length=1000,blank=True, null=True)
    modelo = models.CharField(max_length=1000,blank=True, null=True)
    precio = models.CharField(max_length=1000,blank=True, null=True)
    descuento = models.CharField(max_length=1000,blank=True, null=True)

    #cant_bat_usadas= models.CharField(max_length=1000,blank=True, null=True)

    def __unicode__(self):
        return self.marca




class Factura(models.Model):
    ruc = models.CharField(max_length=1000,blank=True, null=True)
    r_social = models.CharField(max_length=1000,blank=True, null=True)
    ruc = models.CharField(max_length=1000,blank=True, null=True)
    direc_r_social = models.CharField(max_length=1000,blank=True, null=True)

    def __unicode__(self):

        return self.nombre


class Vehiculo(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    modelo= models.CharField(max_length=1000,blank=True, null=True)
    version= models.CharField(max_length=1000,blank=True, null=True)

    def __unicode__(self):

        return self.modelo

# class Modelo_Auto(models.Model):
#     nombre = models.CharField(max_length=1000,blank=True, null=True)

#     def __unicode__(self):

#         return self.nombre

class Pago(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    
    def __unicode__(self):

        return self.nombre

class Atiende(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    celular = models.CharField(max_length=1000,blank=True, null=True)

    def __unicode__(self):

        return self.nombre

class Almacen(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)


    def __unicode__(self):

        return self.nombre
        
class Status(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)

    def __unicode__(self):

        return self.nombre

class Venta(models.Model):

    fecha = models.DateTimeField(default=datetime.datetime.today())


# Create your models here.
class Clientes(models.Model):

    codigo  =models.CharField(max_length=100,blank=True,null=True)
    nombres =models.CharField(max_length=100,blank=True,null=True)
    apellidos  =models.CharField(max_length=100,blank=True,null=True)
    dni =models.CharField('DNI',max_length=100,blank=True,null=True)
    telefono_1=models.CharField(max_length=100,blank=True,null=True)
    telefono_2 =models.CharField(max_length=100,blank=True,null=True)
    importe=models.CharField(max_length=100,blank=True,null=True)
    fecha_promesa=models.CharField(max_length=100,blank=True,null=True)
    deuda=models.CharField(max_length=100,blank=True,null=True)
    deuda_pendiente=models.CharField(max_length=100,blank=True,null=True)
    fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today()) 






class Produccion(models.Model):

    venta= models.ForeignKey(Venta,help_text='Codigo Venta',max_length=1000,blank=True, null=True)
    fecha = models.DateTimeField(help_text=u'Fecha de recepción de la llamada (No se puede modificar)',default=datetime.datetime.today(),editable=False)
    telefono_1 = models.CharField(help_text=u'Número de teléfono desde donde llama el cliente',max_length=1000,blank=True, null=True)
    telefono_2= models.CharField(help_text=u'Otro nmero de teléfono de contacto',max_length=1000,blank=True, null=True) 
    cliente = models.CharField(help_text=u"Nombre del Cliente",max_length=1000,blank=True, null=True)
    apellido_p=models.CharField("Apellido Paterno",max_length=1000,blank=True, null=True)
    apellido_m=models.CharField("Apellido Materno",max_length=1000,blank=True, null=True)
    dni= models.CharField(help_text=u'Otro nmero de dni',max_length=1000,blank=True, null=True)
    direccion= models.CharField(max_length=1000,blank=True, null=True)
    marca_vehiculo= models.CharField(max_length=1000,blank=True, null=True)
    modelo= models.CharField(max_length=1000,blank=True, null=True)
    version= models.CharField(max_length=1000,blank=True, null=True)
    anio= models.ForeignKey(Anio_v,help_text='Anio',max_length=1000,blank=True, null=True,related_name='_nombre')
    cilindrada= models.CharField(max_length=1000,blank=True, null=True)
    color= models.ForeignKey(Colores_v,help_text='Color',max_length=1000,blank=True, null=True,related_name='_nombre')
    kilometraje= models.CharField(max_length=1000,blank=True, null=True)
    placa=models.CharField(max_length=1000,blank=True, null=True)
    cantidad= models.CharField(max_length=1000,blank=True, null=True)
    marca_producto= models.CharField(max_length=1000,blank=True, null=True)
    modelo_bateria = models.CharField(max_length=1000,blank=True, null=True)
    precio= models.CharField(max_length=1000,blank=True, null=True)
    cantidad_bu= models.CharField(help_text='Cantidad de baterias usadas',max_length=1000,blank=True, null=True)
    descuento= models.CharField(max_length=1000,blank=True, null=True)
    precio_total= models.CharField(max_length=1000,blank=True, null=True)
    fecha_atencion= models.DateField(max_length=1000,blank=True, null=True,)#,input_formats=settings.DATE_INPUT_FORMATS
    hora_instalacion= models.TimeField(max_length=1000,blank=True, null=True) 
    misma_direccion= models.CharField(max_length=1000,blank=True, null=True)
    direccion_atencion= models.CharField(max_length=1000,blank=True, null=True)
    distrito=models.ForeignKey(Distrito,help_text='Distrito',max_length=1000,blank=True, null=True,related_name='_nombre')
    referencia= models.CharField(max_length=1000,blank=True, null=True)
    boleta= models.BooleanField(max_length=1000,blank=True, default=True)
    mismo_cliente= models.CharField(max_length=1000,blank=True, null=True)
    nombre_boleta= models.CharField(max_length=1000,blank=True, null=True)
    m_apellido_p= models.CharField(max_length=1000,blank=True, null=True)
    m_apellido_m= models.CharField(max_length=1000,blank=True, null=True)
    dni_c= models.CharField(max_length=1000,blank=True, null=True)
    factura= models.BooleanField(max_length=1000,blank=True, default=True)
    ruc= models.CharField(max_length=1000,blank=True, null=True)
    razon_social= models.CharField(max_length=1000,blank=True, null=True)
    direccion_rs= models.CharField(max_length=1000,blank=True, null=True)
    pago= models.ForeignKey(Pago,max_length=1000,blank=True, null=True)
    correo= models.CharField(max_length=1000,blank=True, null=True)
    atiende= models.ForeignKey(Atiende,max_length=1000,blank=True, null=True,related_name='_atiende')
    almacen= models.ForeignKey(Almacen,max_length=1000,blank=True, null=True,related_name='_almacen')
    #gmail= models.FileField(upload_to='static')
    gmail= models.CharField(max_length=1000,blank=True, null=True)
    #foto = models.FileField(upload_to='static')
    status= models.ForeignKey(Status,max_length=1000,blank=True, null=True, related_name='_status')
    observaciones= models.CharField(max_length=1000,blank=True, null=True)
    usuario=models.ForeignKey(User,help_text='Usuarios',max_length=1000,blank=True, null=True,related_name='_modelo')
    cierre= models.BooleanField(default=0)
    agente= models.ForeignKey(Agente,max_length=1000,blank=True, null=True,related_name='_agente')

    def __unicode__(self):
        return self.cliente
        


class ProduccionAudio(models.Model):

    produccion= models.ForeignKey(Produccion,help_text='Produccion',max_length=1000,blank=True, null=True)
    audio= models.CharField(max_length=1000,blank=True, null=True) 
    fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today()) 
    telefono = models.CharField(max_length=1000,blank=True, null=True) 
    agente= models.ForeignKey(Agente,max_length=1000,blank=True, null=True,related_name='_agente_produccion_audio')

