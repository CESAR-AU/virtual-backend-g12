from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#instancias unicas de las clases para no duplicar 
validador = Marshmallow()
conexion = SQLAlchemy()