import subprocess
from flask import Flask, request 
app = Flask(__name__)
@app.route('/')
def index():
    return '¡Hola, mundo!'
@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    comando = request.form['comando']
    resultado = subprocess.check_output(comando, shell=True)
    return resultado.decode()

if __name__ == '__main__':
    app.run(debug=True)