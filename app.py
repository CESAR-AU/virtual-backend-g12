from datetime import datetime
from flask import Flask
from flask_restful import Api

from controllers.ingredientes import IngredientesController
from controllers.usuario import UsuariosController

app = Flask(__name__)
api = Api(app=app)

@app.route('/status', methods=['GET'])
def status():
    return {'satatus':True, 'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, 200

api.add_resource(IngredientesController, '/ingredientes', '/ingrediente')

api.add_resource(UsuariosController, '/usuarios')


if __name__ == '__main__':
    app.run(debug=True, port=8080)