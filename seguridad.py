from bcrypt import checkpw
from config import conexion
from models.usuarios import ModelUsuario

def autenticador(username, password):
    '''Funcion encargada de validar si las credencialesson correctas'''
    # 1 > valido si los parametros son correctos
    if username and password:
        # busco el usuario en la db
        usuario_encontrado : ModelUsuario | None = conexion.session.query(ModelUsuario).filter_by(correo = username).first()
        if usuario_encontrado:
            print('Se encontro al usuario')
            # validar las contraseña
            validacion = checkpw(bytes(password, 'utf-8'), bytes(usuario_encontrado.password, 'utf-8'))
            if validacion:
                print('Se encontro al usuario y si la contraseña')
                return usuario_encontrado
            else:
                return None
        else:
            return None
    else:
        None

def identificador(payload):
    '''Sirve para validar al usuario previamente autenticado'''
    print('INDENTIFICADOR',payload)
    usuario_encontrado : ModelUsuario | None = conexion.session.query(ModelUsuario).filter_by(id = payload['identity']).first()
    if usuario_encontrado:
        return usuario_encontrado
    else:
        return None