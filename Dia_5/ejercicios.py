# para evitar el salto de linea en una impresion de pantalla print() podemos declarar un parametro end=''
# print('hola',end='*')
# print('estos son los ejercicios')
# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
# dibujar_rectangulo()


def dibujar_rectangulo(altura, ancho, char='*'):
    for alt in range(altura):
        print('{}'.format(char) * ancho)
#dibujar_rectangulo(5, 50, '*')

# Escribir una funcion que nosotros le ingresemos el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
# dibujar_octagono()
def dibujar_octagono(grosor=5, char = '*'):
    if(len(char) > 1): char = char[0]
    for base in range(grosor):
        print_char = (grosor + (base * 2))
        print('{}{}'.format((' ' * (grosor - base - 1)), (char * print_char)))

    for base in range(1,grosor):
        print_char = (grosor + (grosor - 1) * 2)
        print(char * print_char)

    for base in range(grosor-1):
        print_char = ((grosor - base + 1 ) * 2 ) - 1
        print('{}{}'.format((' ' * (base + 1 )), (char * print_char)))

        ejeX = 8 + grosor
    '''for altura in range(0,ejeX,2):
        print_char = (grosor + altura)
        espacios = int((ejeX - print_char) / 2)
        print('{}{}'.format((' '*espacios),('*'*print_char)))

        if(print_char == ejeX):
            for alt in range(0,grosor,2):
                print('*' * print_char)'''

dibujar_octagono(5, '|')

# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# serie_collatz()
respuesta = { 'numeros':[], 'pares':0, 'impares':0, 'saltos': 0}
def serie_collatz(number):  
    try:
        number = int(number)
        #respuesta['numeros'].append(number)
        if(number == 1): return respuesta

        if((number%2) == 0):
            number /= 2
            respuesta['pares'] +=1
        else:  
            number = (number * 3) + 1
            respuesta['impares'] +=1
        respuesta['numeros'].append(int(number))
        respuesta['saltos'] += 1
        return serie_collatz(number)
    except ValueError as ex:
        return 'Solo numeros\nError: {}'.format(ex)
    except Exception as ex:
        return 'Error: {}'.format(ex)

resultado = serie_collatz(input('Ingrese un numero: '))
print(resultado)

#demo