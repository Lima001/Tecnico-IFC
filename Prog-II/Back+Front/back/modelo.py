from peewee import *

arq = "dados.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Cachorro(BaseModel):
    nome = CharField()
    idade = IntegerField()
    raca = CharField()

if __name__ == "__main__":

    db.connect()
    db.create_tables([Cachorro])

    dog1 = Cachorro.create(nome="Rex",idade=1,raca="Pastor Alemao")

    print(dog1.nome + "|" + str(dog1.idade) + "|" + dog1.raca)