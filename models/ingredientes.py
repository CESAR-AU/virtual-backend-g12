from config import conexion
from sqlalchemy import Column, types

class Ingrediente(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.String(45), nullable=False, unique=True)
    # decripcion = Column(type_=types.String(100))
    __tablename__ = 'tbl_ingredientes'
    