#DFU Funciones Definidas por el Usuario
from itertools import product
from math import fabs
from operator import truediv


def sumar(numero1, numero2):
    '''Funcion q recibe 2 emteros y lo imprime por consola sumado'''
    print('Sumado: {}'.format(numero1+numero2))
sumar(1,5)
print(sumar.__doc__)

#
usuarios = []
def registrar(nombre, email, telefono):
    '''Funcion para registrar un usuario y lo guarda en una lista'''
    usuarios.append({
        'nombre': nombre,
        'email': email,
        'telefono':telefono
    })
    return{
        'message':'Usuario registrado',
        'usuario': usuarios[0]
    },1,True


usuario, num, booleano = registrar('Juan', 'juan@c-innoa.pe', '951258456')
print('usuario: {}, numero: {}, booleano: {}'.format(usuario, num, booleano))

productos = []
def registrar_producto(nombre, precio, estado=True, almacen='Almacen del cercado'):
    productos.append({
        'nombre':nombre,
        'precio':precio,
        'estado':estado,
        'almacen':almacen
    })
    return 'Producto registrado exitosamente'

registrar_producto('Tomate', 4.50)
registrar_producto('Apio', 1.40, False)
registrar_producto('Cebolla', 5.00, True, 'Almacen avelino')
registrar_producto(almacen='Almaccen nuevo', precio=2.40, estado=True, nombre='Pescado tilapia')
for producto in productos:
    print('Producto: {}, Precio: {}'.format(producto['nombre'], producto['precio']))

def alumnos(clases, *args):
    print(args)
    print('La clase es: ',clases)

alumnos('grupo12', 'eduardo', 'nahia', 'pedro')
alumnos('frontend', 'eduardo', 'roxana', 'luis')
alumnos('marta', 30, False, 'Juan', 1.50)

def ingresarProducto(**kwargs):
    print(kwargs)
    if(kwargs.get('nombre')):
        print('El usuario quiere agregar un producto')
    if(kwargs.get('cantidad')):
        print('El usuario quiere agregar la cantidad de un producto')

ingresarProducto(nombre='Manzana', precio=2.40, estado=True)
ingresarProducto(tamanio='Manzana', cantidad=2.40, nombre='True')

#recurcibidad
def saludar_n_veces(limite):
    if(limite==0):
        return 'Llego al limite'
    print('Hola...', limite)
    return saludar_n_veces(limite-1)

resultado = saludar_n_veces(10)
print(resultado)

def factorial(limite):
    if limite == 0:
        return 1
    return limite * factorial(limite-1)
resultado = factorial(3)
print(resultado)

nombre_persona = 'Maria'
origen_persona = 'Arequipa'
resultado = 'Me caso' if nombre_persona == 'Maria' and origen_persona == 'Arequipa' else 'Next'
print(resultado)

#LAMBDA FUNCTION
cuadrado = lambda numero: numero **2
print(cuadrado(4))

sacar_igv = lambda precio: precio / 1.18
print(sacar_igv(100))