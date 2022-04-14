from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .authManager import UserManager
# Create your models here.

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, null=False)
    correo = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    nombre = models.CharField(max_length=45, null=False)
    rol = models.CharField(choices=(
        ['ADMINISTRADOR', 'ADMINISTRADOR'],
        ['MOZO', 'MOZO']), max_length=40)
    # Para seguir utilizando el panel de control
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    createAt = models.DateTimeField(auto_now_add=True, db_column='create_at')
    updateAt = models.DateTimeField(auto_now=True, db_column='update_at')

    #modelo de autorizacion 
    objects = UserManager()

    def encriptar_pwr(self):
        pass

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre', 'rol']

    class Meta:
        db_table = "tbl_usuarios"