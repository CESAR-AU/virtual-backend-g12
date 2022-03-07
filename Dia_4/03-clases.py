#
from hashlib import new


class Persona:
    #Propiedade
    fec_nac = '2000-01-01'
    nombre = 'Juan'
    soltero = True

    #Metodos
    def saludar(self):
        print('Hola como estas', self.nombre)
        self.decir_nombre()
        return 'Hola {}'.format(self.nombre)

    def decir_nombre(self):
        print('Mi nombre es: ', self.nombre)

persona1 = Persona()
persona1.nombre = 'Luis'
persona2 = Persona()

Persona.nombre = 'Rick'
Persona().saludar()

persona1.saludar()
print(persona1)
print(persona1.nombre)