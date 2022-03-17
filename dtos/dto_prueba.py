from config import validador
from marshmallow import fields, validate
#
class ValidadorPrueba(validador.Schema):
    nombre = fields.Str(validate=validate.Length(max=10))
    apellidos = fields.Str()
    edad = fields.Int()
    soltero = fields.Bool()

    # class Meta:
    #     fields = ['nombre', 'apellido']

#validador de response
class ValidadorUsuarioPrueba(validador.Schema):
    nombre = fields.Str()
    apellido = fields.Str()
    nacionalidad = fields.Str()