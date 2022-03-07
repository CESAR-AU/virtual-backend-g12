class Producto:
    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio
        #Privado
        self.__ganancia = self.precio * 0.30

    def mostrar_info(self):
        return{'nombre':self.nombre, 'precio':self.precio, 'ganancia':self.__ganancia, 'igv': self.__calcular_igv()}
    
    def aumnetar_ganancia(self):
        self.__ganancia = self.__ganancia * 1.10
    
    def __calcular_igv(self):
        resultado = '{:.2f}'.format(self.precio / 0.18)
        return float(resultado)

cepillo = Producto('Cepillo dental', 3.50)
cepillo.nombre
#cepillo.__ganancia = 0
print(cepillo.mostrar_info())
print(cepillo.aumnetar_ganancia())
print(cepillo.mostrar_info())