from flask import Flask, render_template, request, redirect
from modelo import *

app = Flask(__name__)

@app.route("/")
def iniciar():
    return render_template("inicio.html")

@app.route("/listar_receitas")
def listar_receitas():
    return render_template("listar_receitas.html",lista_receita=Receita.select())

@app.route("/listar_ingredientes_receita")
def listar_ingredientes_receita():
    id_receita = int(request.args.get("id_receita"))
    
    receita = Receita.get_by_id(id_receita)
    ingReceita = IngredienteDaReceita.select().where(IngredienteDaReceita.receita == receita)

    return render_template("listar_ingredientes.html",receita=receita,ings=ingReceita)

app.run(debug=True)