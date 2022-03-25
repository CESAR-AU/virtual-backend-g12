from config import conexion
from sqlalchemy import Column, types


class ModelCategoria(conexion.Model):
    __tablename__ = 'tbl_categorias'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.String(45),  nullable=False)
