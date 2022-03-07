class Usuario:
    def __init__(self, nombre, apellido, correo) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
    
    def saludar(self):
        return 'Hola soy {}'.format(self.nombre)

class Alumno(Usuario):
    def __init__(self, nombre, apellido, correo, padres) -> None:
        super().__init__(nombre, apellido, correo)
        self.padres = padres

    def info(self):
        return{
            'nombre':self.nombre,
            'apellido':self.apellido,
            'correo':self.correo,
            'padres':self.padres,
            'saludar': super().saludar()
        }

alumno1 = Alumno('Juan', 'Ramos', 'ad@sds.ox', [
    {
    'nombre':'wilber',
    'apellido':'Martinez'
    },
    {
    'nombre':'Juliana',
    'apellido':'Perez'
    },
])
print(alumno1.info())