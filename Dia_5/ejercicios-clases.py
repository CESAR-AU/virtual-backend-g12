# crear una clase Persona en la cual se guarden su nombre, fecha_nacimiento, nacionalidad, dni, ademas tambien una clase Alumno y una clase Docente en la cual el alumno , a diferencia del docente, tenga una serie de cursos matriculados, y el docente por su parte tenga un numero del seguro social y su cuenta de la CTS. En base a lo visto de herencia codificar las clases y ademas ver si hay algun atributo o metodo que deba de ser privado.

class Persona:
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni):
        self.nombre = nombre,
        self.fecha_nacimiento = fecha_nacimiento,
        self.nacionalidad = nacionalidad,
        self.dni = dni,
        self.__fecha_ingreso = ''
        self.__respuesta = {}

    def saludar(self):
        return 'Hola, soy {}'.format(self.nombre)
    
    def get_info(self):
        # self.__respuesta['nombre'] = self.nombre
        # self.__respuesta['fecha_nacimiento'] = self.fecha_nacimiento
        # self.__respuesta['nacionalidad'] = self.nacionalidad
        # self.__respuesta['dni'] = self.dni
        # self.__respuesta['fecha_ingreso'] = self.__fecha_ingreso
        return{
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento,
            'nacionalidad': self.nacionalidad,
            'dni': self.dni,
            'fecha_ingreso': self.__fecha_ingreso,
        }

class Alumno(Persona):
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni, cursos):
        super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)
        self.cursos = cursos
    
    def get_info(self):
        respuesta = super().get_info()        
        respuesta['cursos'] = self.cursos
        return respuesta

class Docente(Persona):
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni, seguro_social, cuenta_cts):
        super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)
        self.seguro_social = seguro_social
        self.cuenta_cts = cuenta_cts
    
    def get_info(self):
        respuesta = super().get_info()
        respuesta['seguro_social'] = self.seguro_social
        respuesta['cuenta_cts'] = self.cuenta_cts
        return respuesta

profe = Docente(
    nombre='Eduardo', fecha_nacimiento='1985-04-16', nacionalidad='Peruano', 
    dni='42516325', seguro_social='123456', cuenta_cts='123456789')

print(profe.get_info())

alumno1 = Alumno(
    nombre='Juan', fecha_nacimiento='2000-05-20', nacionalidad='Peruano', dni='85654525',
    cursos=[
        {'curso':'Literatura',
        'docente':'Eduardo',
        'horario':{
            'lunes':'9:00 am - 10:00 am',
            'martes':'9:00 am - 10:00 am',
            'miercoles':'9:00 am - 10:00 am',
            'jueves':'9:00 am - 10:00 am',
            'viernes':'9:00 am - 10:00 am',
            }
        },
        {'curso':'Matematica',
        'docente':'Pedro',
        'horario':{
            'lunes':'10:30 am - 12:00 am',
            'martes':'10:30 am - 12:00 am',
            'miercoles':'10:30 am - 12:00 am',
            'jueves':'10:30 am - 12:00 am',
            'viernes':'10:30 am - 12:00 am',
            }
        },
    ]
)

print(alumno1.get_info())
