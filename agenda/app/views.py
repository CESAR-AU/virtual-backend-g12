# from django.shortcuts import render > para renderizar archivos html
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import PruebaSerializer, TareaSerializer, EtiquetaSerializer
from .models import Tarea, Etiqueta

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
    serializer_class = TareaSerializer

class EtiquetasApiView(ListCreateAPIView):
    queryset = Etiqueta.objects.all() #SELECT * FROM tbl_tareas
    serializer_class = EtiquetaSerializer