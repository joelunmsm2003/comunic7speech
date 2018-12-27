from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.views.generic import View
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import Group, User
#from jwt_auth.compat import json
#from jwt_auth.mixins import JSONWebTokenAuthMixin
from django.template import RequestContext
import simplejson
from django.views.decorators.csrf import csrf_exempt
import xlrd
from django.db.models import Count,Sum
from colasIN.models import *

from app.serializers import *
from django.db.models import Count,Sum
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from colasIN.forms import *
from colasIN.forms_reporte import *
from django.contrib.auth import authenticate
import time
from django.db.models import Func
import os
from datetime import datetime,timedelta,date
import os.path
import requests
import smtplib
from email.mime.text import MIMEText
from django.db.models import Count,Max
import datetime
import random
from django.db.models import Count,Sum
from PIL import Image
from resizeimage import resizeimage
import pandas as pd
from .models import Album
from django.views import generic
import pandas as pd
from django.contrib.auth.models import User
import datetime
from datetime import datetime,timedelta
from django.utils import timezone
from colasIN.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta
import time

import datetime
from datetime import datetime
from datetime import date
import csv

from django.http import HttpResponse
from django.views.generic import View

#from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

#from app.resources import ProduccionResource
from tablib import Dataset


@csrf_exempt
def subir_casos(request):

	df = pd.read_csv('/Users/xiencias/Casos.csv')
	Casos.objects.all().delete()
	# sheet = excel_document.get_sheet_by_name('TELEFONOS')
	# print sheet['A2'].value

	for i in range(df.shape[0]):


		# print df['TIPO GESTION'][i]

		# gestion_id=Gestion.objects.get(nombre=df['TIPO GESTION'][i]).id
		# print df['IDGESTION'][i]
		# id_gestion_id=IDGestion.objects.get(nombre=df['IDGESTION'][i]).id

		# print df['RESULTADO'][i]
		# resultado_id=Resultado.objects.get(nombre=df['RESULTADO'][i]).id
		# print df['JUSTIFICACION'][i]
		# subresultado_id=Subresultado.objects.get(nombre=df['JUSTIFICACION'][i]).id

	
				
		print df['TIPOS DE CASOS'][i]
		caso= df['TIPOS DE CASOS'][i]
		sub_caso = df['SUBTIPO DE CASOS'][i]



		Casos(caso=caso,sub_caso=sub_caso).save()

	return render(request, 'agentes.html',{})



def importar(request):

	

	return render(request, 'import.html',{})



def reportes(request):

	Produccion_resource = ProduccionResource()
	dataset = Produccion.objects.values_list('color__nombre','usuario__username')

	response = HttpResponse(dataset.csv, content_type='text/xls')
	response['Content-Disposition'] = 'attachment; filename="Produccion.xls"'
	list_filter = ('color__nombre',)
	# writer = csv.writer(response)

	# datos =Produccion.objects.values_list('color__nombre','usuario__username')
	# for d in datos:
 #    	   writer.writerow(d)
	return response




def api_motorisado(request):

	print 'engtrree'

	_data = Atiende.objects.all()
	print 'traes la daata?', _data
	serializer =  AtiendeSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)


def reporte(request):

    response = HttpResponse(content_type='text/.xls')
    response['Content-Disposition'] = 'attachment; filename="reporte.xls"'

    writer = csv.writer(response)
    writer.writerow(['Id','Fecha','cliente','apellido_p','apellido_m','DNI','telefono_1','telefono_2','Marca del Vehiculo','Modelo','Version','Anio','Color','Motor', 'placa','Kilometraje','cantidad','marca_producto','modelo_bateria',
	'distrito','referencia','nombre_boleta','m_apellido_p','m_apellido_m','dni_c',
    'ruc','razon_social','direccion_rs','pago','correo',' atiende','almacen','gmail','status',
    'observaciones','usuario' ])
    a= User=request.user
	

    datos =Produccion.objects.filter(usuario_id=a).values_list('id','fecha','cliente','apellido_p','apellido_m','dni','telefono_1','telefono_2','marca_vehiculo','modelo','version','anio__nombre','color__nombre','cilindrada', 'placa','kilometraje','cantidad','marca_producto','modelo_bateria',
	'distrito__nombre','referencia','nombre_boleta','m_apellido_p','m_apellido_m','dni_c',
	'ruc','razon_social','direccion_rs','pago__nombre','correo','atiende__nombre','almacen__nombre','gmail','status__nombre','observaciones','usuario__username')
    for d in datos: 



        writer.writerow(d)

    # users = User.objects.all().values_list('username', 'first_name')
    # for user in users:
    #     writer.writerow(user)

    return response

def usuarios(request):
	usuarios = User.objects.all()
	#recetas = Receta.objects.all()
	#context = {'recetas': recetas, 'usuarios':usuarios}
	print 'usuario00000000000000s',usuarios
	return render(request, 'header.html', context)


def privado(request):
	usuario = request.user
	context = {'usuario': usuario}
	return render(request, 'header.html', context)
	
def nuevopaciente(request):

	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = PacientesForm(request.POST)

		# Create and save the new author instance. There's no need to do anything else.


	# check whether it's valid:
		if form.is_valid():

			a = Pacientes()

			p = PacientesForm(request.POST, instance=a).save()

			#Atencion(paciente_id=p.id).save()

			#id_a = Atencion.objects.all().values('id').order_by('-id')[0]['id']

			#a = Atencion.objects.get(id=id_a)

			#form = AtencionForm(instance=a)





			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return render(request, 'dashboard.html',{'msj': 'Paciente se guardaron con exito','form':form})



	else:
		form = PacientesForm()

	return render(request, 'dashboard.html',{'form': form})



# @login_required(login_url="/dashboard/")
def vehiculos(request):


	if request.method=='POST':

		form = VehiculosForm(request.POST)
	
		if form.is_valid():

			form.save()

		return HttpResponseRedirect("/dashboard")


	if request.method=='GET':

		vehiculos = Vehiculo.objects.all()
		context = {'datos': vehiculos}
		
		formula = VehiculosForm()

		context = {'datoss': formula}

	return render(request, 'dashboard.html',context)

def login2(request):


	# df=pd.read_csv('/home/baterias/MarcasModelosBaterias.csv',header=0)

	# Bateria.objects.all().delete()


	# for i in range(df.shape[0]):

	#   marca = df['MARCA'][i]
	#   modelo = df['MODELO '][i]
	#   equivalencia = df['EQUIVALENCIA'][i]
	#   codigo = df['CODIGO'][i]


	#   Bateria(marca=marca,modelo=modelo,equivalencia=equivalencia,codigo=codigo,).save()


	return render(request, 'login.html',{})

def subir(request):


	df=pd.read_csv('/home/baterias/MarcasModelosBaterias_N.csv',header=0)
	#df=pd.read_csv('/home/jose/codigos/baterias/MarcasModelosBaterias_N.csv',header=0)

	Bateria.objects.all().delete()


	for i in range(df.shape[0]):

		marca = df['MARCA'][i]
		modelo = df['MODELO '][i]
		equivalencia = df['EQUIVALENCIA'][i]
		codigo = df['CODIGO'][i]
		precio = df['PRECIO'][i]
		descuento = df['DESCUENTO'][i]


		Bateria(marca=marca,modelo=modelo,equivalencia=equivalencia,codigo=codigo,precio=precio,descuento=descuento,).save()


	return render(request, 'login.html',{})

def masacre(request):

	
	df=pd.read_csv('/home/baterias/MarcasModelosAutos.csv',header=0)
	#df=pd.read_csv('/home/jose/codigos/baterias/MarcasModelosAutos.csv',header=0)


	Vehiculo.objects.all().delete()
	for i in range(df.shape[0]):

		marca = df['Marca'][i]
		modelo = df['Modelo'][i]
		version = df['Version'][i]
		Vehiculo(nombre=marca,modelo=modelo,version=version,).save()


	return render(request, 'login.html',{})



def dstlima(request):

	
	df=pd.read_csv('/home/baterias/Distrito_lima.csv',header=0)
	#df=pd.read_csv('/home/jose/codigos/baterias/Distrito_lima.csv',header=0)



	Distrito.objects.all().delete()
	for i in range(df.shape[0]):

		nombre = df['Nombre'][i]
		# modelo = df['Modelo'][i]
		# version = df['Version'][i]
		Distrito(nombre=nombre,).save()


	return render(request, 'login.html',{})

def anio(request):

	
	df=pd.read_csv('/home/baterias/Anio_V.csv',header=0)
	#df=pd.read_csv('/home/jose/codigos/baterias/Anio_V.csv',header=0)



	Anio_v.objects.all().delete()
	for i in range(df.shape[0]):

		anio = df['Anio'][i]
		# modelo = df['Modelo'][i]
		# version = df['Version'][i]
		Anio_v(nombre=anio,).save()


	return render(request, 'login.html',{})


def color(request):

	
	df=pd.read_csv('/home/baterias/ColoresAutos.csv',header=0)
	#df=pd.read_csv('/home/jose/codigos/baterias/ColoresAutos.csv',header=0)



	Colores_v.objects.all().delete()
	for i in range(df.shape[0]):

		color = df['COLOR'][i]
		# modelo = df['Modelo'][i]
		# version = df['Version'][i]
		Colores_v(nombre=color,).save()


	return render(request, 'login.html',{})

def disponible(request,id_agente):

	ag = Agente.objects.get(id=id_agente)
	ag.estado_id=1
	ag.save()

	return HttpResponseRedirect('/colasIN/monitor_agente/980729169/0/')

def pausar(request,id_agente):

	ag = Agente.objects.get(id=id_agente)
	ag.estado_id=4
	ag.save()

	return HttpResponseRedirect('/colasIN/monitor_agente/980729169/0/')

def ingresar(request):

	if  request.method == 'POST':


		print 'ACAAAA'


	if  request.method == 'GET':

		user = request.user.id
		print 'usuario, q svr',user

		username = request.POST['username']
		password = request.POST['password']

		print username,password

		user = authenticate(username=username, password=password)
		if user is not None:

			login(request, user)

			print 'INGRESE ACA...'


			a =Agente.objects.get(user_id=request.user.id)
			a.estado_id=1
			a.save()

			return HttpResponseRedirect('/dashboard/')



		else:

			return render(request, 'login.html',{'error': 'No existe este usuario'})


def guardar(request):

	if request.method == 'POST':

		user = request.user.id
		telefono_1= request.POST['telefono_1']
		telefono_2= request.POST['telefono_2']
		cliente= request.POST['cliente']
		apellido_p= request.POST['apellido_p']
		apellido_m= request.POST['apellido_m']
		dni= request.POST['dni']
		marca_vehiculo= request.POST['marca_vehiculo']
		modelo= request.POST['modelo']
		version= request.POST['version']
		#serie= request.POST['serie']
		anio= request.POST['anio']
		#motor= request.POST['motor']
		cilindrada= request.POST['motor']
		color= request.POST['color']
		kilometraje= request.POST['kilometraje']
		placa= request.POST['placa']
		cantidad= request.POST['cantidad']
		marca_producto= request.POST['marca_producto']
		modelo_bateria= request.POST['modelo_b']
		precio= request.POST['precio']
		descuento= request.POST['descuento']
		precio_total= request.POST['precio_total']
		cantidad_bu= request.POST['cantidad_bu']
		fecha_atencion=request.POST['fecha_atencion']
		direccion_atencion= request.POST['direccion_atencion']
		distrito=request.POST['distrito']
		referencia= request.POST['referencia']
		#factura
		ruc =request.POST['ruc']
		razon_social=request.POST['razon_social']
		direccion_rs=request.POST['direccion_rs']
		pago= request.POST['comprobante']
		correo= request.POST['correo']
		atiende= request.POST['atiende']

		print 'atiende',atiende
		try :


			atiende = Atiende.objects.get(celular=atiende).id

		except :
			atiende= request.POST['atiende']

		almacen= request.POST['almacen']		
		#gmail= 'https://www.google.com/maps/search/'+request.POST['direccion_atencion']
		gmail=request.POST['Map']
		status= request.POST['status']
		observaciones= request.POST['observaciones']
		#boleta
		nombre_boleta= request.POST['nombre_boleta']
		m_apellido_p= request.POST['m_apellido_p']
		m_apellido_m= request.POST['m_apellido_m']
		dni_c= request.POST['dni_c']

		


		# direccion1= request.POST['direccion1']


		f=str(fecha_atencion).split('/')
		fecha_atencion = datetime.strptime(fecha_atencion, '%Y-%m-%d')
		ahora = datetime.now()
		h=ahora.hour
		m=ahora.minute
		s=ahora.second
		d1=ahora
		d2 =timedelta(hours=1,minutes=0,seconds=00)
		hora_instalacion=d1+d2
		hh=hora_instalacion.hour
		mm=hora_instalacion.minute
		ss=hora_instalacion.second
		
		
		if mm>30:

			aa=min =round(hora_instalacion.hour)
			prueba=int(aa)
			p=prueba -4
			multi=prueba*100
			rr=str(multi)
			#t = (2009, 2, 17, prueba, 0, 0, 56, 0, 0)
			t = (2009, 1, 1, p, 0, 0, 0, 0, 0)
			t = time.mktime(t)
			hora=time.strftime("%H:%M:%S", time.gmtime(t))
			hora_instalacion=hora

		
		hora_instalacion = request.POST['inputime']

		redis_publisher = RedisPublisher(facility='foobar', users=[request.user.username])

		print 'telefono1',telefono_1

		message = RedisMessage('llamada-'+str(telefono_1))

		redis_publisher.publish_message(message)




		Produccion(hora_instalacion=hora_instalacion,usuario_id=user,modelo_bateria=modelo_bateria,telefono_1=telefono_1,telefono_2=telefono_2,cliente=cliente,apellido_p=apellido_p,apellido_m=apellido_m,dni=dni,marca_vehiculo=marca_vehiculo,modelo=modelo,version=version,anio_id=anio,cilindrada=cilindrada,color_id=color,kilometraje=kilometraje,placa=placa,cantidad=cantidad,marca_producto=marca_producto,precio=precio,descuento=descuento,precio_total=precio_total,cantidad_bu=cantidad_bu,fecha_atencion=fecha_atencion,direccion_atencion=direccion_atencion,distrito_id=distrito,referencia=referencia,pago_id=pago,ruc=ruc,razon_social=razon_social,direccion_rs=direccion_rs,correo=correo,atiende_id=atiende,almacen_id=almacen,gmail=gmail,status_id=status,observaciones=observaciones,nombre_boleta=nombre_boleta,m_apellido_p=m_apellido_p,m_apellido_m=m_apellido_m,dni_c=dni_c).save()

	return render(request, 'colasIN/exito.html',{})

#referencia=referencia,



def dashboard(request):

		

		if request.method=='POST':

			form = BateriasForm(request.POST)
	
			if form.is_valid():

				form.save()

			return HttpResponseRedirect("/dashboard/")


	
	
		marcas= Vehiculo.objects.values('nombre').annotate(Count('nombre')) #.annotate(Count('nombre')) es para agrupar
		bateria= Bateria.objects.values('marca').annotate(Count('marca'))
		anios= Anio_v.objects.all().order_by('-id')
		colores=Colores_v.objects.all()
		distritos= Distrito.objects.all()
		print'heyyy  aquiir estan los distrito,,...',distritos
		pagos= Pago.objects.all()
		almacen=Almacen.objects.all()
		atiende=Atiende.objects.all()
		status=Status.objects.all()

		nombre=''
		marca=''
		modelos=''
		cliente=""
		marca_b=''
		apellido_p=''
		models=''
		
		apellido_m=''

		dni=''
		telefono_1=''

		telefono_2=''
		models_b=''
		distrito=''
		version=''
		
	

		color=''
		precio=''
		modelo_bat=''
		modelo_v=''


		kilometraje=''
		placa=''
		cant_ba=''
		cilindrada= ''
		pre=''
		descuento=''
		#anio=''
		anio=''
		status_uni=''
		motorisado=''
		
		for r in request.GET:

			if r=='marca':

				marca= request.GET['marca']

				modelos = Vehiculo.objects.filter(nombre=marca)
			
			if r=='modelo_v':

				modelo_v=request.GET['modelo_v']


			if r=='marca_b':

				marca_b= request.GET['marca_b']

				models_b = Bateria.objects.filter(marca=marca_b)

				# print'prmodelossssssssss',models_b

				# pre = Bateria.objects.get(modelo=models_b).precio

				# print'preciosssssssssssssssssss',pre
				
			if r=='modelo':

				modelo_bat=request.GET['modelo']
				print 'modelossssssssssssssssssssssss',modelo_bat

				if Bateria.objects.filter(marca=marca_b,modelo=modelo_bat).count()>0:
					print 'modelosddd  ffffffffff',modelo_bat

					precio = Bateria.objects.get(marca=marca_b,modelo=modelo_bat).precio
					descuento = Bateria.objects.get(marca=marca_b,modelo=modelo_bat).descuento
					print'kilok8likili',descuento



			if r=='cliente':

				cliente =request.GET['cliente']

			if r=='apellido_p':

				apellido_p =request.GET['apellido_p']

			if r=='apellido_m':

				apellido_m =request.GET['apellido_m']

			if r=='dni':

				dni =request.GET['dni']

			if r=='telefono_1':

				telefono_1 =request.GET['telefono_1']

			if r=='telefono_2':

				telefono_2 =request.GET['telefono_2']

			if r=='distrito':

				distrito =request.GET['ditrito']

				print 'dissssss',distrito

			if r=='version': #  NOMBRE DE QUE LE DAS LA url q le das

				version =request.GET['version'] # IDENTIFICADOR / NOMBRE DEL TRAEMODELOS
				print 'quue metraes aca.. VERSIOn...',version

		

			if r=='anio': 

				
				anio =request.GET['anio']
				anio = Anio_v.objects.get(id=anio).nombre

				print 'por q no e traes el anioo..gthhhhhhhhhhhhhhhhh.. ANIOO',anio


			if r=='color': 

				color =request.GET['color']
				color = Colores_v.objects.get(id=color).nombre
				print '	que color  ke trares......COLOR..	',color

			if r=='cilindrada': #  NOMBRE DE QUE LE DAS LA url q le das

				cilindrada =request.GET['cilindrada'] # IDENTIFICADOR / NOMBRE DEL traemodelos
				print 'cinlidradasssssss...s...',cilindrada




			if r=='kilometraje': #  NOMBRE DE QUE LE DAS LA url q le das

				kilometraje =request.GET['kilometraje'] # IDENTIFICADOR / NOMBRE DEL TRAEM0ODELOS
				print 'quue metraes aca.. kilometraje...',kilometraje

			if r=='placa': #  NOMBRE DE QUE LE DAS LA url q le das

				placa =request.GET['placa'] # IDENTIFICADOR / NOMBRE DEL TRAEMODELOS
				print 'quue placa essss...',placa

			if r=='cant_ba': #  NOMBRE DE QUE LE DAS LA url q le das

				cant_ba =request.GET['cant_ba'] # IDENTIFICADOR / NOMBRE DEL traemodelos
				print 'cantidadessssssssssssssssss...',cant_ba

			if r=='status_uni': #  NOMBRE DE QUE LE DAS LA url q le das

				#status =request.GET['status'] # IDENTIFICADOR / NOMBRE DEL traemodelos
				#print 'status...',status
				status_uni = Status.objects.get(id=status).nombre
				

			# if r=='anio_v':

			# 	anio_v =request.GET['anio_v']
			# 	print 'noo me jodasssss......',anio_v





		v = VehiculosForm()
		baterias=BateriasForm()

		times = datetime.now()

		t1=times
		t2 =timedelta(hours=1,minutes=0)
		print 'jjjjjjjj',t2

		hora_i=t1+t2
		print ' me traessss la hora???',hora_i
		hhh=hora_i.hour
		mmm=hora_i.minute
		sss=hora_i.second
		
		

		if mmm>30:
		
			aa=min =round(hora_i.hour)
			print 'lo logreeeeee? o aun no?',aa
			prueba=int(aa)
			print 'pruebaaa',prueba
			p=prueba -4
			
			#t = (2009, 2, 17, prueba, 0, 0, 56, 0, 0)
			t = (2009, 1, 1, p, 0, 0, 0, 0, 0)
			t = time.mktime(t)
			horas=time.strftime("%H:%M", time.gmtime(t))
			hora_i=horas
			print 'Hora de hora_instalacion',hora_i

			


		if mmm<30:
			aa=min =round(hora_i.hour)
			print 'lo intente?',aa
			prueba=int(aa)
			print 'pruebita',prueba
			p=prueba -5
			
			#t = (2009, 2, 17, prueba, 0, 0, 56, 0, 0)
			t = (2009, 1, 1, p, mmm, 0, 0, 0, 0)
			t = time.mktime(t)
			horas=time.strftime("%H:%M", time.gmtime(t))
			hora_i=horas
			print 'Hora de hora_instalacion_111',hora_i
			
		

		return render(request, 'colasIN/dashboard.html',{'status_uni':status_uni,'times':times,'hora_i':hora_i,'modelo_v':modelo_v,'colorrecibido':color,'aniorecibido':anio,'descuento':descuento,'precio':precio,'modelo_bat':modelo_bat,'pre':pre,'User':User,'cilindrada':cilindrada,'cant_ba':cant_ba,'placa':placa,'kilometraje':kilometraje,'color':colores,'anio':anios,'version':version,'distrito':distritos,'bateriasform':baterias,'vehiculoform':v,'bateria':bateria,'status':status,'atiende':atiende,'almacen':almacen,'pagos':pagos,'telefono_2':telefono_2,'telefono_1':telefono_1,'dni':dni,'cliente':cliente,'apellido_p':apellido_p,'apellido_m':apellido_m,'modelos':modelos,'marcas':marcas,'marca':marca,'marca_b':marca_b,'modelos_baterias':models_b})


def album(request):

	# u = User.objects.get(id=request.user.id)


	return render(request, 'index.html' )
	
def paciente(request):


	#form = PacientesForm()

	#_pacientes = Pacientes.objects.all()


	#return render(request, 'paciente.html',{'form': form,'pacientes':_pacientes})
	return render(request, 'paciente.html')



def nuevo_caso(request):

	if request.method=='POST':

		instance = Produccion()

		form = IncidenciaForm(request.POST or None, instance=instance)

		if form.is_valid():

			form.save()

			redis_publisher = RedisPublisher(facility='foobar', users=[request.user.username])

			message = RedisMessage('llamada-'+str(telefono))

			redis_publisher.publish_message(message)

		return render(request, 'colasIN/exito.html',{})

	if request.method=='GET':


		casos = Casos.objects.values('caso').annotate(Count('caso'))

		subcaso = Casos.objects.values('subcaso').annotate(Count('subcaso'))

		return render(request, 'colasIN/nuevo_caso.html',{'casos':casos,'subcaso':subcaso})




def nueva_venta(request,id_produccion):

	if request.method=='POST':

		instance = Produccion()

		telefono = request.POST['telefono_1']

 
		form = IncidenciaForm(request.POST or None, instance=instance)

		if form.is_valid():

			form.save()

			redis_publisher = RedisPublisher(facility='foobar', users=[request.user.username])

			message = RedisMessage('llamada-'+str(telefono))

			redis_publisher.publish_message(message)

		return render(request, 'colasIN/exito.html',{})

	if request.method=='GET':

		instance = Produccion.objects.get(id=id_produccion)


		incidenciaform = IncidenciaForm(instance=instance)


		return render(request, 'colasIN/nueva_venta.html',{'incidenciaform':incidenciaform})


def detalle_venta(request,id_produccion):

	if request.method=='POST':

		instance = Produccion()

		telefono = request.POST['telefono_1']

		instance = Produccion.objects.get(id=id_produccion)

		form = IncidenciaForm(request.POST or None, instance=instance)

		if form.is_valid():

				form.save()

		redis_publisher = RedisPublisher(facility='foobar', users=[request.user.username])

		message = RedisMessage('llamada-'+str(telefono))

		redis_publisher.publish_message(message)


		return render(request, 'colasIN/exito.html',{})

	
	if request.method=='GET':

		incidencia = Produccion.objects.get(id=id_produccion)

		incidenciaform = IncidenciaForm(instance=incidencia)

		return render(request, 'colasIN/detalle_venta.html',{'incidenciaform':incidenciaform})


		

				




def lanzallamada(request,base,agente_id):


	if Agente.objects.filter(id=agente_id).count()==0:

		a= simplejson.dumps('No existe el agente con ID '+agente_id)
		return HttpResponse(a, content_type="application/json")


	_agente = Agente.objects.get(id=agente_id)
	_agente.estado_id=2
	_agente.save()

	print 'lanzallamada',_agente.user.username

	redis_publisher = RedisPublisher(facility='foobar', users=[_agente.user.username])

	message = RedisMessage('llamada-'+str(base))

	redis_publisher.publish_message(message)

	a= simplejson.dumps('Se lanzo la llamada')
	return HttpResponse(a, content_type="application/json")

def lanzafinllamada(request,base,agente):

	_agente = Agente.objects.get(id=agente)

	_agente.estado_id=4
	_agente.save()


	redis_publisher = RedisPublisher(facility='foobar', users=[_agente.user.username])

	message = RedisMessage('llamada-'+str(base))


	redis_publisher.publish_message(message)


	_data = Agente.objects.filter(id=agente)
	serializer =  AgentesSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)



def mobile(request):
	"""Return True if the request comes from a mobile device."""
	MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
	if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
		return True
	else:
		return False

def ValuesQuerySetToDict(vqs):

	return [item for item in vqs]

def traesemana(fecha_inicio):

	id =1

	if Semanas.objects.filter(fecha_inicio__lte=fecha_inicio,fecha_fin__gte=fecha_inicio).count()>0:

		id = Semanas.objects.get(fecha_inicio__lte=fecha_inicio,fecha_fin__gte=fecha_inicio).id

	else:

		id=58

	return id







	
	#Actualiza datos
	def put(self, request):

		id =request.user.id
		data = json.loads(request.body)
		telefono = None

		a = Agente.objects.get(user_id=id)

		for i in data:


			data['meta_requerida']=float(str(data['meta_requerida']).replace(',',''))
			data['meta_personal']=float(str(data['meta_personal']).replace(',',''))



			if i=='tipo_agente' :tipo_agente=data['tipo_agente']
			if i=='meta_personal' :a.meta_personal=data['meta_personal']
			if i=='meta_requerida' :a.meta_requerida=data['meta_requerida']
			if i=='correo_capital' :a.correo_capital=data['correo_capital']
			if i=='user__email' :email=data['user__email']
			if i=='photo' :a.photo=data['photo']
			if i=='user__direccion' :a.direccion=data['user__direccion']
			if i=='user__dni' :a.dni=data['user__dni']
			if i=='telefono':a.telefono=data['telefono']
			if i=='telefono_1':a.telefono_1=data['telefono_1']
			if i=='password':
				u = User.objects.get(id=id)
				u.set_password(data['password'])
				u.save()



			if i=='telefono':
				TelefonoUser(user_id=a.user.id,numero=data['telefono']).save()

	
		a.save()



		a= simplejson.dumps('OK')
		return HttpResponse(a, content_type="application/json")

	#Retorna datos del agente
	def get(self, request):



		
		id =request.user.id
		a = Agente.objects.filter(user_id=id).values('user','photo','id','estructura__nombre','user__email','tipo_agente__nombre','meta_personal','meta_requerida','correo_capital','photo','user__first_name','user__last_name','user__dni','user__direccion','equipo__nombre','user__username','pais__nombre','telefono_1','nivel__nombre','telefono')
		fmt = '%d %b %Y'
		for j in range(len(a)):

			if Agente.objects.get(id=a[j]['id']).fecha_ingreso:
				a[j]['fecha_ingreso'] = Agente.objects.get(id=a[j]['id']).fecha_ingreso.strftime(fmt)
			if Agente.objects.get(id=a[j]['id']).user.nacimiento:
				a[j]['fecha_nacimiento'] = Agente.objects.get(id=a[j]['id']).user.nacimiento

			a[j]['meta_requerida']="{:,}".format(a[j]['meta_requerida'])
			a[j]['meta_personal']="{:,}".format(a[j]['meta_personal'])


		a= simplejson.dumps(ValuesQuerySetToDict(a))
		return HttpResponse(a, content_type="application/json")




@login_required(login_url="/ingresar")

def m_agente(request,cliente,id_incidencia):

	print request.user.id

	_agente=Agente.objects.get(user=request.user.id)

	if request.method=='POST':

		instance = Produccion.objects.get(id=id_incidencia)

		form = ProduccionForm(request.POST or None, instance=instance)

		if form.is_valid():

				form.save()

		return HttpResponseRedirect("/colasIN/monitor_agente/"+cliente+"/"+id_incidencia)



	if request.method=='GET':

		

		telefono=cliente

		filter={}

		for r in request.GET:

			if request.GET[r]!='':

				filter[r]=request.GET[r]


			if r=='estado':

				cambia_estado = request.GET['estado']

				_agente.estado_id=cambia_estado

				_agente.save()

		print 'filter',filter

		ven = Produccion.objects.filter(**filter).order_by('-id')

		_estado=EstadoAgente.objects.filter(id__in=[1,2])

		incidenciaform=None

		#agenda = AgendarForm()

		redis_publisher = RedisPublisher(facility='foobar', users=[_agente.user.username])

		message = RedisMessage('hola')

		redis_publisher.publish_message(message)

		agenteform = AgenteForm(instance=_agente)

		incidencia={}

		if int(id_incidencia)>0:

			incidencia = Produccion.objects.get(id=id_incidencia)

			incidenciaform = ProduccionForm(instance=incidencia)

		reportefiltro = IncidenciaForm()

		return render(request, 'colasIN/agente.html',{'reportefiltro':reportefiltro,'telefono':filter,'incidenciaform':incidenciaform,'incidencia':incidencia,'agenteform':agenteform,'agente':_agente,'estados':_estado,'ventas':ven})

