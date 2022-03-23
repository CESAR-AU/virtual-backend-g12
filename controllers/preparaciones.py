from flask_restful import Resource, request
from marshmallow import ValidationError
from models.ModelPreparaciones import ModelPreparacion
from dtos.preparacion_dto import PreparacionRequestDTO, PreparacionResponseDTO
from models.ModelRecetas import ModelReceta
from utils.res_message import ResponseMessage
from config import conexion

class PreparacionesController(Resource):
    def post(self):
        try:
            body = request.get_json()
            data = PreparacionRequestDTO().load(body)
            print(data)
            nueva_preparacion = ModelPreparacion(**data)
            conexion.session.add(nueva_preparacion)
            conexion.session.commit()
            respuesta = PreparacionResponseDTO().dump(nueva_preparacion)
            return ResponseMessage.GetMessage(message='Lista de recetas', success=True, data= respuesta), 200
        except ValidationError as ex:
            return ResponseMessage.GetMessage(message='Informacion incorrecta', success=False, data= {}, error=ex.args), 400
        except Exception as ex:
            conexion.session.rollback()
            return ResponseMessage.GetMessage(message='Hubo un error', success=False, data= {}, error=ex.args), 400
    
    def get(self, id):
        try:
            preparacion: ModelPreparacion | None = conexion.session.query(ModelPreparacion).filter_by(id = 1).first()
            respuesta = PreparacionResponseDTO().dump(preparacion)
            return ResponseMessage.GetMessage(message='Preparacion', success=True, data = respuesta), 200
        except Exception as ex:
            return ResponseMessage.GetMessage(message='Hubo un error', success=False, data= {}, error=ex.args), 400