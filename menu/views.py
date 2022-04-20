from .models import Plato, Stock
from .serializers import PlatoSerializer, StockSerializer, PedidoSerializer, AgregarDetallePedidoSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import (AllowAny, #Controlador publica
IsAuthenticated, #Solisita una token
IsAuthenticatedOrReadOnly, #Solisita una token, solo GET no requiere
IsAdminUser, # Valida si es super usuario
)
from rest_framework.request import Request
from rest_framework.response import Response
from cloudinary import CloudinaryImage
from os import environ
from .permissions import SoloAdminPuedeEscribir, SoloMozoPuedeEscribir
from fact_electr.models import Pedido, DetallePedido
from rest_framework import status
from django.utils import timezone

# Create your views here.
class PlatoApiView(ListCreateAPIView):
    serializer_class = PlatoSerializer
    queryset = Plato.objects.all()
    # Permisos
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request:Request):
        data = self.serializer_class(instance=self.get_queryset(), many = True)
        for index in range(len(data.data)):
            print(data.data[index].get('foto'))
            # link = CloudinaryImage(data.data[index].get('foto')).image(secure=True)
            link = environ.get('CLOUDINARY_URL_IMG') + environ.get('CLOUDINARY_NAME') + '/' + data.data[index].get('foto')
            data.data[index]['foto'] = link
            print(link)
        return Response(data={
            'message':'Listado de platos',
            'data':data.data
        })

class StockApiView(ListCreateAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [IsAuthenticated, SoloAdminPuedeEscribir]

class PedidoApiView(ListCreateAPIView):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()
    permission_classes = [IsAuthenticated, SoloMozoPuedeEscribir]
    def post(self, request:Request):
        request.data['usuarioId'] = request.user.id
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response(data={
            'message':'Pedido creado exitosamente',
            'data': data.data
            
        }, status=status.HTTP_201_CREATED)

class AgregarDetallePedidoApiView(CreateAPIView):
    serializer_class = AgregarDetallePedidoSerializer
    queryset = DetallePedido.objects.all()
    permission_classes = [IsAuthenticated, SoloMozoPuedeEscribir]

    def post(self, request:Request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        # data.save()
        dataStock : Stock | None = Stock.objects.filter(fecha=timezone.now(), platoId = data.validated_data.get('plato_id')).first()
        cantidad = data.validated_data.get('cantidad')
        print(dataStock)
        print(dataStock.cantidad)
        print('ID',data.validated_data.get('plato_id'))
        if (dataStock is None):
            return Response(data={ 'message':'No hay stock del plato para agregar' })
        else:
            if(dataStock.cantidad >= cantidad):
                return Response(data={
                    'message':'Detalle agregado al pedido exitosamente',
                    'data': data.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(data={
                    'message':'El stock es mayor al stock actual',         
                }, status=status.HTTP_204_NO_CONTENT)
