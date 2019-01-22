from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Distrito(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)
	ubigeo=models.CharField(max_length=100,blank=True,null=True)
class Provincia(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)
	ubigeo=models.CharField(max_length=100,blank=True,null=True)

class Departamento(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)
	ubigeo=models.CharField(max_length=100,blank=True,null=True)


class Negocio(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.nombre


class Industria(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.nombre


class Proveedor(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)
	industria=models.ForeignKey(Industria,max_length=100,blank=True,null=True)
	direccion=models.CharField(max_length=100,blank=True,null=True)
	telefono=models.CharField(max_length=100,blank=True,null=True)
	email=models.CharField(max_length=100,blank=True,null=True)
	contacto=models.CharField(max_length=100,blank=True,null=True)
	obserbaciones=models.CharField(max_length=100,blank=True,null=True)
	estado=models.CharField(max_length=100,blank=True,null=True)

	nombre_documento=models.CharField(max_length=100,blank=True,null=True)
	tipo_personal=models.CharField(max_length=100,blank=True,null=True)
	tipo_documento=models.CharField(max_length=100,blank=True,null=True)
	industria=models.ForeignKey(Industria,max_length=100,blank=True,null=True)
	departamento= models.ForeignKey(Departamento, blank=True, null=True)
	provincia= models.ForeignKey(Provincia, blank=True, null=True)
	distrito= models.ForeignKey(Distrito, blank=True, null=True)	


	@property
	def contar_carteras(self):

		cont = ProveedorCarteras.objects.filter(proveedor_id=self.id).count()

		return cont



	def __unicode__(self):
		return self.nombre


class Tipo_cartera(models.Model):
	cod_dpto=models.CharField(max_length=100,blank=True,null=True)
	cod_prov=models.CharField(max_length=100,blank=True,null=True)
	cod_dist=models.CharField(max_length=100,blank=True,null=True)
	nombre=models.CharField(max_length=100,blank=True,null=True)
	dpto=models.CharField(max_length=100,blank=True,null=True)
	provincia=models.CharField(max_length=100,blank=True,null=True)

	distrito=models.CharField(max_length=100,blank=True,null=True)



class Gestion(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

	class Meta:
		verbose_name_plural='Tipo de Gestiones'

	def __unicode__(self):
		return self.nombre


class Ubigeo(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)


class Plano(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)


class Cuadrante(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

class Producto(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)


class Estado_cliente(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)




class Tipo_contacto(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)


class Resultado(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.nombre

class Subresultado(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)
	
	class Meta:
		verbose_name_plural='Justificaciones'




	def __unicode__(self):
		return self.nombre

# class Cliente(models.Model):

#     dni  =models.CharField(max_length=100,blank=True,null=True)
#     operacion  =models.CharField(max_length=100,blank=True,null=True)
#     telefono=models.CharField(max_length=100,blank=True,null=True)
#     razon_social=models.CharField(max_length=100,blank=True,null=True)
#     tipo_persona=models.CharField(max_length=100,blank=True,null=True)
#     tipo_documento=models.CharField(max_length=100,blank=True,null=True)
#     numero_documento=models.CharField(max_length=100,blank=True,null=True)
#     nombres =models.CharField(max_length=100,blank=True,null=True)
#     observacion =models.CharField(max_length=100,blank=True,null=True)
#     fecha =models.CharField(max_length=100,blank=True,null=True)
#     estado =models.CharField(max_length=100,blank=True,null=True)

    #fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today()) 


class Cartera(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)
	estado=models.CharField(max_length=100,blank=True,null=True)
	acw=models.CharField(max_length=100,blank=True,null=True)



	def __unicode__(self):
		return self.nombre


class EstadoScore(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.nombre


class IDGestion(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.nombre
		
class Negocio(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

	def __unicode__(self):
		return self.nombre
		


class ProveedorCarteras(models.Model):
	proveedor = models.ForeignKey(Proveedor, blank=True, null=True)
	cartera=models.ForeignKey(Cartera, blank=True, null=True)
	negocio=models.ForeignKey(Negocio, blank=True, null=True)

	# def __unicode__(self):
	# 	return self.proveedor.nombre+' - '+self.cartera.nombre
		
	

class Score(models.Model):

	negocio=models.ForeignKey(Negocio, blank=True, null=True)
	gestion = models.ForeignKey(Gestion, blank=True, null=True)
	peso_tipo_gestion = models.CharField(max_length=1,default=0)
	id_gestion = models.ForeignKey(IDGestion, blank=True, null=True)
	peso_id_gestion = models.CharField(max_length=1,default=0)
	resultado = models.ForeignKey(Resultado, blank=True, null=True)
	peso_resultado = models.CharField(max_length=1,default=0)
	subresultado = models.ForeignKey(Subresultado, blank=True)

	peso_subresultado=models.CharField(max_length=100,blank=True,null=True)
	estado = models.CharField(max_length=1,default=0)


	def __unicode__(self):
		return self.negocio.nombre

class ScoreProveedor(models.Model):

	proveedor=models.ForeignKey(Proveedor, blank=True, null=True)
	cartera=models.ForeignKey(Cartera, blank=True, null=True)
	negocio=models.ForeignKey(Negocio, blank=True, null=True)
	estado=models.ForeignKey(EstadoScore, blank=True, null=True)
	negocio=models.ForeignKey(Negocio, blank=True, null=True)
	gestion = models.ForeignKey(Gestion, blank=True, null=True)
	peso_tipo_gestion = models.CharField(max_length=1,default=0)
	id_gestion = models.ForeignKey(IDGestion, blank=True, null=True)
	peso_id_gestion = models.CharField(max_length=1,default=0)
	resultado = models.ForeignKey(Resultado, blank=True, null=True)
	peso_resultado = models.CharField(max_length=1,default=0)
	subresultado = models.ForeignKey(Subresultado, blank=True)
	peso_subresultado = models.CharField(max_length=1,default=0)
	estado = models.CharField(max_length=1,default=0)
	

class Tipo_persona(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

# class Estado_cliente(models.Model):
# 	nombre=models.CharField(max_length=100,blank=True,null=True)


class Sexo(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)


class Tipo_domicilio(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

class Tipo_direccion(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

class Tipo_telefono(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)



class Fuente_telefono(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)




class Cliente(models.Model):
	user=models.CharField(max_length=100,blank=True,null=True)
	dni=models.CharField(max_length=100,blank=True,null=True)
	operacion=models.CharField(max_length=100,blank=True,null=True)
	telefono=models.CharField(max_length=100,blank=True,null=True)
	razon_social=models.CharField(max_length=100,blank=True,null=True)
	tipo_persona=models.CharField(max_length=100,blank=True,null=True)
	tipo_documento=models.CharField(max_length=100,blank=True,null=True)
	numero_documento=models.CharField(max_length=100,blank=True,null=True)
	nombres =models.CharField(max_length=100,blank=True,null=True)
	observacion =models.CharField(max_length=100,blank=True,null=True)
	fecha =models.CharField(max_length=100,blank=True,null=True)
	estado =models.CharField(max_length=100,blank=True,null=True)
	cargo_laboral =models.CharField(max_length=100,blank=True,null=True)
	fecha_nacimiento =models.CharField(max_length=100,blank=True,null=True)
	deuda_empresa =models.CharField(max_length=100,blank=True,null=True)
	#fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today()) 
	def __unicode__(self):
		return self.numero_documento

class Telefonos(models.Model):	
	
	numero_documento=models.ForeignKey(Cliente,blank=True, null=True,related_name='cliente')
	discado=models.CharField(max_length=100,blank=True,null=True)
	numero_telefono=models.CharField(max_length=100,blank=True,null=True)
	observacion=models.CharField(max_length=100,blank=True,null=True)
	tipo_contacto=models.CharField(max_length=100,blank=True,null=True)
	tipo_telefono= models.ForeignKey(Tipo_telefono,blank=True, null=True,related_name='tipo_telefono')
	fuente_telefono= models.ForeignKey(Fuente_telefono, blank=True, null=True,related_name='fuente_telefono')
	estado=models.CharField(max_length=100,blank=True,null=True)
	cliente= models.CharField(max_length=100,blank=True,null=True)
	def __unicode__(self):
		return self.numero_documento
	

class Direcciones(models.Model):
	cliente= models.ForeignKey(Cliente, blank=True, null=True,related_name='clientes')
	ubigeo=models.CharField(max_length=100,blank=True,null=True)
	direccion=models.CharField(max_length=100,blank=True,null=True)
	observacion=models.CharField(max_length=100,blank=True,null=True)
	tipo_direccion= models.ForeignKey(Tipo_direccion, blank=True, null=True,related_name='tipo_direccion')
	plano=models.CharField(max_length=100,blank=True,null=True)
	cuadrante=models.CharField(max_length=100,blank=True,null=True)
	fuente=models.CharField(max_length=100,blank=True,null=True)
	estado=models.CharField(max_length=100,blank=True,null=True)
	tipo_domicilio= models.ForeignKey(Tipo_domicilio, blank=True, null=True,related_name='tipo_domicilio')

	
# class Agente(models.Model):	
# 	nombre=models.CharField(max_length=100,blank=True,null=True)
# 	supervisor=models.CharField(max_length=100,blank=True,null=True)
# 	anexo=models.CharField(max_length=100,blank=True,null=True)
# 	estado=models.CharField(max_length=100,blank=True,null=True)
# 	user=models.CharField(max_length=100,blank=True,null=True)
# 	t_inicio_gestion=models.CharField(max_length=100,blank=True,null=True)
# 	t_fin_gestion=models.CharField(max_length=100,blank=True,null=True)
# 	t_inicio_llamada=models.CharField(max_length=100,blank=True,null=True)
# 	t_fin_llamada=models.CharField(max_length=100,blank=True,null=True)
# 	t_inicio_espera=models.CharField(max_length=100,blank=True,null=True)
# 	t_fin_espera=models.CharField(max_length=100,blank=True,null=True)
# 	contactadas=models.CharField(max_length=100,blank=True,null=True)

class Agente(models.Model):	
	nombre=models.CharField(max_length=100,blank=True,null=True)
	tipo_documento=models.CharField(max_length=100,blank=True,null=True)
	numero_documento=models.CharField(max_length=100,blank=True,null=True)
	fecha_nacimiento=models.CharField(max_length=100,blank=True,null=True)
	departamento= models.ForeignKey(Departamento, blank=True, null=True)
	provincia= models.ForeignKey(Provincia, blank=True, null=True)
	distrito= models.ForeignKey(Distrito, blank=True, null=True)
	direccion=models.CharField(max_length=100,blank=True,null=True)
	telefono=models.CharField(max_length=100,blank=True,null=True)
	grupo=models.CharField(max_length=100,blank=True,null=True)
	user= models.ForeignKey(User, blank=True, null=True,related_name="user_agente")
	sexo=models.CharField(max_length=100,blank=True,null=True)
	fecha_ingreso=models.CharField(max_length=100,blank=True,null=True)
	fecha_cese=models.CharField(max_length=100,blank=True,null=True)
	motivo_cese=models.CharField(max_length=100,blank=True,null=True)
	monto_basico=models.CharField(max_length=100,blank=True,null=True)
	obserbacion=models.CharField(max_length=100,blank=True,null=True)
	modalidad=models.CharField(max_length=100,blank=True,null=True)
	turno=models.CharField(max_length=100,blank=True,null=True)
	horario=models.CharField(max_length=100,blank=True,null=True)
	estado=models.CharField(max_length=100,blank=True,null=True)

	supervisor=models.CharField(max_length=100,blank=True,null=True)
	anexo=models.CharField(max_length=100,blank=True,null=True)
	estado=models.CharField(max_length=100,blank=True,null=True)
	t_inicio_gestion=models.CharField(max_length=100,blank=True,null=True)
	t_fin_gestion=models.CharField(max_length=100,blank=True,null=True)
	t_inicio_llamada=models.CharField(max_length=100,blank=True,null=True)
	t_fin_llamada=models.CharField(max_length=100,blank=True,null=True)
	t_inicio_espera=models.CharField(max_length=100,blank=True,null=True)
	t_fin_espera=models.CharField(max_length=100,blank=True,null=True)
	contactadas=models.CharField(max_length=100,blank=True,null=True)

class Cuentas(models.Model):
	cliente= models.ForeignKey(Cliente, blank=True, null=True)
	idcliente=models.CharField(max_length=100,blank=True,null=True)
	numero_cuenta=models.CharField(max_length=100,blank=True,null=True)
	moneda=models.CharField(max_length=100,blank=True,null=True)
	producto=models.CharField(max_length=100,blank=True,null=True)
	cartera = models.ForeignKey(Cartera, blank=True, null=True,related_name='rel_cartera')
	tipo_credito=models.CharField(max_length=100,blank=True,null=True)
	tipo_clasificacion=models.CharField(max_length=100,blank=True,null=True)
	estado=models.CharField(max_length=100,blank=True,null=True)
	fecha_vencimiento=models.CharField(max_length=100,blank=True,null=True)
	fecha_concecion= models.CharField(max_length=1000,blank=True, null=True)
	nuemero_cuotas=models.CharField(max_length=100,blank=True,null=True)
	dias_mora=models.CharField(max_length=100,blank=True,null=True)
	tramo=models.CharField(max_length=100,blank=True,null=True)
	rango_dias=models.CharField(max_length=100,blank=True,null=True)
	segmento=models.CharField(max_length=100,blank=True,null=True)
	grupo=models.CharField(max_length=100,blank=True,null=True)
	ciclo=models.CharField(max_length=100,blank=True,null=True)
	imp_capital=models.CharField(max_length=100,blank=True,null=True)
	imp_interes=models.CharField(max_length=100,blank=True,null=True)
	imp_mora=models.CharField(max_length=100,blank=True,null=True)
	imp_otros=models.CharField(max_length=100,blank=True,null=True)
	imp_total=models.CharField(max_length=100,blank=True,null=True)
	imp_vencido=models.CharField(max_length=100,blank=True,null=True)
	imp_minimo=models.CharField(max_length=100,blank=True,null=True)
	imp_descuento=models.CharField(max_length=100,blank=True,null=True)
	
	imp_campania=models.CharField(max_length=100,blank=True,null=True)
	
	imp_cap_original=models.CharField(max_length=100,blank=True,null=True)
	imp_prox_pago=models.CharField(max_length=100,blank=True,null=True)
	fecha_prox_pago=models.CharField(max_length=100,blank=True,null=True)
	observacion01=models.CharField(max_length=100,blank=True,null=True)
	observacion02=models.CharField(max_length=100,blank=True,null=True)
	observacion03=models.CharField(max_length=100,blank=True,null=True)

	nro_tarjeta=models.CharField(max_length=100,blank=True,null=True)
	fecha_deuda=models.CharField(max_length=100,blank=True,null=True)
	id_gestor=models.CharField(max_length=100,blank=True,null=True)

	



class Segmentacion(models.Model):
	telefono=models.CharField(max_length=100,blank=True,null=True)
	orden=models.CharField(max_length=100,blank=True,null=True)
	cliente=models.CharField(max_length=100,blank=True,null=True)
	base=models.CharField(max_length=100,blank=True,null=True)

class Mail(models.Model):
	correo=models.CharField(max_length=100,blank=True,null=True)
	observacion=models.CharField(max_length=100,blank=True,null=True)
	tipo_contacto= models.ForeignKey(Tipo_contacto, blank=True, null=True)
	fuente=models.CharField(max_length=100,blank=True,null=True)
	estado=models.CharField(max_length=100,blank=True,null=True)
	cliente = models.ForeignKey(Cliente, blank=True, null=True)	





# Create your models here.



