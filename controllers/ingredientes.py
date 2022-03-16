from flask_restful import Resource, request
from config import conexion
from models.ingredientes import Ingrediente

class IngredientesController(Resource):
    def get(self):
        resultado = conexion.session.query(Ingrediente).all()
        print(resultado)
        return{
            'message':'Ingredientes',
            'success': True,
            'data': resultado[0].nombre
        }, 200
    
    def post(self):
        print(request.get_json())
        try:
            nuevoIngrediente = Ingrediente()
            nuevoIngrediente.nombre = 'Leche evaporada'
            conexion.session.add(nuevoIngrediente) #nueva transaccion
            conexion.session.commit()
            
            return{
                'message':'Ingrediente creado exitosamente',
                'success': True,
                'data': request.get_json()
            }, 200
        except Exception as ex:
            conexion.session.rollback() #rpara deshacer la transaccion
            return{
                'message':'Hubo un error al crear el ingrediente Error: {}'.format(ex),
                'success': False,
                'data': request.get_json()
            }, 400