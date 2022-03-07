class Camelcase():
    def __init__(self, *args):
        '''Las palabras que ingrese en los argumentos (args) se omitiran al momento de la conversion'''
        self.__omitir = args
    
    def convertir(self, texto):
        '''Ingrese el texto a convertir a camelcase'''
        try:
            self.__omitir = self.__get_args()
            texto = texto.split(' ')
            salida = ''
            for palabra in texto:
                if((palabra.lower()) in self.__omitir): salida += palabra
                else: 
                    for posicion in range(len(palabra)):
                        if(posicion == 0): salida += palabra[posicion].upper()
                        else: salida += palabra[posicion].lower()
                salida += ' '
            return salida
        except Exception as ex:
            return 'No se pudo convertir.\nError: {}'.format(ex)
    
    def get_omitir(self):
        return self.__omitir

    def __get_args(self):
        res = []
        for palabra in self.__omitir: res.append((palabra.lower()))
        return res

cc = Camelcase('la', 'No', 'mundo')
print(cc.get_omitir())
# print(cc.convertir(input('Ingrese el texto a convertir a camellcase: ')))
print(cc.convertir('la menTe no tiene limites'))