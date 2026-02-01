from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que Netlify pueda enviar datos a tu backend

@app.route("/api/enviar", methods=["POST"])
def enviar():
    datos = request.get_json()
    nombre = datos.get("nombre")
    email = datos.get("email")
    mensaje = datos.get("mensaje")

    print("Nuevo mensaje recibido:")
    print("Nombre:", nombre)
    print("Email:", email)
    print("Mensaje:", mensaje)

    # Aquí puedes poner tu función de enviar email si quieres
    return "Mensaje recibido correctamente"

if __name__ == "__main__":
    app.run()
