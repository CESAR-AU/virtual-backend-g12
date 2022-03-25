from config import conexion
from sqlalchemy import Column, types


class ModelUsuario(conexion.Model):
    __tablename__ = 'tbl_usuarios'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.String(45))
    apellidos = Column(type_=types.String(45))
    correo = Column(type_=types.String(45), nullable=False, unique=True)
    password = Column(type_=types.Text(), nullable=False)
