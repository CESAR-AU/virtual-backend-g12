from flask import Flask, render_template, request
from flask_restful import Api
from config import conexion, validador
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity
from seguridad import autenticador, identificador
from datetime import datetime, timedelta
from seed import categoriasSeed
from cryptography.fernet import Fernet
import json

from controllers.usuarios import (LogginController, RegistroController, UsuarioResponseDTO, RecetPasswordController, 
                                ModelUsuario, ChangePasswordController)
from controllers.movimientos import MovimientoController
from dtos.usuario_dto import ValidarTokenRequestDTO

load_dotenv()

app = Flask(__name__)

CORS(app=app)
#, origins=['http://127.0.0.1:3000','http://localhost:3000','http://127.0.0.1','https://miapp.vercel.app'], methods='*', allow_headers=['Content-Type']

# app.config['SECRET_KEY'] = 'holahola'
app.config['SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
app.config['JWT_AUTH_URL_RULE'] = '/login_jwt'
app.config['JWT_AUTH_USERNAME_KEY'] = 'correo'
# app.config['JWT_AUTH_PASSWORD_KEY'] = 'contra'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=1, minutes=5)
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'
jsonwebtoken = JWT(app=app, authentication_handler=autenticador, identity_handler=identificador)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app=app)
validador.init_app(app=app)
conexion.init_app(app=app)

conexion.create_all(app=app)

@app.before_first_request
def iniciarSeeds():
    print('Ejecutando seed..')
    categoriasSeed()

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

@app.route('/status')
def estado():
    return{
        'success':True,
        'hora_del_servidor': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }, 200

@app.route('/perfil')
@jwt_required()
def perfil_usuario():
    respuesta = UsuarioResponseDTO().dump(current_identity)
    return {
        'message': 'el usuario es: {}'.format(respuesta.get('nombre')),
        'data': respuesta
    }

@app.route('/validar-token', methods=['POST'])
def validar_token():
    body = request.get_json()
    try:
        data = ValidarTokenRequestDTO().load(body)
        fernet = Fernet(environ.get('FERNET_SECRET_KEY'))
        #desencriptado = fernet.decrypt(bytes(data.get('token'), 'utf-8')).decode('utf-8')
        diccionario = json.loads(fernet.decrypt(bytes(data.get('token'), 'utf-8')).decode('utf-8'))
        #print(diccionario)
        fecha_caducidad = datetime.strptime(diccionario.get('fecha_caducidad'), "%Y-%m-%d %H:%M:%S.%f")
        #hora_actual = datetime.now()
        if(datetime.now() <= fecha_caducidad):
            usuario_encontrado : ModelUsuario  = conexion.session.query(ModelUsuario).with_entities(ModelUsuario.correo).filter_by(id = diccionario.get('id_usuario')).first()
            if usuario_encontrado is not None:
                respuesta = UsuarioResponseDTO().dump(usuario_encontrado)
                return {
                    'message': 'Bien',
                    'success':True,
                    'data': {
                        'correo': respuesta.get('correo')
                    }
                }, 200
            else:
                return {
                    'message': 'Usuario no existe',
                    'success':False,
                }, 400
        else:            
            return {
                'message': 'La token caduco',
                'success':False
            }, 400
    except Exception as ex:
        return {
            'message': 'Ocurrio un error',
            'success':False,
            'error': ex.args
        }, 400

api.add_resource(RegistroController, '/registro')
api.add_resource(LogginController, '/loggin')
api.add_resource(RecetPasswordController, '/reset-password')
api.add_resource(ChangePasswordController, '/change-password')
api.add_resource(MovimientoController, '/movimiento', '/movimientos')

if(__name__ == '__main__'):
    app.run(debug=True)