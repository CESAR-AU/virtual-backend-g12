from django.db import models

# Create your models here.
class Etiqueta(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=20, unique=True, null=False)
    # columnas de auditoia => ayuda en el siguimiento
    createAt = models.DateTimeField(auto_now_add=True, db_column='create_at')
    updateAt = models.DateTimeField(auto_now=True, db_column='update_at')

    class Meta:
        db_table = "tbl_etiquetas"
        ordering = ['-nombre']

class Tarea(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=45, null=False)
    categoria = models
    fecha_caducidad = models.DateTimeField()
    importancia = models.IntegerField(max_length=10, null=False)
    # columnas de auditoia => ayuda en el siguimiento
    createAt = models.DateTimeField(auto_now_add=True, db_column='create_at')
    updateAt = models.DateTimeField(auto_now=True, db_column='update_at')

    class Meta:
        db_table = "tbl_tareas"
        ordering = ['importancia']