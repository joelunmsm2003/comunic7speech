from django.contrib.auth.models import User
from discador.models import *
from rest_framework import serializers

class Estado_clienteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Estado_cliente

		fields = '__all__'



class Tipo_contactoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tipo_contacto
		fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Score
		fields = '__all__'


class Tipo_personaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tipo_persona
		fields = '__all__'

class CarteraSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cartera
		fields = '__all__'

class DireccionesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Direcciones
		fields = '__all__'




class Sub_categoriaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Sub_categoria
		fields = '__all__'

class ResultadoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Resultado
		fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):

	resultado = ResultadoSerializer(many=False, read_only=True)
	cartera = CarteraSerializer(many=False, read_only=True)
	class Meta:
		model = Score
		fields = '__all__'



class Estado_clienteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Estado_cliente
		fields = '__all__'








class Tipo_domicilioSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tipo_domicilio
		fields = '__all__'


class Tipo_direccionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tipo_direccion
		fields = '__all__'


class Tipo_telefonoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tipo_telefono
		fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cliente
		fields = '__all__'



class DireccionesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Direcciones
		fields = '__all__'


class AgenteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Agente
		fields = '__all__'



class Fuente_telefonoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Fuente_telefono
		fields = '__all__'



class TelefonosSerializer(serializers.ModelSerializer):

	class Meta:
		model = Telefonos
		fields = '__all__'



class ProveedorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Proveedor
		fields = '__all__'



class CuentasSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cuentas
		fields = '__all__'


class SegmentacionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Segmentacion
		fields = '__all__'




class MailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Mail
		fields = '__all__'








