from flask_restful import Resource, request
from marshmallow import ValidationError
from config import conexion
from models.movimientos import ModelMovimientos
from dtos.movimientos_dto import MovimientoRequestDTO, MovimientoResponseDTO
from utils.message import Message
from flask_jwt import jwt_required, current_identity

class MovimientoController(Resource):
    @jwt_required()
    def post(self):
        body = request.get_json()
        try:
            data = MovimientoRequestDTO().load(body)
            data['usuario_id'] = current_identity.id
            nuevo_movimiento = ModelMovimientos(**data)
            conexion.session.add(nuevo_movimiento)
            conexion.session.commit()
            respuesta = MovimientoResponseDTO().dump(nuevo_movimiento)
            return Message.GetMessage(message='Movimiento creado exitosamente', success=True, data=respuesta), 201
        except ValidationError as ex:
            return Message.GetMessage(message='Hubo un error en la informacion', success=False, error=ex.args), 400
        except Exception as ex:
            conexion.session.rollback()
            return Message.GetMessage(message='Hubo un error al crear el movimiento', success=False, error=ex.args), 400

    @jwt_required()
    def get(self):
        try:
            print('MOVIMIENTOS')
            movimientos : list[ModelMovimientos] | None = conexion.session.query(ModelMovimientos).filter_by(usuario_id = current_identity.id).all()
            respuesta = MovimientoResponseDTO(many=True).dump(movimientos)
            return Message.GetMessage(message='Lista de Movimientos', success=True, data=respuesta), 200
        except Exception as ex:
            return Message.GetMessage(message='Hubo un error al listar los movimientos', success=False, error=ex.args), 400
