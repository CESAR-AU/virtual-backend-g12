from django.db import models
from cloudinary import models as modelClouddinary

# Create your models here.
class Plato(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=45, null=False)
    # foto = models.ImageField(max_length=45)
    foto = modelClouddinary.CloudinaryField(folder='plato')
    disponible = models.BooleanField(default=True)
    precio = models.FloatField(null=False)
    createAt = models.DateTimeField(auto_now_add=True, db_column='create_at')
    updateAt = models.DateTimeField(auto_now=True, db_column='update_at')

    class Meta:
        db_table = "tbl_platos"

class Stock(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    fecha = models.DateField(null=False)
    cantidad = models.IntegerField(null=False)
    precio_diario = models.FloatField(null=False)

    platoId = models.ForeignKey(to=Plato, related_name='stock', on_delete=models.CASCADE, db_column='plato_id')

    class Meta:
        db_table = 'tbl_stock'
        unique_together = [['fecha', 'platoId']]