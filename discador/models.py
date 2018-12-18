from __future__ import unicode_literals

from django.db import models



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

	def __unicode__(self):
		return self.proveedor.nombre+' - '+self.cartera.nombre
		
	

class Score(models.Model):

	negocio=models.ForeignKey(Negocio, blank=True, null=True)
	nombre=models.CharField(max_length=100,blank=True,null=True)
	gestion = models.ForeignKey(Gestion, blank=True, null=True)
	id_gestion = models.ForeignKey(IDGestion, blank=True, null=True)
	resultado = models.ForeignKey(Resultado, blank=True, null=True)
	subresultado = models.ForeignKey(Subresultado, blank=True)
	peso=models.CharField(max_length=100,blank=True,null=True)
	estado = models.CharField(max_length=1,default=0)
	negocio = models.ForeignKey(Negocio, blank=True, null=True)

	def __unicode__(self):
		return self.negocio.nombre

class ScoreProveedor(models.Model):

	score=models.ForeignKey(Score, blank=True, null=True)
	proveedor=models.ForeignKey(ProveedorCarteras, blank=True, null=True)
	estado=models.ForeignKey(EstadoScore, blank=True, null=True)

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

class Cliente(models.Model):
	user=models.CharField(max_length=100,blank=True,null=True)
	dni  =models.CharField(max_length=100,blank=True,null=True)
	operacion  =models.CharField(max_length=100,blank=True,null=True)
	telefono=models.CharField(max_length=100,blank=True,null=True)
	razon_social=models.CharField(max_length=100,blank=True,null=True)
	tipo_persona=models.CharField(max_length=100,blank=True,null=True)
	tipo_documento=models.CharField(max_length=100,blank=True,null=True)
	numero_documento=models.CharField(max_length=100,blank=True,null=True)
	nombres =models.CharField(max_length=100,blank=True,null=True)
	observacion =models.CharField(max_length=100,blank=True,null=True)
	fecha =models.CharField(max_length=100,blank=True,null=True)
	estado =models.CharField(max_length=100,blank=True,null=True)
	#fecha = models.DateTimeField(db_column='fecha', default=datetime.datetime.today()) 


class Direcciones(models.Model):
	cliente= models.ForeignKey(Cliente, blank=True, null=True,related_name='cliente')
	ubigeo=models.CharField(max_length=100,blank=True,null=True)
	direccion=models.CharField(max_length=100,blank=True,null=True)
	observacion=models.CharField(max_length=100,blank=True,null=True)
	tipo_direccion= models.ForeignKey(Tipo_direccion, blank=True, null=True,related_name='tipo_direccion')
	plano=models.CharField(max_length=100,blank=True,null=True)
	cuadrante=models.CharField(max_length=100,blank=True,null=True)
	fuente=models.CharField(max_length=100,blank=True,null=True)
	estado=models.CharField(max_length=100,blank=True,null=True)
	tipo_domicilio= models.ForeignKey(Tipo_domicilio, blank=True, null=True,related_name='tipo_domicilio')

	
class Agente(models.Model):	
	nombre=models.CharField(max_length=100,blank=True,null=True)
	supervisor=models.CharField(max_length=100,blank=True,null=True)
	anexo=models.CharField(max_length=100,blank=True,null=True)
	estado=models.CharField(max_length=100,blank=True,null=True)
	user=models.CharField(max_length=100,blank=True,null=True)
	t_inicio_gestion=models.CharField(max_length=100,blank=True,null=True)
	t_fin_gestion=models.CharField(max_length=100,blank=True,null=True)
	t_inicio_llamada=models.CharField(max_length=100,blank=True,null=True)
	t_fin_llamada=models.CharField(max_length=100,blank=True,null=True)
	t_inicio_espera=models.CharField(max_length=100,blank=True,null=True)
	t_fin_espera=models.CharField(max_length=100,blank=True,null=True)
	contactadas=models.CharField(max_length=100,blank=True,null=True)
	contactadas=models.CharField(max_length=100,blank=True,null=True)



class Fuente_telefono(models.Model):
	nombre=models.CharField(max_length=100,blank=True,null=True)

class Telefonos(models.Model):	
	numero_documento=models.CharField(max_length=100,blank=True,null=True)
	discado=models.CharField(max_length=100,blank=True,null=True)
	numero_telefono=models.CharField(max_length=100,blank=True,null=True)
	observacion=models.CharField(max_length=100,blank=True,null=True)
	tipo_contacto=models.CharField(max_length=100,blank=True,null=True)
	tipo_telefono= models.ForeignKey(Tipo_telefono,blank=True, null=True,related_name='tipo_telefono')
	fuente_telefono= models.ForeignKey(Fuente_telefono, blank=True, null=True,related_name='fuente_telefono')
	estado=models.CharField(max_length=100,blank=True,null=True)
	cliente= models.ForeignKey(Cliente, blank=True, null=True,related_name='nombre')
	




class Cuentas(models.Model):
	cliente= models.ForeignKey(Cliente, blank=True, null=True)
	capital=models.CharField(max_length=100,blank=True,null=True)
	numero_cuenta=models.CharField(max_length=100,blank=True,null=True)
	total=models.CharField(max_length=100,blank=True,null=True)
	compania=models.CharField(max_length=100,blank=True,null=True)
	mora=models.CharField(max_length=100,blank=True,null=True)
	interes=models.CharField(max_length=100,blank=True,null=True)
	dias_mora=models.CharField(max_length=100,blank=True,null=True)
	tramo=models.CharField(max_length=100,blank=True,null=True)
	fecha_vencimiento=models.CharField(max_length=100,blank=True,null=True)
	estado=models.CharField(max_length=100,blank=True,null=True)
	proveedor= models.ForeignKey(Proveedor, blank=True, null=True,related_name='rel_proveedor')
	cartera = models.ForeignKey(Cartera, blank=True, null=True,related_name='rel_cartera')



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



