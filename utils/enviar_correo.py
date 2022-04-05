from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
from utils.message import Message

class EnviarCorrreo():
    def __init__(self, correos, subject, contenido, tipo_contenido = 'plain') -> None:
        self.password_emisor = environ.get('EMAIL_PASSWORD')
        self.email_emisor = environ.get('EMAIL_EMISOR')

        self.correos = correos
        self.subject = subject
        self.contenido = contenido
        self.tipo_contenido = tipo_contenido

    def enviarPorSMTP(self):
        try:
            mensaje = MIMEMultipart()
            mensaje['Subject'] = self.subject

            #mensaje.attach(MIMEText(texto, 'plain'))
            mensaje.attach(MIMEText(self.contenido, self.tipo_contenido))
            # enviando TLS:587 o SSL:465 ZOHO
            emeisor_SMTP = SMTP('smtp.zoho.com', 587)
            emeisor_SMTP.starttls()
            emeisor_SMTP.login(self.email_emisor, self.password_emisor)
            emeisor_SMTP.sendmail(
                from_addr=self.email_emisor,
                to_addrs=self.correos,                    
                msg=mensaje.as_string()
            )
            emeisor_SMTP.quit()
            return Message.GetMessage(message='Correo enviado exitosamente', success=True)
        except Exception as ex:
            return Message.GetMessage(message='Hubo un error al enviar el correo', success=False, error=ex.args)
