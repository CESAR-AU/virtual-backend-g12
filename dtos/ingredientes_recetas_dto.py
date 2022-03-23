from config import validador
from models.ModelIngredientesRecetas import ModelIngredientesRecetas
from dtos.receta_dto import RecetaResponseDTO
from dtos.preparacion_dto import PreparacionResponseDTO
from marshmallow import fields

class IngredientesRecetasRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = ModelIngredientesRecetas
        include_fk=True


class IngredientesRecetasResponseDTO(validador.SQLAlchemyAutoSchema):
    receta = fields.Nested(nested=RecetaResponseDTO)
    ingrediente = fields.Nested(nested=PreparacionResponseDTO)
    class Meta:
        model = ModelIngredientesRecetas
        include_fk=True
        load_instance = True
        include_relationship = True