from flask import Flask, render_template, session, redirect, request, url_for
from classe_jogo import *

app = Flask("__name__")
app.config["SECRET_KEY"] = "123001"

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/form_login")
def form_login():
    return render_template("form_login.html")

@app.route("/login", methods=['post'])
def login():
    usuario = request.form["usuario"]
    senha = request.form["senha"]

    if usuario == "root" and senha == "toor":
        session["user"] = usuario
        return redirect("/")
    else:
        return "Erro! Verifique o usuario/senha, e tente novamente"

@app.route("/logout")
def logout():
    session.pop("user")
    return redirect("/")

@app.route("/listar_jogos")
def listar_jogos():
    return render_template("listar.html", lista=jogos)

@app.route("/form_inserir_jogo")
def form_inserir_jogo():
    return render_template("form_inserir.html")

@app.route("/inserir_jogo", methods=['post'])
def inserir_jogo():
    id = int(request.form["id"])
    nome = request.form["nome"]
    ano_lancamento = int(request.form["ano_lancamento"])
    qtd_estoque = int(request.form["qtd_estoque"])

    jogos.append(Jogo(id,nome,ano_lancamento,qtd_estoque))
    return listar_jogos()

@app.route("/excluir_jogo")
def excluir():
    cod = int(request.args.get("id"))
    for jogo in jogos:
        if jogo.id == cod:
            jogos.remove(jogo)
            return redirect(url_for("inicio"))

@app.route("/form_alterar", methods=["post"])
def form_alterar():
    id = request.form["id"]

    for j in jogos:
        if j.id == int(id):
            return render_template("form_alterar.html", jogo=j)
    return "Erro no sistema, tente novamente"

@app.route("/alterar", methods=['post'])
def alterar():
    id = int(request.form["id"])
    nome = request.form["nome"]
    ano_lancamento = int(request.form["ano_lancamento"])
    qtd_estoque = int(request.form["qtd_estoque"])

    for cont in range(len(jogos)):
        if jogos[cont].id == id:
            jogos[cont] = Jogo(id,nome,ano_lancamento,qtd_estoque)
            return redirect(url_for("listar_jogos"))
    return "Erro! Tente novamente"

app.run()