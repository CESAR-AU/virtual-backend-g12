#mientas que
numero = 0
while numero < 10:
    pass
    print(numero)
    numero += 1
    #break
else:
    print('El while termino bien')

# CON FOR
numeros =[1,5,16,28,234,67,29,18, 15 ]
pares, impares = 0,0

for numero in numeros:
    if((numero % 2) == 0): pares +=1
    else: impares +=1

print('Pares: {}, Impares {}'.format(pares, impares))
#CON WHILE
index = 0
pares, impares = 0,0
while index < len(numeros):
    if((numeros[index] % 2) == 0): pares +=1
    else: impares +=1
    index +=1
print('Pares: {}, Impares {}'.format(pares, impares))