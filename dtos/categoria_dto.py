from config import validador
from models.categorias import ModelCategoria

class CategoriaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = ModelCategoria