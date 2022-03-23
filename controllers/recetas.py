from flask_restful import Resource, request
from marshmallow import ValidationError
from dtos.paginacion_dto import PaginacionRequestDTO
from dtos.receta_dto import (BuscarRecetaRequestDTO, RecetaRequestDTO, RecetaResponseDTO, RecetaPreparacionesResponseDTO)
from models.ModelRecetas import ModelReceta
from config import conexion
from utils.res_message import ResponseMessage
from math import ceil

#CREATE, GET ALL (PAGINATED), UPDATE, FIND por like de nombre, DELETE
class RectasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RecetaRequestDTO().load(body)
            nueva_receta = ModelReceta(
                nombre=data.get('nombre'),
                estado=data.get('estado'),
                comensales=data.get('comensales'),
                duracion=data.get('duracion'),
                dificultad=data.get('dificultad')
                )
            conexion.session.add(nueva_receta)
            conexion.session.commit()
            receta_guradado = RecetaResponseDTO().dump(nueva_receta)
            return ResponseMessage.GetMessage(message='Receta creada exitosamente', success=True, data=receta_guradado), 200
        except ValidationError as ex:
            return ResponseMessage.GetMessage(message='La informacion es incorrecta', success=False, error=ex.args, data={}), 400
        except Exception as ex:
            conexion.session.rollback()
            return ResponseMessage.GetMessage(message='Error al crear la receta', success=False, error=ex.args, data={}), 500

    def get(self):
        # TODO: agregar paginacion
        # page > que pagina queremos
        # perPage
        try:
            query_params = request.args
            paginacion = PaginacionRequestDTO().load(query_params)
            page, perPage = paginacion.get('page'), paginacion.get('perPage')
            page = 1 if page <= 0 else page
            perPage = 1 if perPage <= 0 else perPage
            skip = perPage * (page - 1)
            recetas = conexion.session.query(ModelReceta).limit(perPage).offset(skip).all()
            #SELCT COUNT(*) FROM recetas
            total = conexion.session.query(ModelReceta).count()
            itemsXPage =  perPage if total >= perPage else total
            totalPage = ceil(total / itemsXPage) if itemsXPage > 0 else None
            prevPage = page - 1 if page > 1 and page <= totalPage else None
            nextPage = page + 1 if totalPage > 1 and page < totalPage else None

            respuesta = RecetaResponseDTO(many=True).dump(recetas)

            pagination = {
                'pagination':{
                    'total':total,
                    'itemsXPage': itemsXPage,
                    'totalPage': totalPage,
                    'prevPage': prevPage,
                    'nextPage': nextPage
                }           
            }
            return ResponseMessage.GetMessage(message='Lista de recetas', success=True, data=(respuesta, pagination)), 200
        except Exception as ex:
            return ResponseMessage.GetMessage(message='Hubo un error', success=False, error=ex.args, data=query_params), 500

class BuscarRecetaController(Resource):
    def get(self):
        try:
            query_params = request.args
            parametros_buscar = BuscarRecetaRequestDTO().load(query_params)
            recetas2 = conexion.session.query(ModelReceta).filter(ModelReceta.nombre.like('%ss%')).all()
            # recetas = conexion.session.query(ModelReceta).filter_by(**parametros_buscar).all()
            nombre = parametros_buscar.get('nombre', '')
            if parametros_buscar.get('nombre') is not None:
                del parametros_buscar['nombre']
            recetas = conexion.session.query(ModelReceta).filter(ModelReceta.nombre.like('%{}%'.format(nombre))).filter_by(**parametros_buscar).all()
            response_recetas = RecetaResponseDTO(many=True).dump(recetas)
            return ResponseMessage.GetMessage(message='Lista de recetas', success=True, data=response_recetas), 200
        except ValidationError as ex:
            return ResponseMessage.GetMessage(message='Hubo un error en los parametros', success=False, error=ex.args, data=query_params), 400
        except Exception as ex:
            return ResponseMessage.GetMessage(message='Hubo un error', success=False, error=ex.args, data=query_params), 500

class RecetaController(Resource):
    def get(self, id):
        try:
            receta: ModelReceta | None = conexion.session.query(ModelReceta).filter(id = id).first()
            if receta is None:                
                return ResponseMessage.GetMessage(message='No se encontro la receta', success=True, data={}), 404
            else:
                print(receta.preparaciones)
                respuesta = RecetaPreparacionesResponseDTO().dump(receta)
                return ResponseMessage.GetMessage(message='Info receta', success=True, data=respuesta), 200
        except Exception as ex:
            return ResponseMessage.GetMessage(message='Hubo un error', success=False, data={}, error=ex.args), 400