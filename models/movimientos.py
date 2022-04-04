from config import conexion
from sqlalchemy import Column, types, orm
from sqlalchemy.sql.schema import ForeignKey


class ModelMovimientos(conexion.Model):
    __tablename__ = 'tbl_movimientos'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    monto = Column(type_=types.Float(), nullable=False)
    tipo = Column(type_=types.Enum('INGRESO', 'EGRESO'))
    descripcion = Column(type_=types.String(150))
    moneda = Column(type_=types.Enum('SOLES', 'DOLARES', 'EUROS'))
    fecha_creacion = Column(type_=types.DateTime(), nullable=False)

    usuario_id = Column(ForeignKey(column='tbl_usuarios.id'), type_=types.Integer)
    categoria_id = Column(ForeignKey(column='tbl_categorias.id'), type_=types.Integer)

    usuario = orm.relationship('ModelUsuario', backref='usuario_movimientos')
    categoria = orm.relationship('ModelCategoria', backref='categoria_movimientos')
