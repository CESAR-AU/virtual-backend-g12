class Animal:
    # nombre = ''
    # sexo = ''
    # patas = 0

    def __init__(self, nombre, sexo, patas) -> None:
        self.nombre = nombre
        self.sexo = sexo
        self.patas = patas
    
    def descripcion(self):
        return 'Yo soy un {}, soy {}, y tengo {} patas'.format(self.nombre, self.sexo, self.patas)


foca = Animal('Foca', 'M', 2)
caballo = Animal('Caballo', 'M', 4)
gato = Animal('Gato', 'F', 4)

print(foca.descripcion())
print(caballo.descripcion())
print(gato.descripcion())