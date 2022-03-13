from faker import Faker
from faker.providers import internet, person

fake = Faker()
fake.add_provider({internet, person})

def generar_alumnos(limite):
    persona = {
    'nombre' : '',
    'apellido_paterno' : '',
    'apellido_materno' : '',
    'correo' : '' ,
    'numero_emergencia' : ''
    }

    persona['nombre'] = fake.name()
    persona['apellido_paterno'] = fake.first_name()
    persona['apellido_materno'] = fake.last_name()
    persona['correo'] = fake.ascii_free_email()
    # persona['numero_emergencia'] = fake.phone_number()
    persona['numero_emergencia'] = fake.bothify(text='9########')


    print(persona)

    for rango in range(limite):
        persona['nombre'] = fake.name()
        persona['apellido_paterno'] = fake.first_name()
        persona['apellido_materno'] = fake.last_name()
        persona['correo'] = fake.ascii_free_email()
        persona['numero_emergencia'] = fake.bothify(text='9########')

        sql = ''' INSERT INTO tbl_alumnos (nombre, apellido_paterno, apellido_materno, correo, numero_emergencia) VALUES
        ('%s', '%s', '%s', '%s', '%s');''' % (persona['nombre'], persona['apellido_paterno'], persona['apellido_materno'], persona['correo'], persona['numero_emergencia'])
        print(sql)

def generar_secciones():
    secciones = ['A', 'B', 'C']
    ubicaciones = ['Sotano', 'Primer piso', 'Segundo piso', 'Tercer piso']
    niveles = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto']
    for nivel in niveles:
        nro_secciones = fake.random_int(min=2,max=3)
        for posicion in range(0,nro_secciones):
            nro_ubicacion = fake.random_int(min=0,max=3)
            sql = ''' INSERT INTO tbl_niveles (seccion, ubicacion, nombre) VALUES ('%s', '%s', '%s'); ''' % (secciones[posicion], ubicaciones[nro_ubicacion], nivel)
            print(sql)
            # print('Nivel: {} Seccion: {} Ubicacion: {}'.format(nivel, secciones[posicion], ubicaciones[nro_ubicacion]))

def generar_niveles_alumnos(cantidad):
    # generar un numero aleatorio que sera el id del alumno y el id del nivel y un anio de manera en la cual no se puede volver a generar ese mismo alumno con un nivel inferior pero con un anio superior
    # ALUMNO_ID    NIVEL_ID    YEAR
    #     1            1        1999   // 1 > primero A ✔️
    #     1            1        2002   // 1 > primero A ❌
    #     1            3        2000   // 3 > segundo A 
    # en total tiene que haber unos 80 registros
    id_alumnos = []
    rango_id_nivel = (1, 17)
    def get_id_niveles(cursando):
        nivel_id = fake.random_int(rango_id_nivel[0], rango_id_nivel[1])
        id_niveles = []
        for nivel in range(0, cursando):
            if nivel == 0: id_niveles.append(nivel_id)
            else: 
                nivel_id += fake.random_int(2, 3)
                id_niveles.append((nivel_id))
        return id_niveles
    
    def get_anios(cursando):
        anio_inicio = fake.random_int(2000, 2022) - cursando 
        anios = []
        for nivel in range(cursando): anios.append(anio_inicio + nivel)
        return anios
    
    def get_id_alumno():
        alumno_id = fake.random_int(1, 100)
        while alumno_id in id_alumnos:
            #print('ID Repetido:',alumno_id)
            alumno_id = fake.random_int(1, 100)
            #print('Nuevo ID:',alumno_id)
        id_alumnos.append(alumno_id)
        return alumno_id

    for nro in range(cantidad):
        cursando = fake.random_int(1, 6)
        alumno_id = get_id_alumno()

        anios = get_anios(cursando=cursando)
        niveles = get_id_niveles(cursando)
        for posicion in range(len(niveles)):
            if niveles[posicion] <= rango_id_nivel[1]:
                sql = ''' INSERT INTO tbl_alumnos_niveles (fecha_cursada, alumnos_id, nivel_id) VALUES (%s, %s, %s); ''' % (anios[posicion], alumno_id, niveles[posicion])
                #print('ID Alumno: {}, ID Nivel: {}, Año: {}'.format(alumno_id, niveles[posicion], anios[posicion] ))
                print(sql)
        #print('ID Alumno: {}, ID Nivel: {}, Año: {}'.format(alumno_id, niveles, anios ))

#py simulador.py > nombre_archivo_salida
#generar_alumnos(100)
#generar_secciones()
generar_niveles_alumnos(80)