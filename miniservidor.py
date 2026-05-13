from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# Necesario para que Flask entienda que Apache gestiona el SSL (HTTPS)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

@app.route("/")
def home():
    return "<h1>Servidor Flask Operativo</h1><p>Nodo: flask.jocarsa.com</p>"

if __name__ == "__main__":
    # En producción se lanza con Gunicorn, esto es para test local
    app.run(host="0.0.0.0", port=5000)