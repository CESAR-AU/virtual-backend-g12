from rest_framework import serializers
from .models import Plato, Stock
from fact_electr.models import Pedido, DetallePedido

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Plato

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Stock
        '''depth = 1
        extra_kwargs = {
            'id':{'read_only':True},
            'plato_id':{'read_only':True},
        }'''

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Pedido
        # depth = 1

class AgregarDetallePedidoSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField(required = True, min_value = 1)
    plato_id = serializers.IntegerField(required = True, min_value = 1)
    pedido_id = serializers.IntegerField(required = True, min_value = 1)