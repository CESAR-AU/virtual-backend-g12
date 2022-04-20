from django.db import models
from autorizacion.models import Usuario
from menu.models import Stock
from django.utils import timezone

# Create your models here.

class Pedido(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.FloatField(null=False)
    nro_doc_cliente = models.CharField(max_length=12, null=True)
    tipo_doc_cliente = models.CharField(choices=(['RUC','RUC'], ['DNI','DNI']), max_length=5, null=True)
    mesa = models.IntegerField()
    propina = models.FloatField()

    usuarioId = models.ForeignKey(to=Usuario, related_name='pedidos', db_column='usuario_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_pedidos'

class Comprobante(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    serie = models.CharField(max_length=5, null=False)
    numero = models.CharField(max_length=10, null=False)
    pdf = models.TextField()
    cdr = models.TextField()
    xml = models.TextField()
    tipo = models.CharField(choices=(['BOLETA','BOLETA'], ['FACTURA', 'FACTURA']), null=False, max_length=10)

    pedido = models.OneToOneField(to=Pedido, related_name='comprobante', on_delete=models.CASCADE, db_column='pedido_id')

    class Meta:
        db_table = 'tbl_comprobantes'
        unique_together = [['serie', 'numero']]

class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    cantidad = models.IntegerField(null=False)

    stockId = models.ForeignKey(
        to=Stock, related_name='detalle_pedidos', on_delete=models.CASCADE, db_column='stock_id')
    pedidoId = models.ForeignKey(
        to=Pedido, related_name='detalle_pedidos', on_delete=models.CASCADE, db_column='pedido_id')

    class Meta:
        db_table = 'tbl_detalle_pedidos'
