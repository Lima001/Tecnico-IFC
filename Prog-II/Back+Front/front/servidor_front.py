from flask import Flask, render_template
from modelo import Cachorro
import requests
from playhouse.shortcuts import dict_to_model

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Sistema Front --- CachorrosPY.   <a href=/listar_cachorros>Listar Cachorros</a>"

@app.route("/listar_cachorros")
def listar_cachorros():
    
    dados = requests.get('http://localhost:4999/listar_cachorros')
    json_dados = dados.json()
    lista_cachorros = []
    
    for c_json in json_dados['lista']:

        cachorro = dict_to_model(Cachorro, c_json)
        lista_cachorros.append(cachorro)

    return render_template("listar.html", lista=lista_cachorros)

app.run()