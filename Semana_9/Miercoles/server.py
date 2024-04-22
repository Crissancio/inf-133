from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

@app.route('/saludar', methods=['GET'])
def Saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere 'nombre' en los parámetros de la url"},400)
            )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route('/sumar', methods=['GET'])
def Sumar():
    num1 = (request.args.get("num1"))
    num2 = (request.args.get("num2"))
    if not num1 and not num2:
        return (
            jsonify({"error": "Se requiere valores en los parámetros de la url"},400)
            )
    elif not num1:
        return (
            jsonify({"error": "Se requiere 'num1' en los parámetros de la url"},400)
            )
    elif not num2:
        return (
            jsonify({"error": "Se requiere 'num2' en los parámetros de la url"},400)
            )
    return jsonify({"resultado": f"La suma de {num1} + {num2} es {int(num1)+int(num2)}"})

@app.route('/palindromo', methods=['GET'])
def Palindromo():
    cadena = request.args.get('cadena')
    if not cadena:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la url"},400)
            )
    cadena_invertida = cadena[::-1]
    if cadena == cadena_invertida:
        return jsonify({"respuesta":f"{cadena} es un palindromo"})
    else:
        return jsonify({"respuesta":f"{cadena} no es un palindromo"})

@app.route('/contar', methods=['GET'])
def contar():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")
    if not cadena and not vocal:
        return (
            jsonify({"error": "Se requiere una cadena y una vocal en los parámetros de la url"},400)
            )
    elif not cadena:
        return (
            jsonify({"error": "Se requiere 'cadena' en los parámetros de la url"},400)
            )
    elif not vocal:
        return (
            jsonify({"error": "Se requiere 'vocal' en los parámetros de la url"},400)
            )
    cont = cadena.count(vocal)
    return jsonify({"respuesta": f"hay {cont} vocales {vocal} en la cadena {cadena}"})


if __name__ == "__main__":
    app.run()