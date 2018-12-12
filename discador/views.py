from django.shortcuts import render
from discador.models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import simplejson
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth import login

from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from discador.serializers import *

from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
from django.db.models.signals import pre_save
from django.dispatch import receiver
from discador.admin import *




@csrf_exempt
def api_gestion(request):

	if request.method == 'POST':

		nombre = json.loads(request.body)['nombre']

		Gestion(nombre=nombre).save()

		a= simplejson.dumps('OK')
		
		return HttpResponse(a, content_type="application/json")

	if request.method == 'GET':

		_data = Gestion.objects.all()

		serializer =  GestionSerializer(_data,many=True)
		return JsonResponse(serializer.data, safe=False)

def importador(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'importador.html',{})

def marcador(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'marcador.html',{})

def usuarios(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'usuarios.html',{})

def api_proveedor(request,id):

	_data = Proveedor.objects.get(id=id)

	serializer =  ProveedorSerializer(_data,many=False)
	return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_agentes(request):

	_data = Agente.objects.all()

	serializer =  AgenteSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def api_carteras(request):

	
	if request.method == 'POST':

		nombre = json.loads(request.body)['nombre']

		Cartera(nombre=nombre).save()

		a= simplejson.dumps('OK')
		
		return HttpResponse(a, content_type="application/json")

	if request.method == 'GET':


		_datos = Cartera.objects.all()

		
		serializer =  CarteraSerializer(_datos,many=True)
		return JsonResponse(serializer.data, safe=False)

def api_cuadrante(request):

	_data = Cuadrante.objects.all()

	serializer =  CuadranteSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)


def api_plano(request):

	_data = Plano.objects.all()

	serializer =  PlanoSerializer(_data,many=True)
	
	return JsonResponse(serializer.data, safe=False)


def api_resultados_gestion(request,id):

	_data = Score.objects.filter(gestion_id=id)

	_ges = []

	for d in _data:

		_ges.append(d.resultado.id)

	_data = Resultado.objects.filter(id__in=_ges)

	serializer =  ResultadoSerializer(_data,many=True)

	return JsonResponse(serializer.data, safe=False)



def api_producto(request):

	_data = Producto.objects.all()

	serializer =  ProductoSerializer(_data,many=True)

	return JsonResponse(serializer.data, safe=False)

def proveedor(request):



	print 'traes la daata?', _data
	serializer =  AgenteSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def menu_proveedor_1(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'proveedor.html',{})


@csrf_exempt
def prueba(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'prueba.html',{})


@csrf_exempt
def carteras(request,id_proveedor):


	return render(request, 'cartera.html',{})



@csrf_exempt
def menu_proveedor(request):


	discador = Proveedor.objects.all()

	try:
	
		id=request.GET['proveedor']

		print 'Proveedor....'+id

		x=Score.objects.filter(proveedor_id=id)

		print x

		id=request.GET['cartera']

		if id!=0:

			r=Score.objects.filter(cartera_id=id)


		return render(request, 'proveedor.html',{'discador': discador,'carteras':x,'resultado':r})

	except:


		return render(request, 'proveedor.html',{'discador': discador})

	

	

	# print 'traes la daata?', _data
	# serializer =  AgenteSerializer(_data,many=True)
	# return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_proveedores(request):

	if request.method == 'POST':

		nombre = json.loads(request.body)['nombre']

		Proveedor(nombre=nombre).save()

		a= simplejson.dumps('OK')
		
		return HttpResponse(a, content_type="application/json")

	if request.method == 'GET':


		_datos = Proveedor.objects.all()

		print 'traes la daata?', api_proveedor
		serializer =  ProveedorSerializer(_datos,many=True)
		return JsonResponse(serializer.data, safe=False)

# Create your views here.
@csrf_exempt
def api_estadocliente(request):

	print 'engtrree'

	_datos = Estado_cliente.objects.all()

	print 'traes la daata?', _datos
	serializer =  Estado_clienteSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def api_tipo_contacto(request):

	print 'engtrree'

	_datos = Tipo_contacto.objects.all()

	print 'traes la daata?', _datos
	serializer =  Tipo_contactoSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_score(request):

	_datos = Score.objects.all()

	serializer =  ScoreSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_cartera(request,id_proveedor):


	if request.method == 'POST':

		nombre = json.loads(request.body)['nombre']

		Cartera(nombre=nombre).save()

		a= simplejson.dumps('OK')
		
		return HttpResponse(a, content_type="application/json")

	if request.method == 'GET':



		_datos = Cartera.objects.filter(proveedor_id=id_proveedor)

		print ('traes la daata?', _datos)
		serializer =  CarteraSerializer(_datos,many=True)
		return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_resultados(request):

	_datos = Resultado.objects.all()
	serializer =  ResultadoSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def api_subresultados(request):

	_datos = Sub_categoria.objects.all()
	serializer =  Sub_categoriaSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def api_tipodomicilio(request):

	print 'engtrree'

	_datos = Tipo_domicilio.objects.all()

	print 'traes la daata?', _datos
	serializer =  Tipo_domicilioSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_detalle_cartera(request,id):

	if request.method == 'POST':

		nombre = json.loads(request.body)['nombre']

		Cartera(nombre=nombre).save()

		a= simplejson.dumps('OK')
		
		return HttpResponse(a, content_type="application/json")

	if request.method == 'GET':


		_datos = Cartera.objects.get(id=id)

		print 'traes la daata?', 
		serializer =  ProveedorSerializer(_datos,many=False)
		return JsonResponse(serializer.data, safe=False)



