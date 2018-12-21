class AgenteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Agente
		fields = '__all__'