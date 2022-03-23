from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from dtos.ingredientes_recetas_dto import IngredientesRecetasRequestDTO, IngredientesRecetasResponseDTO
from models.ModelIngredientesRecetas import ModelIngredientesRecetas
from config import conexion
from utils.res_message import ResponseMessage

class IngredientesRecetasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = IngredientesRecetasRequestDTO().load(body)
            nuevoIR = ModelIngredientesRecetas(**data)
            conexion.session.add(nuevoIR)
            conexion.session.commit()
            respuesta = IngredientesRecetasResponseDTO().dump(nuevoIR)
            return ResponseMessage.GetMessage(message='Ingrediente-receta agregado exitosamente', success=True, data = respuesta), 201
        except ValidationError as ex:
            return ResponseMessage.GetMessage(message='Error en la informacion', success=True, data = {}, error=ex.args), 400
        except Exception as ex:
            conexion.session.rollback()
            return ResponseMessage.GetMessage(message='Hubo un error', success=True, data = {}, error=ex.args), 400