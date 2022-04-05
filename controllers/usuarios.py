from email.mime.text import MIMEText
from flask_restful import Resource, request
from marshmallow import ValidationError
# from sendgrid.helpers.mail import Email, To, Content, Mail
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
import json

from config import conexion, sendgrid
from dtos.registro_dto import LogginDTO, RegistroDTO, UsuarioResponseDTO
from dtos.usuario_dto import ResetPasswordRequestDTO, ChangePasswordRequestDTO
from models.usuarios import ModelUsuario
from utils.message import Message
from utils.enviar_correo import EnviarCorrreo

class RegistroController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RegistroDTO().load(body)
            nuevo_usuario = ModelUsuario(**data)
            # generar un hash de la contraseña
            nuevo_usuario.encripta_pwr()
            conexion.session.add(nuevo_usuario)
            conexion.session.commit()
            respuesta = UsuarioResponseDTO().dump(nuevo_usuario)
            return Message.GetMessage(message='Usuarios registrado exitosamente', success=True, data=respuesta), 201
        except ValidationError as ex:
            return Message.GetMessage(message='Error en la informacion', success=False, error=ex.args), 400
        except Exception as ex:
            conexion.session.rollback()
            return Message.GetMessage(message='No se pudo registrar el usuario', success=False, error=ex.args), 500

class LogginController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = LogginDTO().load(body)
            return Message.GetMessage(message='Logeado', success=True, data=data), 200
        except ValidationError as ex:
            return Message.GetMessage(message='Credenciales incorrectas', success=False, error=ex.args), 400
        except Exception as ex:
            # conexion.session.rollback()
            return Message.GetMessage(message='No se pudo inisiar la sesion', success=False, error=ex.args), 500


class RecetPasswordController(Resource):
    def post(self):
        body = request.get_json()
        #----------------- UTILIZANDO LA LIBRERIA DE PYTHON ------------------------------
        try:
            # Con la libreria propia de PY
            mensaje = MIMEMultipart()
            password_emisor = environ.get('EMAIL_PASSWORD')
            email_emisor = environ.get('EMAIL_EMISOR')

            data = ResetPasswordRequestDTO().load(body)
            usuario_encontrado : ModelUsuario  = conexion.session.query(ModelUsuario).filter_by(correo = data.get('correo')).first()
            if usuario_encontrado is not None:
                texto = 'Hola, has solicitado el reinicio de tu contraseña, haz click en el siguiente link para cambiar, sino has sido tu ignora este mensaje: ....'
                mensaje['Subject'] = 'Reiniciar contraseña APP Monedero'

                # key = Fernet.generate_key()
                fernet = Fernet(environ.get('FERNET_SECRET_KEY'))
                print('1111111111111111111111111111111111111111', environ.get('FERNET_SECRET_KEY'))
                mensaje_secreto = {
                    'fecha_inicial': str(datetime.now() + timedelta(hours=1)),
                    'fecha_caducidad': str(datetime.now() + timedelta(hours=2)),
                    'id_usuario':usuario_encontrado.id
                }
                mensaje_secreto_str = json.dumps(mensaje_secreto)
                mensaje_encriptado = fernet.encrypt(bytes(mensaje_secreto_str, 'utf-8'))

                with open("templates/email/forgot_password2.html") as f:
                    texto = f.read()
                html = texto.format(usuario_encontrado.nombre, (environ.get('URL_FRONT')+'/nueva-contra?token='+mensaje_encriptado.decode('utf-8')))
                #mensaje.attach(MIMEText(texto, 'plain'))
                mensaje.attach(MIMEText(html, 'html'))
                # enviando TLS:587 o SSL:465 ZOHO
                emeisor_SMTP = SMTP('smtp.zoho.com', 587)
                emeisor_SMTP.starttls()
                emeisor_SMTP.login(email_emisor, password_emisor)
                emeisor_SMTP.sendmail(
                    from_addr=email_emisor,
                    to_addrs=[usuario_encontrado.correo],                    
                    msg=mensaje.as_string()
                )
                emeisor_SMTP.quit()
                print('Correo enviado exitosamente')
            else:
                print('No se pudo enviar correo')
            return Message.GetMessage(message='Correo enviado exitosamente', success=True, data=data), 200
        except Exception as ex:
            return Message.GetMessage(message='Hubo un error al enviar el correo para recetear la password', success=False, error=ex.args), 400

        #----------------- UTILIZANDO LA LIBRERIA DE SENDGRID ------------------------------
        '''try:
            # Envio de correo mediante SENDGRID
            data = ResetPasswordRequestDTO().load(body)
            usuario_encontrado : ModelUsuario  = conexion.session.query(ModelUsuario).filter_by(correo = data.get('correo')).first()
            if usuario_encontrado is not None:
                from_email = Email('no-reply-innova@hotmail.com')
                to_email = To(usuario_encontrado.correo)
                # to_email = To('cesarmf@c-innova.pe')
                subject = 'Reinicia tu contraseña del Monedero'
                content = Content('text/plain', 'Hola, has solicitado el reinicio de tu contraseña, haz click en el siguiente link para cambiar, sino has sido tu ignora este mensaje: ....')
                mail = Mail(from_email, to_email, subject, content)
                enviar_correo = sendgrid.client.mail.send.post(request_body=mail.get())

                print('Correo enviado')
                print(enviar_correo.status_code)
                print(enviar_correo.body)
                print(enviar_correo.headers)
            else:
                print('No se pudo enviar correo')
            return Message.GetMessage(message='Correo enviado exitosamente', success=True), 200
        except Exception as ex:
            return Message.GetMessage(message='Hubo un error al recetear la password', success=False, error=ex.args), 500 '''
                
class ChangePasswordController(Resource):
    def put(self):
        try:
            body = request.get_json()
            data = ChangePasswordRequestDTO().load(body)
            fernet = Fernet(environ.get('FERNET_SECRET_KEY'))
            diccionario = json.loads(fernet.decrypt(bytes(data.get('token'), 'utf-8')).decode('utf-8'))
            fecha_caducidad = datetime.strptime(diccionario.get('fecha_caducidad'), "%Y-%m-%d %H:%M:%S.%f")
            if(datetime.now() <= fecha_caducidad):
                usuario_encontrado : ModelUsuario | None = conexion.session.query(ModelUsuario).filter_by(id = diccionario.get('id_usuario')).first()
                #usuario_encontrado : ModelUsuario | None = conexion.session.query(ModelUsuario).with_entities(ModelUsuario.id, ModelUsuario.password, ModelUsuario.correo).filter_by(id = diccionario.get('id_usuario')).first()
                if usuario_encontrado is not None:
                    usuario_encontrado.password = data.get('password')
                    usuario_encontrado.encripta_pwr()
                    conexion.session.commit()
                    resultado = UsuarioResponseDTO().dump(usuario_encontrado)
                    # 
                    texto = ''
                    with open("templates/email/change_password.html") as f:
                        texto = f.read()
                    html = texto.format(usuario_encontrado.nombre, usuario_encontrado.correo, (environ.get('URL_FRONT')+'/solicitar-nueva-contra'))

                    enviar_correo = EnviarCorrreo(usuario_encontrado.correo, 'APP Monedero | Contraseña modificado', html, 'html')
                    resultado_envio = enviar_correo.enviarPorSMTP()
                    print(resultado_envio)
                    return Message.GetMessage(message='Su contraseña fue modificado correctamente', success=True, data=resultado), 200
                else:
                    return Message.GetMessage(message='No fue posible modificar la contraseña', success=False), 404
            else:
                return Message.GetMessage(message='Su token ha caducado', success=False), 401
        except ValidationError as ex:
            return Message.GetMessage(message='Hubo un error en la info', success=False, error=ex.args), 401
        except Exception as ex:
            return Message.GetMessage(message='Hubo un error al recetear la password', success=False, error=ex.args), 401