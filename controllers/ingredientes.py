from flask_restful import Resource, request

class IngredientesController(Resource):
    def get(self):
        return{
            'message':'Ingredientes',
            'success': True
        }, 200
    
    def post(self):
        print(request.get_json())
        return{
            'message':'POST',
            'success': True,
            'data': request.get_json()
        }, 200