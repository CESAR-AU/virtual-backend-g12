from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def inicio():
    # render_template > renderiza un archivo .html o .jinja
    data = {
        'nombre':'Juan',
        'dia':'Jueves',
        'integrantes':['Foca', 'Lapagol', 'Ruidiaz', 'Paolin', 'Rayo Advincula'],
        'usuario':{
            'nombre':'Luis',
            'direccion':'Los tulipanes 123',
            'edad': 40
        },
        'selecciones':[{
            'nombre':'Bolivia',
            'clasificado':False
        },
        {
            'nombre':'Brasil',
            'clasificado':True
        },
        {
            'nombre':'Chile',
            'clasificado':False
        },
        {
            'nombre':'Peru',
            'timado':True
        }]
    }
    return render_template('inicio.jinja', **data)

if(__name__ == '__main__'):
    app.run(debug=True)