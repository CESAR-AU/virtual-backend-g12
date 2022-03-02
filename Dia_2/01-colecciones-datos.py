#listas
nombre = ['Pedro', 'luis', 'Danny', 'Cesar', 'Magaly']
conbinada = ['Juan', 80, False, 15.20, [1,2,3]]

#0
print(nombre[0])
print(nombre[-1])
print(nombre)

res = nombre.pop() #elimina el ultimo elemento
print(res)
print(nombre)

nombre.append('Daniela')
print(nombre)

del nombre[0]
print(nombre)

nombre.clear()
print(nombre)

print(id(nombre))
#del nombre
#print(id(nombre))

x = conbinada[:]
y = conbinada
b = conbinada.copy()
print(conbinada[1:3])
print(id(conbinada))
print(id(x))
print(id(y))
print(id(b))

print(conbinada[:2])
print(conbinada[2:])

meses_desc = ['Enero', 'Marzo', 'Julio']
mes = 'Septiembre'
mes2 = 'Enero'
print(mes in meses_desc)
print(mes2 in meses_desc)
print(mes2 not in meses_desc)

a = ['Juan', 'Rosa']
b = ['Eder', 'Maria']
print(a + b)

#dato = input('Ingresa tu nombre: ')
#print('Tu nombre es: {}'.format(dato))

#tuplas
cursos = ('backend', 'frontend')
d = cursos[:]
print(cursos)
print(d)

variada = (1,2,3, [5,6,7])
print(variada)
variada[3][0] = 'Hola'
print(variada)
print(2 in variada)

variada_list = list(variada)
print(variada_list)

print(len(variada_list))

#conjunto
estaciones = {'verano', 'otoño', 'primavera', 'invierno'}
print(estaciones)
estaciones.add('Otro')
print(estaciones)
estacion = estaciones.pop()
print(estacion)

#diccionarios
persona={
    'nombre':'Juan',
    'apellido':'Ramos',
    'direcciones':{
        'ubigeo':'04004'
    }
}
print(persona.get('apellido'))
print(persona.get('apellidos', 'No existe, verifique'))
print(persona['direcciones']['ubigeo'])
print(persona.keys())
persona['edad'] = 25
persona['Nombre'] = 'Julian'
print(persona)
print(persona.values())
print((persona['direcciones'].keys()) in 'otros')
print(persona.items())