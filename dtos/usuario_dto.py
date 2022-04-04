from config import validador
from marshmallow import fields, validate

class ResetPasswordRequestDTO(validador.Schema):
    correo = fields.Email(required=True)

class ValidarTokenRequestDTO(validador.Schema):
    token = fields.String(required=True, validate=validate.Length(min=200, max=250))