from rest_framework import serializers

from .models import Tarea, Etiqueta

class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length = 40, trim_whitespace = True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(max_length = 8, min_length = 8, regex="[0-9]")

class TareasSerializer(serializers.ModelSerializer):
    foto = serializers.CharField(max_length = 100)
    class Meta:
        model = Tarea
        # fields = ['']
        fields = '__all__'
        # exclude = ['']
        # depth = 1
        extra_kwargs = {
            'etiquetas':{'write_only':True}
        }

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
        depth = 1

class EtiquetaSerializer(serializers.ModelSerializer):
    tareas_relacionadas = TareasSerializer(many=True, read_only=True, source='tareas')
    class Meta:
        model = Etiqueta
        fields = '__all__'
        # depth = 1
        extra_kwargs = {
            #'nombre':{'write_only':True},
            'id':{'read_only':True}
        }
        read_only_fields = ['createAt']

class TareaPersonalizableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
        depth = 1
        # nombre, id es de solo lectura y no aceptara una actualizacion
        extra_kwargs = {
            'nombre':{'read_only':True},
            'id':{'read_only':True}
        }

class ArchivoSerializer(serializers.Serializer):
    #archivo = serializers.ImageField(required=True, max_length=100, use_url=True, verbose_name='multimedia')
    archivo = serializers.ImageField(required=True, max_length=100, use_url=True)
    help_text = 'Solo imagenes'

class EliminarArchivoSerializer(serializers.Serializer):
    archivo = serializers.CharField(required=True, max_length=100)