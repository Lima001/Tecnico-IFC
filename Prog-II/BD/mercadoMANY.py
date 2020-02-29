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

    def __str__(self):
        return str(self.cod_produto) + " " + self.nome + " " + str(self.preco)


class Carrinho(BaseModel):
    
    cod_carrinho = IntegerField()
    data = CharField()
    hora = CharField()
    produtos = ManyToManyField(Produto)

    def __str__(self):
        sturing=[]
        for x in self.produtos:
            sturing.append(x)

        return str(self.cod_carrinho) + " " + str(sturing)


if __name__ == "__main__":

    arq = "mercado.db"
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Produto,Carrinho,Carrinho.produtos.get_through_model()])

    except OperationalError as err:
        print ( "ERRO !!!" +str (err))



    prod1 = Produto.create(cod_produto=1,nome="Batata",preco=0.99)
    prod2 = Produto.create(cod_produto=2,nome="Arroz",preco=5.49)
    prod3 = Produto.create(cod_produto=3,nome="Bolacha",preco=2.99)



    car1 = Carrinho.create(cod_carrinho=1,data="02/09/2023",hora="16:14")
    

    car1.produtos.add([prod1,prod2])
    prod3.carrinhos.add(car1)
    print(car1)
