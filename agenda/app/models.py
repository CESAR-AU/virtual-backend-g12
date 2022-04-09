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

    class CategoriaOpciones(models.TextChoices):
        TODO = 'TODO', 'TO_DO'
        IN_PROGRESS = 'IP', 'IN_PROGRESS'
        DONE = 'DONE', 'DONE'
        CANCELLED = 'CANCELLED', 'CANCELLED'
    
    opciones = [
        ('TODO', 'TO_DO'),
        ('IP', 'IN_PROGRESS'),
        ('DONE', 'DONE'),
        ('CANCELLED', 'CANCELLED'),
    ]

    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=45, null=False)
    categoria = models.CharField(max_length=45, choices=CategoriaOpciones.choices, default=CategoriaOpciones.TODO)
    #categoria = models.CharField(max_length=45, choices=opciones, default='TODO')
    fechaCaducidad = models.DateTimeField(db_column='fecha_caducidad')
    importancia = models.IntegerField(null=False)

    descripcion = models.TextField(default='---', null=True)

    createAt = models.DateTimeField(auto_now_add=True, db_column='create_at')
    updateAt = models.DateTimeField(auto_now=True, db_column='update_at')

    etiquetas = models.ManyToManyField(to=Etiqueta, related_name='tareas')
    #nuevo campo
    foto = models.ImageField(upload_to='multimedia', null=True)
    class Meta:
        db_table = "tbl_tareas"
        #ordering = ['importancia']