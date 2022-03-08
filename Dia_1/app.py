from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

clientes = []

@app.route('/')
def estado():
    hora_del_servidor = datetime.now()
    return{
        'status':True,
        'hour': hora_del_servidor.strftime('%Y/%m/%d %H:%M:%S')
    }

@app.route('/clientes', methods=['POST'])
def get_clientes():
    # print(request.method)
    # print(request.data)
    # print(request.get_json())
    data = request.get_json()
    print(clientes)
    clientes.append(data)
    
    return{
        'success':True,
        'message':'Cliente agregado exitosamente',
        'client':data
    }

app.run(debug=True)