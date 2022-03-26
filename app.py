from flask import Flask, render_template
from flask_restful import Api
from config import conexion, validador
from os import environ
from dotenv import load_dotenv

from controllers.usuarios import LogginController, RegistroController

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

api = Api(app=app)
validador.init_app(app=app)
conexion.init_app(app=app)

conexion.create_all(app=app)

@app.route('/')
def inicio():
    # render_template > renderiza un archivo .html o .jinja
    data = {
        'nombre':'Juan',
        'dia':'Jueves',
        'integrantes':['Foca', 'Lapagol', 'Ruidiaz', 'Paolin', 'Rayo Advincula'],
        'usuario':{
            'nombre':'Luis',
            'direccion':'Los tulipanes 123',
            'edad': 40
        },
        'selecciones':[{
            'nombre':'Bolivia',
            'clasificado':False
        },
        {
            'nombre':'Brasil',
            'clasificado':True
        },
        {
            'nombre':'Chile',
            'clasificado':False
        },
        {
            'nombre':'Peru',
            'timado':True
        }]
    }
    return render_template('inicio.jinja', **data)

api.add_resource(RegistroController, '/registro')
api.add_resource(LogginController, '/loggin')

if(__name__ == '__main__'):
    app.run(debug=True)