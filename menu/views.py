from .models import Plato, Stock
from .serializers import PlatoSerializer, StockCreateSerializer, StockSerializer, PedidoSerializer, AgregarDetallePedidoSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import (AllowAny, #Controlador publica
IsAuthenticated, #Solisita una token
IsAuthenticatedOrReadOnly, #Solisita una token, solo GET no requiere
IsAdminUser, # Valida si es super usuario
SAFE_METHODS)
from rest_framework.request import Request
from rest_framework.response import Response
from cloudinary import CloudinaryImage
from os import environ
from .permissions import SoloAdminPuedeEscribir, SoloMozoPuedeEscribir
from fact_electr.models import Pedido, DetallePedido
from rest_framework import status
from django.utils import timezone
from django.db import transaction, IntegrityError

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
    # serializer_class = StockSerializer
    queryset = Stock.objects.all()
    permission_classes = [IsAuthenticated, SoloAdminPuedeEscribir]
    def get_serializer_class(self):
        if not self.request.method in SAFE_METHODS:
            return StockCreateSerializer
        return StockSerializer

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
        dataStock : Stock | None = Stock.objects.filter(fecha=timezone.now(), platoId = data.validated_data.get('plato_id'), cantidad__gte=data.validated_data.get('cantidad')).first()
        print('ID', data.validated_data.get('plato_id'))
        print('dataStock', dataStock)
        print('CANTIDAD', data._validated_data.get('cantidad'))
        
        if (dataStock is None):
            return Response(data={ 'message':'No hay stock para ese producto para el dia de hoy' },status=status.HTTP_400_BAD_REQUEST)
        print('ID 2',data.validated_data.get('plato_id'))
        
        pedido:Pedido|None = Pedido.objects.filter(id=data.validated_data.get('pedido_id')).first()
        if (pedido is None):
            return Response(data={'message':'No hay ese pedido'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            with transaction.atomic():
                nuevo_detalle = DetallePedido(cantidad=data.validated_data.get('cantidad'), stockId = dataStock, pedidoId = pedido)
                nuevo_detalle.save()
                dataStock.cantidad = dataStock.cantidad - nuevo_detalle.cantidad
                dataStock.save()
                pedido.total += (nuevo_detalle.cantidad * dataStock.precio_diario)
                pedido.save()
            
        except IntegrityError:
            return Response(data={'message':'Error al crear el pedido'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response(data={'message':'Error en el servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data={'message':'Detalle agrtegado al pedido'}, status=status.HTTP_200_OK)
            
