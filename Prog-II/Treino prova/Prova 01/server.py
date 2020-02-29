from flask import Flask, render_template, request
from carro import *

app = Flask("__name__")

@app.route("/")
def iniciar():
    return render_template("inicio.html")

@app.route("/listar_carros")
def listar_carros():
    return render_template("listar_carros.html", lista=lista_de_carros)

@app.route("/inserir_carro")
def inserir_carro():
    return render_template("inserir.html")

@app.route("/processar_inserir_carro")
def processar_inserir_carro():
    numero_serie = int(request.args.get("num_serie"))
    modelo = request.args.get("modelo")
    marca = request.args.get("marca")
    ano = int(request.args.get("ano"))

    cont = None
    for carro in lista_de_carros:
        if carro.numero_serie == numero_serie:
            cont = 0        
    if cont is None:
        lista_de_carros.append(Carro(numero_serie,modelo,marca,ano))
    return listar_carros()

@app.route("/processar_excluir_carro")
def processar_excluir_carro():
    numero_serie = int(request.args.get("num_serie"))

    indice = None
    for carro in lista_de_carros:
        if carro.numero_serie == numero_serie:
            indice = lista_de_carros.index(carro)
    
    lista_de_carros.pop(indice)
    return listar_carros()

app.run()