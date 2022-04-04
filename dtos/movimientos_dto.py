from config import validador
from models.movimientos import ModelMovimientos
from marshmallow_sqlalchemy import auto_field
from dtos.categoria_dto import CategoriaResponseDTO
from marshmallow import fields

class MovimientoRequestDTO(validador.SQLAlchemyAutoSchema):
    usuario_id = auto_field(dump_only=True)
    class Meta:
        include_fk = True
        model = ModelMovimientos

class MovimientoResponseDTO(validador.SQLAlchemyAutoSchema):
    categoria = fields.Nested(nested=CategoriaResponseDTO, only=['nombre'])
    class Meta:
        model = ModelMovimientos
        include_relationships = True