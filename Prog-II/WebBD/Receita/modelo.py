from peewee import *
import os

arq = "Receitas_e_Ingredientes"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Ingrediente(BaseModel):
    nome = CharField()
    unidade = CharField()

class Receita(BaseModel):
    nome = CharField()

class IngredienteDaReceita(BaseModel):
    receita = ForeignKeyField(Receita)
    ingrediente = ForeignKeyField(Ingrediente)
    quantidade = FloatField()

if __name__ == "__main__":

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Ingrediente,Receita,IngredienteDaReceita])
    except:
        print("Erro!")

    bolo = Receita.create(nome="Bolo de Laranja")
    ovo = Ingrediente.create(nome="Ovo",unidade="Unidade")
    laranja = Ingrediente.create(nome="Laranja",unidade="Unidade")

    ing_receita1 = IngredienteDaReceita.create(receita=bolo,ingrediente=ovo,quantidade=3.0)
    ing_receita2 = IngredienteDaReceita.create(receita=bolo,ingrediente=laranja,quantidade=3.0)
    
    for rec in Receita.select():
        print("Receita: " + rec.nome)
        ingredientes = IngredienteDaReceita.select().where(IngredienteDaReceita.receita == rec)
        print("-- Ingredientes:")
        for ing in ingredientes:
            print("--- " + ing.ingrediente.nome,end="")
            print(" "*10 + "Qtd: " + str(ing.quantidade) + " " + str(ing.ingrediente.unidade))