from peewee import *
import os

arq = "marcenaria.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Cliente(BaseModel):
    id = IntegerField() 
    nome = CharField()

    def __str__(self):
        return str(self.id) + "-->" + self.nome

class Material(BaseModel):
    id = IntegerField()
    nome = CharField()
    qtd = IntegerField()

class Mobilia(BaseModel):
    id = IntegerField()
    cor = CharField()
    medidas = CharField()
    sob_medida = BooleanField()
    materiais = ManyToManyField(Material)

class Pedido(BaseModel):
    id = IntegerField()
    data_hora = CharField()
    cliente = ForeignKeyField(Cliente)
    mobilias = ManyToManyField(Mobilia)

if __name__ == "__main__":

    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Cliente, Material, Mobilia.materiais.get_through_model(), Pedido.mobilias.get_through_model()])

    except OperationalError as err:
        print ( "ERRO !!!" +str (err))

    c1 = Cliente(id=1,nome="Sofia Alma Caridosa")
    mat1 = Material(id=1,nome="Madeira",qtd=5)
    mat2 = Material(id=2,nome="Prego",qtd=50)
    mob1 = Mobilia(id=1,cor="Preto",medidas="1.20 X 0.50")

    mob1.materiais.add([mat1,mat2])

    ped1 = Pedido(id=1,data_hora="11/10/2020 -- 14:30", cliente=c1)
    ped1.mobilias.add([mob1])

    print("Sucess")