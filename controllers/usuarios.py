from flask_restful import Resource, request
from marshmallow import ValidationError

from config import conexion
from dtos.registro_dto import LogginDTO, RegistroDTO, UsuarioResponseDTO
from models.usuarios import ModelUsuario
from utils.message import Message


class RegistroController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RegistroDTO().load(body)
            nuevo_usuario = ModelUsuario(**data)
            # generar un hash de la contraseña
            nuevo_usuario.encripta_pwr()
            conexion.session.add(nuevo_usuario)
            conexion.session.commit()
            respuesta = UsuarioResponseDTO().dump(nuevo_usuario)
            return Message.GetMessage(message='Usuarios registrado exitosamente', success=True, data=respuesta), 201
        except ValidationError as ex:
            return Message.GetMessage(message='Error en la informacion', success=False, error=ex.args), 400
        except Exception as ex:
            conexion.session.rollback()
            return Message.GetMessage(message='No se pudo registrar el usuario', success=False, error=ex.args), 500

class LogginController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = LogginDTO().load(body)
            return Message.GetMessage(message='Logeado', success=True, data=data), 200
        except ValidationError as ex:
            return Message.GetMessage(message='Credenciales incorrectas', success=False, error=ex.args), 400
        except Exception as ex:
            conexion.session.rollback()
            return Message.GetMessage(message='No se pudo inisiar la sesion', success=False, error=ex.args), 500

