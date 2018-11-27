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

def proveedor(request):



	print 'traes la daata?', _data
	serializer =  AgenteSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)


def menu_proveedor_1(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'menu_proveedor.html',{})





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



def api_proveedor(request):

	print 'engtrree'

	_datos = Proveedor.objects.all()

	print 'traes la daata?', api_proveedor
	serializer =  ProveedorSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)

# Create your views here.

def api_estadocliente(request):

	print 'engtrree'

	_datos = Estado_cliente.objects.all()

	print 'traes la daata?', _datos
	serializer =  Estado_clienteSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)


def api_tipo_contacto(request):

	print 'engtrree'

	_datos = Tipo_contacto.objects.all()

	print 'traes la daata?', _datos
	serializer =  Tipo_contactoSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)



def api_score(request):

	print 'engtrree'

	_datos = Score.objects.all()

	print 'traes la daata?', _datos
	serializer =  ScoreSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)



def api_cartera(request,id_proveedor):



	_datos = Score.objects.filter(proveedor_id=id_proveedor)


	serializer =  ScoreSerializer(_datos,many=True)
	
	
	return JsonResponse(serializer.data, safe=False)



def api_tipodomicilio(request):

	print 'engtrree'

	_datos = Tipo_domicilio.objects.all()

	print 'traes la daata?', _datos
	serializer =  Tipo_domicilioSerializer(_datos,many=True)
	return JsonResponse(serializer.data, safe=False)


