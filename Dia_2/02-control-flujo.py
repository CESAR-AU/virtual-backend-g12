#
edad = int(input('Ingrese sus edad: '))
if (edad > 18):
    print('Mayor de eadad')
elif (edad > 15):
    print('Mayor de eadad de 15 y menor de 18')
else :
    print('Menor de edad')

print('Finalizo...')

#PRACTICA
# Validar si un numero (ingresos de una persona) ingresado por teclado es :
# * mayor a 500: indicar que no recibe el bono yanapay
# * entre 500 y 250: indicar que si recibe el bono
# * es menor que 250: indicar que recibe el bono y un balon de gas
# RESOLUCION DEL EJERCICIO

ingreso = int(input('Ingrese su ingreso mensual: '))
if (ingreso > 500):
    print('Ud. no recibe el bono yanapay')
elif (ingreso < 500 and ingreso > 250):
    print('Ud. si recibe el bono yanapay')
elif(ingreso > 250):
    print('Ud. si recibe el bono y un balon de gas')
else:
    print('Ud. no figura en el sistema')

