from flask import Flask, jsonify
from modelo import Cachorro
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route("/")
def iniciar():
    return "Estado: Operacional" + " <a href=/listar_cachorros>Dados</a>"

@app.route("/listar_cachorros")
def listar_cachorros():
    lista_cachorros = list(map(model_to_dict, Cachorro.select()))
    return jsonify({'lista':lista_cachorros})

app.run(port=4999)