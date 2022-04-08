from rest_framework import serializers

from .models import Tarea, Etiqueta

class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length = 40, trim_whitespace = True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(max_length = 8, min_length = 8, regex="[0-9]")

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        # fields = ['']
        fields = '__all__'
        # exclude = ['']
        depth = 1

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'