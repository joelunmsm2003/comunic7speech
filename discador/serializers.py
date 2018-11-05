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
		fields = '_all_'

class ScoreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Score
		fields = '_all_'


class Tipo_personaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tipo_persona
		fields = '_all_'


class ScoreSerializer(serializers.ModelSerializer):

	class Meta:
		model = Score
		fields = '_all_'



class Estado_clienteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Estado_cliente
		fields = '_all_'



class CarteraSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cartera
		fields = '_all_'




class Tipo_domicilioSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tipo_domicilio
		fields = '_all_'


class Tipo_direccionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tipo_direccion
		fields = '_all_'


class Tipo_telefonoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tipo_telefono
		fields = '_all_'


class ClienteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cliente
		fields = '_all_'



class DireccionesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Direcciones
		fields = '_all_'


class AgenteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Agente
		fields = '__all__'



class Fuente_telefonoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Fuente_telefono
		fields = '_all_'



class TelefonosSerializer(serializers.ModelSerializer):

	class Meta:
		model = Telefonos
		fields = '_all_'



class ProveedorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Proveedor
		fields = '_all_'



class CuentasSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cuentas
		fields = '_all_'


class SegmentacionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Segmentacion
		fields = '_all_'




class MailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Mail
		fields = '_all_'









