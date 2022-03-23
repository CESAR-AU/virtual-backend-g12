from config import validador
from models.ModelPreparaciones import ModelPreparacion
from models.ModelRecetas import ModelReceta
from marshmallow import fields


class PreparacionRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = ModelPreparacion
        include_fk = True
        
class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = ModelReceta

class PreparacionResponseDTO(validador.SQLAlchemyAutoSchema):
    # Nested > es un tipo de campo que sirve para relacionar un DTO con otro DTO y usamos el parametro nested para indicar a que DTO nos queremos relacionar, tiene que ser el mismo nombre que el relationship pero si quisieramos tener un nombre diferente entonces agregamos el parametro data_key en el cual indicaremos como se llamara nuestra llave en el resultado pero de igual forma tendremos que utilizar el nombre de nuestro relationship como atributo de la clase
    receta = fields.Nested(nested=RecetaResponseDTO, data_key = 'receta_relacion')
    class Meta:
        model = ModelPreparacion
        load_instance = True
        include_fk = True
        include_relationship = True