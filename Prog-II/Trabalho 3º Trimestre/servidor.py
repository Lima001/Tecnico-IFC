from flask import Flask, json, jsonify
from modelo import *
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return "Backend do Sistema de Missões Espaciais: <br><a href=/listar_missao>API Listar Missões</a>"+\
            "<br><a href=/listar_astronauta>API Listar Astronautas</a>" +\
            "<br><a href=/listar_treino>API Listar Treinos</a>" +\
            "<br><a href=/listar_treino_astronauta>API Listar Treinos Por Astronauta</a>"+\
            "<br><a href=/listar_central_terrestre>API Listar Centrais Terrestres</a>"+\
            "<br><a href=/listar_equipe>API Listar Equipes</a>"+\
            "<br><a href=/listar_nave>API Listar Naves</a>"+\
            "<br><a href=/listar_revisao_mecanica>API Listar Revisoes Por Nave</a>"+\
            "<br><a href=/listar_planeta>API Listar Planetas</a>"+\
            "<br><a href=/listar_base_planetaria>API Listar Bases Planetarias</a>"+\
            "<br><a href=/listar_tarefa>API Listar Tarefas</a>"+\
            "<br><a href=/listar_relatorio_missao>API Listar Relatorio da Missao -- Conclusao de Tarefas por Missao</a>"+\
             "<br><a href=/listar_ocorrencia>API Listar Ocorrencias</a>"

@app.route('/listar_missao')
def listar_missoes():
    missoes = list(map(model_to_dict, Missao.select()))
    return jsonify({"lista_missoes": missoes})

@app.route('/listar_astronauta')
def listar_astronautas():
    astronautas = list(map(model_to_dict, Astronauta.select()))
    return jsonify({"lista_astronautas": astronautas})

@app.route('/listar_treino')
def listar_treino():
    treinos = list(map(model_to_dict, Treino.select()))
    return jsonify({"lista_treinos": treinos})

@app.route('/listar_treino_astronauta')
def listar_treino_astronauta():
    treino_astronauta = list(map(model_to_dict, TreinoDoAstronauta.select()))
    return jsonify({"lista_treino_astronauta": treino_astronauta})

@app.route('/listar_central_terrestre')
def listar_central_terrestre():
    central_terrestre = list(map(model_to_dict, CentralTerrestre.select()))
    return jsonify({"lista_central_terrestre": central_terrestre})

@app.route('/listar_equipe')
def listar_equipe():
    equipe = list(map(model_to_dict, Equipe.select()))
    return jsonify({"lista_equipe": equipe})

@app.route('/listar_nave')
def listar_nave():
    nave = list(map(model_to_dict, Nave.select()))
    return jsonify({"lista_nave": nave})

@app.route('/listar_revisao_mecanica')
def listar_revisao_mecanica():
    revisao_mecanica = list(map(model_to_dict, RevisaoMecanica.select()))
    return jsonify({"lista_revisao_mecanica": revisao_mecanica})

@app.route('/listar_planeta')
def listar_planeta():
    planeta = list(map(model_to_dict, Planeta.select()))
    return jsonify({"lista_planeta": planeta})

@app.route('/listar_base_planetaria')
def listar_base_planetaria():
    base_planetaria = list(map(model_to_dict, BasePlanetaria.select()))
    return jsonify({"lista_base_planetaria": base_planetaria})

@app.route('/listar_tarefa')
def listar_tarefa():
    tarefa = list(map(model_to_dict, Tarefa.select()))
    return jsonify({"lista_tarefa": tarefa})

@app.route('/listar_relatorio_missao')
def listar_relatorio_missao():
    relatorio_missao = list(map(model_to_dict, RelatorioDaMissao.select()))
    return jsonify({"lista_relatorio_missao": relatorio_missao})

@app.route('/listar_ocorrencia')
def listar_ocorrencia():
    ocorrencia = list(map(model_to_dict, Ocorrencia.select()))
    return jsonify({"lista_ocorrencia": ocorrencia})

app.run(debug=True, port=5000)