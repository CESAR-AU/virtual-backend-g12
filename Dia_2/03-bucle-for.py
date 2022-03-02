#BUCLE FOR
notas = [10, 20, 16, 6, 15]
for nota in notas:
    print('Nota: {}'.format(nota))

for numero in range(10):
    print(numero)
#inicio fin
for numero in range(5, 10):
    print(numero)
#inicio fin salto
for numero in range(5, 10, 2):
    print(numero)

for nota in notas[:3]:
    print('Nota: {}'.format(nota))

for nota in notas[len(notas)-3:]:
    print('Nota: {}'.format(nota))

for index in range(3):
    print('Nota: {}'.format(notas[index]))