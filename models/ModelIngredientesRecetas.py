from config import conexion
from sqlalchemy import Column, types, orm
from sqlalchemy.sql.schema import ForeignKey

class ModelIngredientesRecetas(conexion.Model):
    __tablename__ = 'tbl_ingredientes_recetas'
    id = Column(type_= types.Integer, primary_key=True, autoincrement=True)
    unidad_medida = Column(type_=types.String(45), nullable=False)

    tbl_recetas_id = Column(ForeignKey(column='tbl_recetas.id'), type_=types.Integer)
    tbl_ingredientes_id = Column(ForeignKey(column='tbl_ingredientes.id'), type_=types.Integer)

    receta = orm.relationship('ModelReceta', backref='receta_ingredientes')
    ingrediente = orm.relationship('Ingrediente', backref='ingredientes_recetas')