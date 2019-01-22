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
from django.db.models import Count
from discador.forms import *

@csrf_exempt
def subetelefonos(request):

	df = pd.read_csv('/home/jose/Descargas/Telefonos.csv')
	Telefonos.objects.all().delete()
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

		print df['NUMERO_DOCUMENTO'][i]
		numero_documento_id=Cliente.objects.get(numero_documento=df['NUMERO_DOCUMENTO'][i]).id
		print df['DISCADO'][i]
		discado = df['DISCADO'][i]

		cliente = df['NOMBRE'][i]
		
		print df['NUMERO DE TELEFONO'][i]
		numero_telefono= df['NUMERO DE TELEFONO'][i]
		observacion = df['OBSERVACION'][i]
		tipo_contacto= df['TIPO CONTACTO'][i]
		tipo_telefono = df['TIPO TELEFONO'][i]
		fuente_telefono= df['FUENTE'][i]
		estado = df['ESTADO'][i]


		Telefonos(numero_documento_id=numero_documento_id,numero_telefono=numero_telefono,discado=discado,
		cliente=cliente,observacion=observacion,tipo_contacto=tipo_contacto,
		tipo_telefono=tipo_telefono,fuente_telefono=fuente_telefono,estado=estado
		).save()


	return render(request, 'agentes.html',{})





@csrf_exempt
def subeclientes(request):

	df = pd.read_csv('/home/jose/Descargas/Clientes.csv')
	Cliente.objects.all().delete()

	for i in range(df.shape[0]):


		# print df['TIPO GESTION'][i]

		# gestion_id=Gestion.objects.get(nombre=df['TIPO GESTION'][i]).id
		# print df['IDGESTION'][i]
		# id_gestion_id=IDGestion.objects.get(nombre=df['IDGESTION'][i]).id

		# print df['RESULTADO'][i]
		# resultado_id=Resultado.objects.get(nombre=df['RESULTADO'][i]).id
		# print df['JUSTIFICACION'][i]
		# subresultado_id=Subresultado.objects.get(nombre=df['JUSTIFICACION'][i]).id

		tipo_persona = df['TIPO_PERSONA'][i]
		tipo_documento = df['TIPO_DOCUMENTO'][i]
		numero_documento= df['NUMERO_DOCUMENTO'][i]
		nombres = df['NOMBRE'][i]
		observacion = df['OBSERVACIONES'][i]
		fecha = df['FECHA_NACIMIENTO'][i]
		estado = df['ESTADO'][i]

		Cliente(tipo_persona=tipo_persona,tipo_documento=tipo_documento,numero_documento=numero_documento,
		nombres=nombres,observacion=observacion,fecha=fecha,estado=estado).save()

	return render(request, 'agentes.html',{})


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
def api_agentes(request):

	_data = Agente.objects.all()

	serializer =  AgenteSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

	
@csrf_exempt
def agentes(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'agentes.html',{})

@csrf_exempt
def traeagentes(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'traeagentes.html',{})




@csrf_exempt
def opcion_score(request):

	#_data = Proveedor.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)


	return render(request, 'opcion_score.html',{})




@csrf_exempt
def borrar(request):

	Subresultado.objects.all().delete()

	return render(request, 'importador.html',{})

@csrf_exempt
def subescores(request):

	xls = pd.ExcelFile('/home/jose/Descargas/Libro1.xlsx') 
	
	df = pd.read_excel(xls, 'MARKETING') 

	Score.objects.filter(negocio_id=2).delete()

	for i in range(df.shape[0]):

		subresultado=df['TIPO GESTION'][i]

		gestion_id=Gestion.objects.get(nombre=df['TIPO GESTION'][i]).id
		
		id_gestion_id=IDGestion.objects.get(nombre=df['IDGESTION'][i]).id

		print 'resultado',df['RESULTADO'][i]
		resultado_id=Resultado.objects.get(nombre=df['RESULTADO'][i]).id
		print 'jsutificacion',df['JUSTIFICACION'][i]
		nombre=df['JUSTIFICACION'][i]

		
		subresultado_id=Subresultado.objects.get(nombre=df['JUSTIFICACION'][i]).id

		peso_subresultado = df['PESO JUSTIFICACION'][i]
		peso_tipo_gestion = df['PESO TIPO GESTION'][i]
		peso_id_gestion = df['PESO IDGESTION'][i]
		peso_resultado = df['PESO RESULTADO'][i]


		Score(negocio_id=2,gestion_id=gestion_id,id_gestion_id=id_gestion_id,resultado_id=resultado_id,subresultado_id=subresultado_id,peso_resultado=peso_resultado,peso_tipo_gestion=peso_tipo_gestion,peso_id_gestion=peso_id_gestion,peso_subresultado=peso_subresultado).save()

	
	df = pd.read_excel(xls, 'ATENCION_CLIENTE') 

	Score.objects.filter(negocio_id=1).delete()

	for i in range(df.shape[0]):
		print 'gestion',df['TIPO GESTION'][i]

		gestion_id=Gestion.objects.get(nombre=df['TIPO GESTION'][i]).id
		print 'id-gestion', df['IDGESTION'][i]
		id_gestion_id=IDGestion.objects.get(nombre=df['IDGESTION'][i]).id

		print 'resultado',df['RESULTADO'][i]
		resultado_id=Resultado.objects.get(nombre=df['RESULTADO'][i]).id
		print 'justificacion1',df['JUSTIFICACION'][i]
		nombre=df['JUSTIFICACION'][i]


		# try :
		# 	Subresultado(nombre=nombre).save()
		# except:

		subresultado_id=Subresultado.objects.get(nombre=df['JUSTIFICACION'][i]).id
		

		print 'PESO-justificacion0n',df['JUSTIFICACION'][i]
		peso_subresultado = df['PESO JUSTIFICACION'][i]


		print 'PESO-TIPO-justificacion0n',df['PESO TIPO GESTION'][i]
		peso_tipo_gestion = df['PESO TIPO GESTION'][i]

		print 'PESO-ID-GESTION',df['PESO IDGESTION'][i]
		peso_id_gestion = df['PESO IDGESTION'][i]

		print 'PESO-RESULTADO',df['PESO RESULTADO'][i]
		peso_resultado = df['PESO RESULTADO'][i]
		print('?????????????????',id_gestion_id)

		Score(negocio_id=1,gestion_id=gestion_id,id_gestion_id=id_gestion_id,resultado_id=resultado_id,subresultado_id=subresultado_id,peso_resultado=peso_resultado,peso_tipo_gestion=peso_tipo_gestion,peso_id_gestion=peso_id_gestion,peso_subresultado=peso_subresultado).save()

	df = pd.read_excel(xls, 'COBRANZA') 

	Score.objects.filter(negocio_id=3).delete()

	for i in range(df.shape[0]):
	
		print('tipo-gestion')
		print 'PESO-Tipo-gestion', df['TIPO GESTION'][i]
		gestion_id=Gestion.objects.get(nombre=df['TIPO GESTION'][i]).id
		
		print 'id-gestion', df['IDGESTION'][i]
		id_gestion_id=IDGestion.objects.get(nombre=df['IDGESTION'][i]).id
		
		print 'Resultadoo',df['RESULTADO'][i]
		resultado_id=Resultado.objects.get(nombre=df['RESULTADO'][i]).id

		
		print 'Justificacionn',df['JUSTIFICACION'][i]
		
		subresultado_id=Subresultado.objects.get(nombre=df['JUSTIFICACION'][i]).id

		
		peso_subresultado = df['PESO JUSTIFICACION'][i]
		
		peso_tipo_gestion = df['PESO TIPO GESTION'][i]
		
		peso_id_gestion = df['PESO IDGESTION'][i]

		print('')
		peso_resultado = df['PESO RESULTADO'][i]
		print('?????????????????',id_gestion_id)

		Score(negocio_id=3,gestion_id=gestion_id,id_gestion_id=id_gestion_id,resultado_id=resultado_id,subresultado_id=subresultado_id,peso_resultado=peso_resultado,peso_tipo_gestion=peso_tipo_gestion,peso_id_gestion=peso_id_gestion,peso_subresultado=peso_subresultado).save()




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

	x = request.GET

	print x

	sc=ScoreProveedor.objects.filter(proveedor_id=proveedor,cartera_id=cartera,negocio_id=negocio)


	for r in x:

		if r=='scoreproveedor':

			scoreproveedor = x['scoreproveedor']

		if r=='activar':

			estado = x['activar']

		if r=='gestion':

			gestion= x['gestion']

			sc=ScoreProveedor.objects.filter(proveedor_id=proveedor,cartera_id=cartera,negocio_id=negocio,gestion_id=gestion)


	try:

		sc=ScoreProveedor.objects.get(id=scoreproveedor)
		sc.estado=x['activar']
		sc.save()

	except:

		print 'Error'



	proveedor=Proveedor.objects.get(id=proveedor)
	cartera=Cartera.objects.get(id=cartera)
	negocio=Negocio.objects.get(id=negocio)

	_gestion = Score.objects.all().values('gestion_id','gestion__nombre').annotate(Count('gestion'))

	print _gestion


	
	return render(request, 'opcion_asigna_score.html',{'gestion':_gestion,'scoreproveedor':sc,'proveedor':proveedor,'cartera':cartera,'negocio':negocio})

@csrf_exempt
def guardaproveedor(request):

	if request.method == 'POST':

		data = json.loads(request.body)

		print 'Guardando Score...',data

		ProveedorCarteras(**data).save()

		print data['negocio_id']

		sc = Score.objects.filter(negocio_id=data['negocio_id'])

		print 'Socre Negocios...',sc

		for s in sc:


			print data['proveedor_id']

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
def opcion_clientes(request):

	_data = Cliente.objects.all()

	nuevocliente =  ClientesForm()

	if request.POST:

		form = ClientesForm(request.POST)
	
		if form.is_valid():

			form.save()

	if request.GET:

		filtro = {}

		for r in request.GET:

			if r=='nombres' and request.GET['nombres']!= '':
				filtro['nombres'] = request.GET['nombres']
			if r=='dni' and request.GET['dni']!= '' :
				filtro['dni'] = request.GET['dni']
			if r=='telefono' and request.GET['telefono']!= '':
				filtro['telefono'] = request.GET['telefono']
			if r=='numero_documento' and request.GET['numero_documento']!= '':
				filtro['numero_documento'] = request.GET['numero_documento']

		print filtro

		_data=Cliente.objects.filter(**filtro)

		
		return render(request, 'opcion_clientes.html',{'clientes':_data,'nuevocliente':nuevocliente})

	return render(request, 'opcion_clientes.html',{'clientes':_data,'nuevocliente':nuevocliente})


@csrf_exempt
def editar_cliente(request,cliente_id):
	
	if request.method == 'POST':

		cliente_id = Cliente.objects.get(id=cliente_id)

		form = ClientesForm(request.POST,instance=cliente_id)
	
		if form.is_valid():

			form.save()

		return render(request, 'discador.exito.html',{})


	if request.method == 'GET':



		cli = Cliente.objects.get(id=cliente_id)

		editarcliente = ClientesForm(instance=cli)

		return render(request, 'discador.editar_cliente.html',{'editarcliente':editarcliente})

@csrf_exempt
def provedor_carteras(request):

	_data = ProveedorCarteras.objects.all()
	nv_provedor_cartera =  ProveedorCarteraForm()
	if request.POST:
		form = ProveedorCarteraForm(request.POST)	
		if form.is_valid():
			form.save()
		return render(request, 'discador.exito.html',{})
	
	

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'provedor_cartera.html',{'provedor_cartera':_data,'nv_provedor_cartera':nv_provedor_cartera})




@csrf_exempt
def opcion_provedor(request):

	_data = Proveedor.objects.all()
	nuevoprovedor =  ProveedorForm()
	if request.POST:
		form = ProveedorForm(request.POST)	
		if form.is_valid():
			form.save()
	
	if request.GET:
		filtro = {}
		for r in request.GET:
			if r=='nombre' and request.GET['nombre']!= '':
				filtro['nombre'] = request.GET['nombre']
			
		print 'me-funcion este filtro',filtro
		_data=Proveedor.objects.filter(**filtro)

		
		return render(request, 'opcion_provedor.html',{'provedor':_data,'nuevoprovedor':nuevoprovedor})

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'opcion_provedor.html',{'provedor':_data,'nuevoprovedor':nuevoprovedor})

@csrf_exempt
def editar_provedor(request,provedor_id):
	
	if request.method == 'POST':
		provedor_id = Proveedor.objects.get(id=provedor_id)
		form = ProveedorForm(request.POST,instance=provedor_id)
		if form.is_valid():
			form.save()
		return render(request, 'discador.exito.html',{})
	if request.method == 'GET':
		pro = Proveedor.objects.get(id=provedor_id)
		editarprovedor = ProveedorForm(instance=pro)
		return render(request, 'discador.editar_provedor.html',{'editarprovedor':editarprovedor})
	


@csrf_exempt
def opcion_usuarios(request):

	_data = Agente.objects.all()

	nuevoagente =  AgenteForm()
	if request.POST:
		form = AgenteForm(request.POST)	
		if form.is_valid():
			form.save()
	
	if request.GET:
		filtro = {}
		for r in request.GET:
			if r=='nombre' and request.GET['nombre']!= '':
				filtro['nombre'] = request.GET['nombre']
			
		print 'me-funcion este filtro',filtro
		_data=Agente.objects.filter(**filtro)

		
		return render(request, 'opcion_usuarios.html',{'agentes':_data,'nuevoagente':nuevoagente})

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)

	return render(request, 'opcion_usuarios.html',{'agentes':_data,'nuevoagente':nuevoagente})


@csrf_exempt
def editar_usuarios(request,usuario_id):
	
	if request.method == 'POST':
		usuario_id = Agente.objects.get(id=usuario_id)
		form = AgenteForm(request.POST,instance=usuario_id)
		if form.is_valid():
			form.save()
		return render(request, 'discador.exito.html',{})
	if request.method == 'GET':
		age = Agente.objects.get(id=usuario_id)
		print '???? que usuarios trae....xd',age
		editarusuarios = AgenteForm(instance=age)
		return render(request, 'discador.editar_usuarios.html',{'editarusuarios':editarusuarios})

@csrf_exempt

@csrf_exempt
def opcion_cuenta(request):

	_data = Cuentas.objects.all()

	nuevocliente =  ClientesForm()

	if request.POST:

		form = ClientesForm(request.POST)
	
		if form.is_valid():

			form.save()

	if request.GET:

		filtro = {}

		for r in request.GET:

			if r=='nombres' and request.GET['nombres']!= '':
				filtro['nombres'] = request.GET['nombres']
			if r=='dni' and request.GET['dni']!= '' :
				filtro['dni'] = request.GET['dni']
			if r=='telefono' and request.GET['telefono']!= '':
				filtro['telefono'] = request.GET['telefono']
			if r=='numero_documento' and request.GET['numero_documento']!= '':
				filtro['numero_documento'] = request.GET['numero_documento']

		print filtro

		_data=Cliente.objects.filter(**filtro)

		
		return render(request, 'opcion_cuenta.html',{'cuenta':_data,'nuevocliente':nuevocliente})

	return render(request, 'opcion_cuenta.html',{'cuenta':_data,'nuevocliente':nuevocliente})



def proseso_masivo(request):

	_data = Cuentas.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)


	return render(request, 'proseso_masivo.html',{'cuentas':_data})


@csrf_exempt

def gestion_telefonia(request):

	_data = Telefonos.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)
	

	return render(request, 'gestion_telefonia.html',{'telefonos':_data})


@csrf_exempt

def gestion_campo(request):

	_data = Telefonos.objects.all()

	#serializer =  ScoreSerializer(_data,many=True)
	#return JsonResponse(serializer.data, safe=False)
	

	return render(request, 'gestion_campo.html',{'telefonos':_data})

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
def api_carteras_negocios(request,id_proveedor,id_cartera):

	_data= ProveedorCarteras.objects.filter(proveedor_id=id_proveedor,cartera_id=id_cartera)

	serializer =  ProveedorCarterasSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)

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
def api_resultados(request):



	_data = Resultado.objects.all()
	serializer =  ResultadoSerializer(_data,many=True)
	return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def api_busca_score(request):

	data =  json.loads(request.body)['data']

	print data

	my_filter = {}

	for r in data:

		if r=='resultado' and data['resultado']!= False:
			
			my_filter['resultado_id'] = data['resultado']['id']

		if r=='cartera':

			my_filter['cartera_id']  = data['cartera']['cartera']['id']
		
		if r=='proveedor':

			my_filter['proveedor_id'] = data['proveedor']['id']

		if r=='negocio':

			my_filter['negocio_id'] = data['negocio']['negocio']['id']

		if r=='gestion':

			my_filter['gestion_id'] = data['gestion']['id']


	_score = ScoreProveedor.objects.filter(**my_filter)

	serializer =  ScoreProveedorSerializer(_score,many=True)
	return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def proveedor_score(request):


	discador = Proveedor.objects.all()

	try:
	
		id=request.GET['proveedor']

		print 'Proveedor....'+id

		x=Score.objects.filter(proveedor_id=id)

		print x

		id=request.GET['cartera']

		if id!=0:

			r=Score.objects.filter(cartera_id=id)


		return render(request, 'proveedor_score.html',{'discador': discador,'carteras':x,'resultado':r})

	except:


		return render(request, 'proveedor_score.html',{'discador': discador})

	

	

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





