from config import conexion
from sqlalchemy import Column, types
from bcrypt import hashpw, gensalt


class ModelUsuario(conexion.Model):
    __tablename__ = 'tbl_usuarios'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.String(45))
    apellidos = Column(type_=types.String(45))
    correo = Column(type_=types.String(45), nullable=False, unique=True)
    password = Column(type_=types.Text(), nullable=False)

    def encripta_pwr(self):
        # primero el pass le convierto a bytes
        passsword_bytes = bytes(self.password, 'utf-8')
        # usamos el metodo gensalt para generar un hash aleotorio
        salt = gensalt(rounds=10)
        hash_password = hashpw(passsword_bytes, salt)
        # convertir en strin para guardar en la db
        hash_pwr_str = hash_password.decode('utf-8')
        # sobre escribo password
        self.password = hash_pwr_str
