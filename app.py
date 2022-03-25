from datetime import datetime
from flask import Flask, request
from flask_restful import Api
import requests

from controllers.ingredientes import (IngredientesController, PruebaController, IngredienteController)
from controllers.recetas import (BuscarRecetaController, RectasController, RecetaController)
from controllers.preparaciones import PreparacionesController
from controllers.ingredientes_recetas import IngredientesRecetasController
from controllers.usuario import UsuariosController
from config import conexion, validador
from dotenv import load_dotenv
from os import environ

load_dotenv()
# print(environ.get('NOMBRE'))

app = Flask(__name__)
api = Api(app=app)

# print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False
conexion.init_app(app)
validador.init_app(app=app)
conexion.create_all(app=app)

@app.route('/status', methods=['GET'])
def status():
    return {'satatus':True, 'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, 200

@app.route('/', methods=['GET'])
def inicio():
    f = open('./app_page.html')
    res = f.read()
    return res
    # return {'message':'Bienvenido a mi API de recetas'}, 200

api.add_resource(IngredientesController, '/ingredientes', '/ingrediente')
api.add_resource(IngredienteController, '/ingrediente/<int:id>')
api.add_resource(RectasController, '/recetas', '/receta')
api.add_resource(RecetaController, '/receta/<int:id>')
api.add_resource(BuscarRecetaController, '/buscar_receta')
api.add_resource(PreparacionesController, '/preparacion')
api.add_resource(IngredientesRecetasController, '/ingrediente_receta')

api.add_resource(UsuariosController, '/usuarios')

api.add_resource(PruebaController, '/pruebas')


if __name__ == '__main__':
    app.run(debug=True, port=5000)