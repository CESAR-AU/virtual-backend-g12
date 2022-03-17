from flask_restful import Resource, request
from config import conexion
from models.ingredientes import Ingrediente
from dtos.dto_prueba import ValidadorPrueba, ValidadorUsuarioPrueba
from dtos.ingrediente_dto import IngredienteRequestDTO, IngredienteResponseDTO
from marshmallow.exceptions import ValidationError

class IngredientesController(Resource):
    def get(self):
        resultado = conexion.session.query(Ingrediente).all()
        print(resultado)

        ingredientes_serializados = IngredienteResponseDTO(many=True).dump(resultado)
        return{
            'message':'Ingredientes',
            'success': True,
            'data': ingredientes_serializados
        }, 200
    
    def post(self):
        # print(request.get_json())
        #validar entradas
        data = request.get_json()
        # validacion = ValidadorPrueba().load(data)
        # print(validacion)
        try:
            data_serializada = IngredienteRequestDTO().load(data)
            print(data_serializada)
            #IInstaciamos el modelo Ingrediente()
            nuevoIngrediente = Ingrediente()
            #Asignamos los datos al modelo para guardarlo en la DB
            nuevoIngrediente.nombre = data_serializada.get('nombre')
            #abrimos una sesion para la transaccion y le agregamos la transaccion
            conexion.session.add(nuevoIngrediente) #nueva transaccion
            #hacemos el commit para guardarlo definitivamente y terminar la session
            conexion.session.commit()
            
            ingrediente_serializado = IngredienteResponseDTO.dump(nuevoIngrediente)

            return{
                'message':'Ingrediente creado exitosamente',
                'success': True,
                'data': request.get_json(),
                'ingrediente': ingrediente_serializado
            }, 201
        except ValidationError as ex:
            return{
                'message':'La informacion es incorrecta',
                'error': ex.args,
                'success': False,
            }, 400
        except Exception as ex:
            conexion.session.rollback() #rpara deshacer la transaccion
            return{
                'message':'Hubo un error al crear el ingrediente',
                'error': ex.args,
                'success': False,
                'data': request.get_json()
            }, 500

class PruebaController(Resource):
    def post(self):
        try:
            #validar entradas
            data = request.get_json()
            validacion = ValidadorPrueba().load(data)
            print(validacion)
            return {
                'message':'Ok',
                'data':validacion
            }
        except Exception as ex:
            return {
                'message': 'Error al recibir los tags',
                'error': ex.args
            }

    
    def get(self):
        usuario = {
            'nombre':'juan',
            'apellido': 'ramoz',
            'nacionalidad': 'peruano',
            "password":"123"
        }

        resultado = ValidadorUsuarioPrueba().dump(usuario)

        return {
            'message': 'Usuario',
            'data': resultado
        }