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
def api_telefonos(request):

	_data = Telefonos.objects.all()

	serializer =  TelefonosSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_detalle_cuentas(request,id):

	if request.method == 'POST':

		nombre = json.loads(request.body)['nombre']

		Cuentas(nombre=nombre).save()

		a= simplejson.dumps('OK')
		
		return HttpResponse(a, content_type="application/json")

	if request.method == 'GET':


		_datos = Cuentas.objects.filter(id=id)

		print 'traes la daata?', 
		serializer =  CuentasSerializer(_datos,many=True)
		return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def agentes(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'agentes.html',{})



@csrf_exempt
def subescores(request):

	df = pd.read_csv('/Users/xiencias/score.csv')

	for i in range(df.shape[0]):


		print df['TIPO GESTION'][i]

		gestion_id=Gestion.objects.get(nombre=df['TIPO GESTION'][i]).id
		print df['IDGESTION'][i]
		idgestion_id=Resultado.objects.get(nombre=df['IDGESTION'][i]).id

		print df['RESULTADO'][i]
		resultado_id=Resultado.objects.get(nombre=df['RESULTADO'][i]).id
		print df['JUSTIFICACION'][i]
		subresultado_id=Resultado.objects.get(nombre=df['JUSTIFICACION'][i]).id

		peso_subresultado = df['PESO JUSTIFICACION'][i]
		peso_tipo_gestion = df['PESO TIPO GESTION'][i]
		peso_idgestion = df['PESO IDGESTION'][i]
		peso_resultado = df['PESO RESULTADO'][i]

		Score(negocio_id=1,gestion_id=gestion_id,idgestion_id=idgestion_id,resultado_id=resultado_id,subresultado_id=subresultado_id,peso_resultado=peso_resultado,peso_tipo_gestion=peso_tipo_gestion,peso_id_gestion=peso_id_gestion,peso_subresultado=peso_subresultado).save()

	return render(request, 'agentes.html',{})


@csrf_exempt
def api_resultados_negocio(request,id_negocio):

	_data = Score.objects.filter(negocio_id=id_negocio)

	serializer =  ScoreSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_obtiene_estado_score(request,proveedor_id,cartera_id,negocio_id):

	_data = Score.objects.filter(negocio_id=negocio_id,proveedor_id=proveedor_id,cartera_id=cartera_id)

	if _data.count()>0:

		serializer =  ScoreSerializer(_data,many=True)
		return JsonResponse(serializer.data, safe=False)
	




@csrf_exempt
def api_cuentas(request):

	if request.method == 'POST':

		nombre = json.loads(request.body)['nombre']

		Cuentas(nombre=nombre).save()

		a= simplejson.dumps('OK')
		
		return HttpResponse(a, content_type="application/json")

	if request.method == 'GET':

		_data = Cuentas.objects.all()

		serializer =  CuentasSerializer(_data,many=True)
		return JsonResponse(serializer.data, safe=False)



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

def api_negocios(request):

	_data = Negocio.objects.all()

	serializer =  NegocioSerializer(_data,many=True)

	return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def api_asigna_score(request):

	if request.method == 'POST':

		data = json.loads(request.body)

		score_id = data['item']['id']

		sco = Score.objects.get(id=score_id)

		pro = data['proveedor']

		print 'Proveedor....',pro

		prove = ProveedorCarteras.objects.filter(**pro)

		if prove.count()==0: 
			
			ProveedorCarteras(**pro).save()

			proveedor_id=ProveedorCarteras.objects.all().order_by('-id')[0].id

		else:

			proveedor_id=prove[0].id

		sco = ScoreProveedor.objects.filter(score_id=score_id,proveedor_id=proveedor_id)

		if sco.count()==0: 
		
			ScoreProveedor(score_id=score_id,proveedor_id=proveedor_id,estado_id=data['estado']).save()
		
		else:

			ScoreProveedor.objects.filter(id=sco[0].id,estado_id=data['estado']).update(score_id=score_id,proveedor_id=proveedor_id)


	_data = Negocio.objects.all()

	serializer =  NegocioSerializer(_data,many=True)

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
def guardaproveedor(request):

	if request.method == 'POST':

		data = json.loads(request.body)

		ProveedorCarteras(**data).save()


	_data = ProveedorCarteras.objects.all()[:1]

	serializer =  ProveedorCarterasSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)





@csrf_exempt
def opcion_proveedor(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'prueba.html',{})


@csrf_exempt
def carteras(request,id_proveedor):

	pro = Proveedor.objects.get(id=id_proveedor)
	return render(request, 'cartera.html',{'proveedor':pro})

@csrf_exempt
def api_carteras_proveedor(request,id_proveedor):

	_data= ProveedorCarteras.objects.filter(proveedor_id=id_proveedor)

	serializer =  ProveedorCarterasSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def api_id_gestion(request,id_gestion):

	id_ges=[]

	sc = Score.objects.filter(gestion_id=id_gestion)

	print sc.count()

	for s in sc:

		print 'entre...',s.id

		id_ges.append(s.id_gestion.id)

	_data = IDGestion.objects.filter(id__in=id_ges)
	serializer =  IDGestionSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def api_resultados(request,id_gestion):

	id_res=[]

	sc = Score.objects.filter(id_gestion_id=id_gestion)

	print sc.count()

	for s in sc:

		print 'entre...',s.id

		id_res.append(s.resultado.id)

	_data = Resultado.objects.filter(id__in=id_res)
	serializer =  ResultadoSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)


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
def api_subresultados(request,id_resultado):

	id_subres=[]

	sc = Score.objects.filter(resultado_id=id_resultado)

	print sc.count()

	for s in sc:

		print 'entre...',s.id

		id_subres.append(s.subresultado.id)

	_data = Subresultado.objects.filter(id__in=id_subres)
	serializer =  SubresultadoSerializer(_data,many=True)
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





