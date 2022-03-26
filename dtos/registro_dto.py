from config import validador
from marshmallow_sqlalchemy import auto_field
from marshmallow import validate, fields
from models.usuarios import ModelUsuario


class RegistroDTO(validador.SQLAlchemyAutoSchema):
    correo = auto_field(validate=validate.Email())
    class Meta:
        model = ModelUsuario

class UsuarioResponseDTO(validador.SQLAlchemyAutoSchema):
    password = auto_field(load_only = True)
    class Meta:
        model = ModelUsuario

class LogginDTO(validador.Schema):
    correo = fields.Email(required=True)
    password = fields.String(required=True,validate=validate.Length(min=3))
