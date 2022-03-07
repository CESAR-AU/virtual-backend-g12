#
#print(dir(locals()['__builtins__']))

from operator import truediv


try:
    valor = int(input('Ingrese un numero: '))
    print(valor)
except ValueError:
    print('Error al convertir un strin a un numero')
except Exception as error :
    print(error.args)
    print('Oops algo salio mal intentalo nuevamente')
print('Finalizado...')

while True:
    try:
        contra = int(input('Ingrese su codigo de acceso: '))
        if(contra == 123456) : break
        else : print('Codigo incorrecto')
    except:
        print('Codigo incorrecto')
print('Logeado...')

try:
    result = 1/1
    producto = None
    if(producto is None):
        raise Exception('El producto no existe en la db')
except Exception as ex:
    print(ex)
    print('Hubo un error')
else:
    print('Yo soy el else')
    print('El proceso finalizo sin errores')
finally:
    print('Yo me ejecuto siempre')