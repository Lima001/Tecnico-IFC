import os
from peewee import *

db = SqliteDatabase('mercado.db')

class BaseModel(Model):
    class Meta:
        database = db

class Produto(BaseModel):

    cod_produto = IntegerField()
    nome = CharField()
    preco = FloatField()

class Carrinho(BaseModel):
    
    cod_carrinho = IntegerField()
    data = CharField()
    hora = CharField()

class Item(BaseModel):

    produto = ForeignKeyField(Produto)
    carrinho = ForeignKeyField(Carrinho)
    qtd = IntegerField()


if __name__ == "__main__":

    arq = "mercado.db"
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Produto,Carrinho,Item])

    except OperationalError as err:
        print ( "ERRO !!!" +str (err))




    prod1 = Produto.create(cod_produto=1,nome="Batata",preco=0.99)
    prod2 = Produto.create(cod_produto=2,nome="Arroz",preco=5.49)
    prod3 = Produto.create(cod_produto=3,nome="Bolacha",preco=2.99)

    car1 = Carrinho.create(cod_carrinho=1,data="02/09/2023",hora="16:14")

    item1 = Item.create(produto=prod1,carrinho=car1,qtd=2)
    item2 = Item.create(produto=prod2,carrinho=car1,qtd=1)
    item3 = Item.create(produto=prod3,carrinho=car1,qtd=3)