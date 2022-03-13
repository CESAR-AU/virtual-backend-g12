from datetime import datetime
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(
    app=app, 
    origins=['http://localhost:5000', 'https://mi-pagina.pe', 'http://190.235.116.37:5500'],
    methods=['*'],
    allow_headers=['Content-Type']
    )

clientes = [
    {
        'id':1,
        "nombre": "Juan",
        "pais": "PERU",
        "edad": 29,
        "organos": True,
        "casado": False
    }
]

@app.route('/')
def estado():
    hora_del_servidor = datetime.now()
    return{
        'status':True,
        'hour': hora_del_servidor.strftime('%Y/%m/%d %H:%M:%S')
    }

@app.route('/clientes', methods=['POST', 'GET'])
@cross_origin(origins=['http://localhost:5000'])
def get_set_clientes():
    # print(request.method)
    # print(request.data)
    # print(request.get_json())
        
    if(request.method == 'POST'):
        data = request.get_json()
        data['id'] = len(clientes) + 1
        print(clientes)
        clientes.append(data)
        return{
            'success':True,
            'message':'Cliente agregado exitosamente',
            'client':data
        }
    else:
        return{
            'success':True,
            'message':'La lista de clientes',
            'clients':clientes
        }


@app.route('/cliente/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def get_cliente(id):
    respuesta = {'message':'Cliente no encontrado', 'success': False, 'data': {}}
    try:
        if request.method == 'GET':
            resultado = buscar_cliente(id)
            if resultado:
               return resultado[0]
            else:
                return {'message': 'El cliente no fue encontrado'}, 404
        elif request.method == 'PUT':
            resultado = buscar_cliente(id)
            if resultado:
                [cliente, posicion] = resultado
                data = request.get_json()
                data['id'] = id
                # posicion = resultado[1]
                clientes[posicion] = data
                return data
            else:
                return {'message': 'El cliente no fue encontrado'}, 404
        elif request.method == 'DELETE':
            resultado = buscar_cliente(id)
            if resultado:
                [cliente, posicion] = resultado
                clientes.pop(posicion)
                return resultado
            else:
                return {'message': 'El cliente no fue encontrado'}, 404


    except Exception as ex:
        respuesta['message'] = 'Error: {}'.format(ex)

    if respuesta['success']: return respuesta, 200
    else: return respuesta, 404

def buscar_cliente(id):
    # for cliente in clientes:
    #     if(id == cliente.get('id')):
    #         return cliente
    
    for posicion in range(0, len(clientes)):
        cliente = clientes[posicion]
        if(cliente.get('id') == id):
            return (cliente, posicion)

app.run(debug=True, port=8080, host='0.0.0.0')