from datetime import datetime
from flask import Flask, request
from flask_restful import Api

from controllers.ingredientes import IngredientesController, PruebaController
from controllers.usuario import UsuariosController
from config import conexion, validador

app = Flask(__name__)
api = Api(app=app)

# print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:amigos@127.0.0.1:3307/recetario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
conexion.init_app(app)
validador.init_app(app=app)
conexion.create_all(app=app)

@app.route('/status', methods=['GET'])
def status():
    return {'satatus':True, 'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, 200

@app.route('/', methods=['GET'])
def inicio():
    return {'message':'Bienvenido a mi API de recetas'}, 200

api.add_resource(IngredientesController, '/ingredientes', '/ingrediente')

api.add_resource(UsuariosController, '/usuarios')

api.add_resource(PruebaController, '/pruebas')


if __name__ == '__main__':
    app.run(debug=True, port=5000)