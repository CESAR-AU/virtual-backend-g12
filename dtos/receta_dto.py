from config import validador
from models.ModelRecetas import ModelReceta
from models.ModelPreparaciones import ModelPreparacion
from marshmallow_sqlalchemy import auto_field
from marshmallow import validate, fields

class RecetaRequestDTO(validador.SQLAlchemyAutoSchema):
    # nombre = auto_field(validate=validate.And(validate.Length(min=1), validate.Regexp("[A-Z]|[a-z]+")))
    class Meta:
        model = ModelReceta

class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = ModelReceta

class BuscarRecetaRequestDTO(validador.Schema):
    nombre = fields.String(required=False)
    estado = fields.Boolean(required=False)
    comensales = fields.Integer(required=False)
    dificultad = fields.String(required=False, validate=validate.OneOf(choices=['FACIL', 'MEDIO', 'DIFICIL', 'EXTREMO']))

# Para traer todos sus pasaos de la preparacion de la receta
class PreparacionResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = ModelPreparacion

class RecetaPreparacionesResponseDTO(validador.SQLAlchemyAutoSchema):
    preparaciones = fields.Nested(nested=PreparacionResponseDTO, many=True, only=['descripcion', 'orden'])
    class Meta:
        model: ModelReceta