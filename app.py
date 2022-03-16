from datetime import datetime
from flask import Flask, request
from flask_restful import Api

from controllers.ingredientes import IngredientesController
from controllers.usuario import UsuariosController
from config import conexion

app = Flask(__name__)
api = Api(app=app)

# print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:amigos@127.0.0.1:3307/recetario'
conexion.init_app(app)
conexion.create_all(app=app)

@app.route('/status', methods=['GET'])
def status():
    return {'satatus':True, 'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, 200

@app.route('/', methods=['GET'])
def inicio():
    return {'message':'Bienvenido a mi API de recetas'}, 200

'''@app.route('/ruc', methods=['POST'])
def demo():
    try:
        ruc = request.get_json()
        ruta = 'https://dniruc.apisperu.com/api/v1/ruc/{}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InBhc3RlbGVyaWFzam9yZ2VAZ21haWwuY29tIn0.vUNQGoW2muXLfc5hHdD_2ZW9UbLhQgK9AMdaHC7B4DI'.format(ruc['ruc'])
        res = requests.get(ruta)
        return {'message':'Consulta RUC', 'consultar': ruc, 'data': res.json()}, 200
    except Exception as ex:
        return {'message':'Error: {}'.format(ex)}, 400'''

api.add_resource(IngredientesController, '/ingredientes', '/ingrediente')

api.add_resource(UsuariosController, '/usuarios')


if __name__ == '__main__':
    app.run(debug=True, port=5000)