from flask import Flask

app = Flask(__name__)

@app.get('/')
def inicio():
    return {
        "message": "API funcionando correctamente"
    }
