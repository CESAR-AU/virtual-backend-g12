productoId = input('Ingrese el ID del producto: ')

try:
    if(productoId == '10'):
        raise Exception('El producto no se encuentra en la db')
except Exception as ex:
    print(ex.args[0])
else:
    print('Producto: {} encontrado'.format(productoId))
finally:
    print('Inicializando y liberando recursos')

print('Continuamos...')