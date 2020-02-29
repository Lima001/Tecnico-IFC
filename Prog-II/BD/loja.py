import os
from peewee import *

arq = "loja.db"
db = SqliteDatabase(arq)

class BaseModel(Model):

    class Meta:
        database = db

class Cliente(BaseModel):

    nome = CharField()
    email = CharField()

class Produto(BaseModel):

    den_produto = CharField()
    preco = FloatField()

class Venda(BaseModel):

    cod_venda = IntegerField()
    data_hora = CharField()
    cliente = ForeignKeyField(Cliente)
    produtos = ManyToManyField(Produto)

if __name__ == "__main__":

    try:
        os.system("cls")
    except:
        os.system("clear")

    if os.path.exists(arq):
        os.remove(arq)
    
    try:
        db.connect()
        db.create_tables([Cliente,Produto,Venda, Venda.produtos.get_through_model()])

    except OperationalError as err:
        print ( "ERRO !!!" +str (err))

    produto1 = Produto.create(den_produto="Placa de Vídeo ZTX 5080 TI",preco=989.50)
    produto2 = Produto.create(den_produto="SSD MLar 2TB ",preco=499.90)

    cliente1 = Cliente.create(nome="Sapiens Sapiens",email="ser.humaninho123@gmail.com")

    venda1 = Venda.create(cod_venda=1, data_hora="16:30 -- 12/02/2027", cliente=cliente1)
    venda1.produtos.add([produto1,produto2])

    vendas = Venda.select()

    for venda in vendas:
        print(str(venda.cod_venda) + " | "  + str(venda.data_hora) + "\n" + venda.cliente.nome + "\n")

        for prod in venda.produtos:
            print(prod.den_produto + " -- " + str(prod.preco))