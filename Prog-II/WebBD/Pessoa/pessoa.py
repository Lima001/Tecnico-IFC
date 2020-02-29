from peewee import *
import os

db = SqliteDatabase("pessoa.db")

class Pessoa(Model):

    cpf = CharField()
    nome = CharField()
    endereco = CharField()
    telefone = CharField()

    class Meta:

        database = db

if __name__ == "__main__":

    if os.path.exists("pessoa.db"):
        os.remove("pessoa.db")

    try:
        db.connect()
        db.create_tables([Pessoa])

    except OperationalError as err:
        print ( "ERRO !!!" +str (err))