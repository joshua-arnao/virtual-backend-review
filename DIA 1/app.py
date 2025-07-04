from flask import Flask, request
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app, origins='http://127.0.0.1:5000/')

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


def search_usr(id):
    # v1
    # for client in clients:
    #     if client.get('id') == id:
    #         return client
    # v2
    for position in range(0, len(clients)):
        client = clients[position]
        if client.get('id') == id:
            print(f'Posición: {position}')
            return (client, position)


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


@app.route('/client/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_client(id):
    if request.method == 'GET':
        usr = search_usr(id)
        # is usr is not None:
        if usr:
            return usr[0]
        else:
            return ({
                'message': 'El usuario a buscar no se encontro'
            }, 404)

    elif request.method == 'PUT':
        result = search_usr(id)
        if result:
            [client, position] = result
            data = request.get_json()
            data['id'] = id
            clients[position] = data

            return data

        else:
            return {
                'message': 'El cliente a modificar no se encontro'
            }, 404

    elif request.method == 'DELETE':
        result = search_usr(id)
        if result:
            [client, position] = result
            client_delete = clients.pop(position)

            return {
                'message': 'Cliente eliminado satisfactoriamente',
                'client': client_delete
            }
        else:
            return {
                'message': 'El cliente a eliminar no se encontro'
            }, 404


app.run(debug=True)
