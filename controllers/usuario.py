from flask_restful import Resource, request

class UsuariosController(Resource):
    def get(self):
        return{
            'message':'Usuarios',
            'success': True
        }