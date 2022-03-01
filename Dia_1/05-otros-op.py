#OPERADORES DE COMPARACION
n1,n2 = 10, 20
# = que

# Mayor que |

print(n1==n2)
print(n1>n2)
print(n1>=n2)
print(n1<n2)
print(n1<=n2)
print(n1!=n2)

print((10>5) and (10<20))
print((10>5) or (10<20))

verduras = ['apio', 'lechuga', 'zapallo']
verduras2 = verduras
verduras3 = ['apio', 'lechuga', 'zapallo']# ['brocoli', 'espinaca', 'zanahoria']

verduras2[0] = 'perejil'
verduras[1] = 'mazana'

#
verduras4 = verduras.copy()
verduras4[0] = 'huatacay'

print(verduras2 is verduras)
print(verduras)
print(verduras2)
print(verduras3 is verduras)

print('Posicion de verduras es:', id(verduras))
print('Posicion de verduras2 es:', id(verduras2))
print('Posicion de verduras4 es:', id(verduras4))

#
nombre = 'juan'
nombre2 = nombre
print(nombre2 is nombre)
print(id(nombre2))
print(id(nombre))
nombre2 = 1
print(nombre)
print(nombre2)
print(id(nombre2))
print(id(nombre))

#validar si el nomkbre del usuario es = eduardo y nacionalidad = peruano o colombiano

nombre = 'eduardo'
nacionalidad = 'cubano'

print(nombre == 'eduardo' and (nacionalidad == 'peruano' or nacionalidad == 'colombiano'))