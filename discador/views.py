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
def subecuentas(request):

	df = pd.read_csv('/home/jose/Descargas/cuentas.csv')
	Cuentas.objects.all().delete()

	for i in range(df.shape[0]):


		# print df['idcliente'][i]

		# gestion_id=Gestion.objects.get(nombre=df['idcliente'][i]).id
		# print df['IDGESTION'][i]
		# id_gestion_id=IDGestion.objects.get(nombre=df['IDGESTION'][i]).id

		# print df['RESULTADO'][i]
		# resultado_id=Resultado.objects.get(nombre=df['RESULTADO'][i]).id
		# print df['JUSTIFICACION'][i]
		# subresultado_id=Subresultado.objects.get(nombre=df['JUSTIFICACION'][i]).id

		idcliente = df['idcliente'][i]
		
		moneda = df['moneda'][i]
		producto = df['producto'][i]

		print df['tipo_cartera'][i]
		cartera_id=Cartera.objects.get(nombre=df['tipo_cartera'][i]).id

		tipo_credito = df['tipo_credito'][i]
		tipo_clasificacion = df['tipo_clasificacion'][i]
		estado = df['id_estado'][i]
		fecha_vencimiento = df['fecha_vencimiento'][i]
		fecha_concecion = df['fecha_concecion'][i]
		nuemero_cuotas=df['nro_cuotas'][i]  
		dias_mora= df['dias_mora'][i]  
		tramo= df['tramo'][i]  
		rango_dias= df['rango_dias'][i]  
		segmento= df['segmento'][i]  
		grupo= df['grupo'][i]  
		ciclo= df['ciclo'][i]  
		imp_capital= df ['imp_capital'][i]  
		imp_interes= df['imp_interes'][i]  
		imp_mora= df['imp_mora'][i]  
		imp_otros= df['imp_otros'][i]  
		imp_total= df['imp_total'][i]  
		imp_vencido= df ['imp_vencido'][i]  
		imp_minimo= df['imp_minimo'][i]  
		imp_descuento= df['imp_descuento'][i]  
		imp_campania= df['imp_campania'][i]  
		imp_cap_original= df['imp_cap_original'][i]  
		imp_prox_pago= df['imp_prox_pago'][i]  
		fecha_prox_pago= df ['fecha_prox_pago'][i]  
		observacion01= df['observacion01'][i]  
		observacion02= df ['observacion02'][i]  
		observacion03=df ['observacion03'][i]  
		nro_tarjeta= df['nro_tarjeta'][i]  
		id_gestor= df['id_gestor'][i]
		fecha_deuda = df['fecha_deuda'][i]


		print('daniellllllll',estado)

		print('?????????????????',cartera_id )
		print('?????????????????',idcliente )

		Cuentas(idcliente=idcliente,moneda=moneda,producto=producto,cartera_id=cartera_id,tipo_credito=tipo_credito,
		tipo_clasificacion=tipo_clasificacion,estado=estado,fecha_vencimiento=fecha_vencimiento,
		fecha_concecion=fecha_concecion,nuemero_cuotas=nuemero_cuotas,dias_mora=dias_mora,tramo=tramo, 
		rango_dias=rango_dias,segmento =segmento,grupo=grupo,ciclo=ciclo,imp_capital=imp_capital, 
		imp_interes =imp_interes,imp_mora = imp_mora,imp_otros=imp_otros,imp_total=imp_total, 
		imp_vencido = imp_vencido, imp_minimo=imp_minimo , imp_descuento =imp_descuento,
		imp_campania=imp_campania, imp_cap_original = imp_cap_original,imp_prox_pago=imp_prox_pago,
		fecha_prox_pago= fecha_prox_pago,observacion01  =observacion01  , observacion02= observacion02,
		observacion03 = observacion03,nro_tarjeta= nro_tarjeta, id_gestor=id_gestor,fecha_deuda=fecha_deuda ).save()

	return render(request, 'agentes.html',{})




@csrf_exempt
def api_proveedor_cartera_negocio(request):

	_data = ProveedorCarteras.objects.all().order_by('-id')

	serializer =  ProveedorCarterasSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def api_detalle_proveedor_cartera_negocio(request,proveedor,cartera,negocio):

	_data = ScoreProveedor.objects.filter(proveedor_id=proveedor,cartera_id=cartera,negocio_id=negocio)

	serializer =  ScoreProveedorSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

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
def opcion_score(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'opcion_score.html',{})

@csrf_exempt
def subescores(request):

	df = pd.read_csv('/home/jose/Descargas/Libro1.csv')
	Score.objects.all().delete()

	for i in range(df.shape[0]):


		print df['TIPO GESTION'][i]

		gestion_id=Gestion.objects.get(nombre=df['TIPO GESTION'][i]).id
		print df['IDGESTION'][i]
		id_gestion_id=IDGestion.objects.get(nombre=df['IDGESTION'][i]).id

		print df['RESULTADO'][i]
		resultado_id=Resultado.objects.get(nombre=df['RESULTADO'][i]).id
		print df['JUSTIFICACION'][i]
		subresultado_id=Subresultado.objects.get(nombre=df['JUSTIFICACION'][i]).id

		peso_subresultado = df['PESO JUSTIFICACION'][i]
		peso_tipo_gestion = df['PESO TIPO GESTION'][i]
		peso_id_gestion = df['PESO IDGESTION'][i]
		peso_resultado = df['PESO RESULTADO'][i]
		print('?????????????????',id_gestion_id)

		Score(negocio_id=1,gestion_id=gestion_id,id_gestion_id=id_gestion_id,resultado_id=resultado_id,subresultado_id=subresultado_id,peso_resultado=peso_resultado,peso_tipo_gestion=peso_tipo_gestion,peso_id_gestion=peso_id_gestion,peso_subresultado=peso_subresultado).save()

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

def api_detalle_cartera_negocio(request,proveedor,cartera,negocio):

	_data = ScoreProveedor.objects.filter(proveedor_id=proveedor,cartera_id=cartera,negocio_id=negocio)

	serializer =  ScoreProveedorSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)



@csrf_exempt
def menu_proveedor_1(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'proveedor.html',{})

@csrf_exempt
def opcion_asigna_score(request,proveedor,cartera,negocio):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'opcion_asigna_score.html',{})

@csrf_exempt
def guardaproveedor(request):

	if request.method == 'POST':

		data = json.loads(request.body)

		print data['proveedor_id']

		ProveedorCarteras(**data).save()

		sc = Score.objects.filter(negocio_id=data['negocio_id'])

		for s in sc:

			ScoreProveedor(
			cartera_id=data['cartera_id']
			,proveedor_id=data['proveedor_id']
			,negocio_id=data['negocio_id']
			,gestion_id=s.gestion.id
			,peso_tipo_gestion=s.peso_tipo_gestion
			,id_gestion_id=s.id_gestion.id
			,peso_id_gestion=s.peso_id_gestion
			,resultado_id=s.resultado.id
			,peso_resultado=s.peso_resultado
			,subresultado_id=s.subresultado.id
			,peso_subresultado=s.peso_subresultado
			,estado=1).save()


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





