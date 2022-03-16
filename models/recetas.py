from msilib.schema import Class
from sqlalchemy import Column, types
from config import conexion

class Recetas(conexion.Model):
    id = Column(type_=types.Integer)