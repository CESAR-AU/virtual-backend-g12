from email.policy import default
from config import conexion
from sqlalchemy import Column, types

class ModelReceta(conexion.Model):
    __tablename__ = 'tbl_recetas'
    
    id = Column(type_= types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.String(45), nullable=False)
    estado = Column(type_=types.Boolean, default=True)
    comensales = Column(type_=types.Integer)
    duracion = Column(type_=types.String(45))
    dificultad = Column(type_=types.Enum('FACIL', 'MEDIO', 'DIFICIL', 'EXTREMO'), default='FACIL')
