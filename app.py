from flask import Flask

app = Flask(__name__)

@app.route('/') #(decoradores)ruta dentro de la carpeta working directory donde se encontrará la pág web
def index():
    return "Hola mundo"

if __name__ == "__main__":
    app.run()