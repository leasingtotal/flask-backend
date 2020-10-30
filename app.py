from flask import Flask, render_template, request,jsonify
from flask_cors import CORS, cross_origin

from funciones import validar_usuarios,crear_usuario,datos_tabla

app = Flask(__name__)
app.config['SECRET_KEY'] = 'faasdasdf1231asdad123'

@app.route("/")
@cross_origin()
def index():
    return render_template('index.html')

@app.route("/login",methods=['POST'])
@cross_origin()
def login():
    try:
        data = request.get_json()
        usuario = data['usuario']
        clave = data['clave']
        
        resultado = validar_usuarios(usuario,clave)
        return jsonify(resultado)
    except Exception as e:
        error = [{
            "status":"400",
            "detalle":"Ha ocurrido un error en el endpoint: " +str(e)
        }]
        return jsonify(error)

@app.route("/registro", methods=['PUT'])
@cross_origin()
def registro():
    try:
        data = request.get_json()
        usuario = data['usuario']
        clave = data['clave']
        nombre = data['nombre']
        mail = data['email']
        print(usuario, clave, nombre)
        resultado = crear_usuario(usuario, clave, nombre,mail)
        return jsonify(resultado)

    except Exception as e:
        error = [{
            "status":"400",
            "detalle":"Ha ocurrido un error en el endpoint: " +str(e)
        }]
        return jsonify(error)

@app.route("/tabla", methods=['GET'])
@cross_origin()
def tabla():
    try:
        retorno = datos_tabla()
        return jsonify(retorno)

    except Exception as e:
        error = f"Ha ocurrido un error {e}"
        return error


if __name__=='__main__':
    app.run(host='10.50.1.137', port=3434, debug=True)