# from django.shortcuts import render > para renderizar archivos html
# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import (PruebaSerializer, TareasSerializer, EtiquetaSerializer, 
TareaSerializer, TareaPersonalizableSerializer, ArchivoSerializer)
from .models import Tarea, Etiqueta
from datetime import datetime
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@api_view(http_method_names=['GET', 'POST'])
def inicio(resquest: Request):
    print(resquest.method)
    if resquest.method == 'GET':
        return Response(data={
            'message':'API de Agenda',
            'success':True,
            'data':resquest.data
        })
    elif resquest.method == 'POST':
        return Response(data={
            'message':'API POST',
            'success':True,
        }, status=201)

class PruebaApiView(ListAPIView):
    serializer_class = PruebaSerializer
    queryset = [{
        'nombre':'Juan',
        'apellido': 'Jsdki nmsf',
        'correo': 'Jsdki@c-insd.psd',
        'dni': '12345678',
        'estado_civil': 'adñkjahdsfkj',
    },
    {
        'nombre':'Juana',
        'apellido': 'Jsdasdsdki nmsf',
        'correo': 'Juandamjd@c-insd.psd',
        'dni': '87654321',
        'estado_civil': 'soslsk',
    }]


    def get(self, request: Request):
        informacion = self.queryset

        infromacion_serializada = self.serializer_class(data=informacion, many=True)
        infromacion_serializada.is_valid(raise_exception=True)
        return Response(data={
            'message':'Hola',
            'data':infromacion_serializada.data
        })

class TareasApiView(ListCreateAPIView):
    queryset = Tarea.objects.all() #SELECT * FROM tbl_tareas
    serializer_class = TareasSerializer

    def post(self, request: Request):
        serializador = self.serializer_class(data=request.data)
        if(serializador.is_valid()):
            fecha_caducidad : timezone = serializador.validated_data.get('fechaCaducidad')
            importancia = serializador.validated_data.get('importancia') 
            
            if (importancia > 10 or importancia < 0):
                return Response(data={
                    'message': 'La importancia debe estar entre 0 - 10',
                    'data': serializador.data,
                }, status=status.HTTP_400_BAD_REQUEST)
            elif(timezone.now() > fecha_caducidad):
                return Response(data={
                    'message': 'La fecha no puede ser menor a la fecha actual',
                    'data': serializador.data,
                }, status=status.HTTP_400_BAD_REQUEST)

            serializador.save()
            return Response(data={
                    'message': 'La tarea fue guardado',
                    'data': serializador.data,
                }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'La data no es valida',
                'error': serializador.errors
                }, status=status.HTTP_400_BAD_REQUEST)
class EtiquetasApiView(ListCreateAPIView):
    queryset = Etiqueta.objects.all() #SELECT * FROM tbl_tareas
    serializer_class = EtiquetaSerializer


class TareaApiView(RetrieveUpdateDestroyAPIView):
    # serializer_class = TareaSerializer
    serializer_class = TareaPersonalizableSerializer
    queryset = Tarea.objects.all()

class ArchivosApiView(CreateAPIView):
    serializer_class = ArchivoSerializer

    def post(self, request:Request):
        data = self.serializer_class(data=request.FILES)
        requy_params = request.query_params
        carpeta_destino = requy_params.get('carpeta')
        nombre_archivo = requy_params.get('nombre_archivo')
        if(data.is_valid()):
            print(data.validated_data.get('archivo'))
            archivo:InMemoryUploadedFile = data.validated_data.get('archivo')
            print(archivo.file)
            print(archivo.size)
            print(archivo.content_type_extra)
            print(archivo.content_type)
            print(archivo.charset)
            print(archivo.field_name)
            print(archivo.fileno)
            print(archivo.flush)
            if(archivo.size > (5 * 1024 * 1024)):
                return Response(data={
                'message': 'Archivo muy grande, no puede ser mas de 5MB',
                'data': data.data,
                'ruta': resultado
                }, status=status.HTTP_400_BAD_REQUEST)
            ruta = carpeta_destino + '/' if carpeta_destino is not None else ''
            ruta = ruta + nombre_archivo if nombre_archivo is not None else ruta + archivo.name
            resultado = default_storage.save(ruta, ContentFile(archivo.read()))
            print(resultado)
            return Response(data={
                'message': 'Archivo guardado',
                'data': data.data,
                'ruta': resultado
                }, status=status.HTTP_200_OK)
        else:
            return Response(data={
                'message': 'Seleccione una imagen para subir',
                'data': data.errors
                }, status=status.HTTP_400_BAD_REQUEST)