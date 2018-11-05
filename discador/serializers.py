from django.contrib.auth.models import User
from app.models import *
from rest_framework import serializers

class Estado_clienteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Estado_cliente
		fields = '__all__'