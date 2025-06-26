from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

clients = [
    {
        "name": "Joshua",
        "country": "Peru",
        "age": 28,
        'id': 1
    }
]


@app.route('/')
def state():
    hora_del_servidor = datetime.now()
    return {
        'status': True,
        'hour': hora_del_servidor.strftime('%H:%M:%S')
    }


@app.route('/clients', methods=['POST', 'GET'])
def get_clients():
    print(request.method)
    print(request.get_json())

    if request.method == 'POST':
        data = request.get_json()
        data['id'] = len(clients) + 1
        clients.append(data)

        return {
            'message': 'Cliente agregado exitosamente',
            'clients': data
        }
    elif request.method == 'GET':
        return {
            'message': ' La lista de clientes',
            'clients': clients
        }


@app.route('/client/<int:id>', methods=['GET'])
def get_id_client(id):
    print(id)
    return {
        'id': id
    }


app.run(debug=True)
