from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    '''Clase que sirve para manejar el comportamiento del auth_user'''
    def create_user(self, correo, nombre, rol, password):
        '''Creacion de usuarion sin el comando createsuperuser'''
        if not correo:
            raise ValueError('El usuario debe tener obligatoriamente un correo')
        correo = self.normalize_email(correo)
        #
        self.model()

        nuevo_usuario = self.model(correo=correo, nombre=nombre, rol=rol)
        nuevo_usuario.set_password(password)
        nuevo_usuario.save(using=self._db)
        return nuevo_usuario
    
    def create_superuser(self, correo, nombre, rol, password):
        '''Creacion de un super usuario por consola'''
        usuario = self.create_user(correo, nombre, rol, password)
        usuario.is_superuser = True
        usuario.is_staff = True

        usuario.save(using=self._db)