from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

clients = []


@app.route('/')
def state():
    hora_del_servidor = datetime.now()
    return {
        'status': True,
        'hour': hora_del_servidor.strftime('%H:%M:%S')
    }


@app.route('/clients', methods=['POST'])
def get_clients():
    # request: Es llamado en cada controlador
    print(request.method)
    print(request.get_json())

    data = request.get_json()
    clients.append(data)

    return {
        'message': 'Cliente agregado exitosamente',
        'clients': data
    }


app.run(debug=True)
