from flask import Flask
from datetime import datetime

# __name__ : Muestra si el archivo es el archivo raíz o principal del proyecto, si el archivo en el archivos principal entonces el valor de __name__ será __main__
# print(__name__)
app = Flask(__name__)

# @: Es un decorador, patron de software que se utiliza para modificar un funcionamiento de un metodo o clases en aprticular sin la necesidad de emplear otros metodos como la herencia
# route() metodo


@app.route('/')
def start():
    print('Me llamaron!')

    # Siempre en los controladores tenemos que devolver una respuesta
    return 'Bienvenido a mi API 🔌'


@app.route('/api/info')
def info_app():
    return {
        # strftime: para dar formato de fecha
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }


# debuggin: Estamos en modo prueba y con ello cada vez que guardamos se reinciia el servidor automaticamente
app.run(debug=True)
