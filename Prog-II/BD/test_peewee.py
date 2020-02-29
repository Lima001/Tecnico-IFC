import peewee, os

db = peewee.SqliteDatabase('animalia.db')

class Cliente(peewee.Model):
    nome = peewee.CharField()
    telefone = peewee.CharField()

    class Meta:
        database = db

    def __str__(self):
        return self.nome + " , " + self.telefone


class Animal(peewee.Model):
    dono = peewee.ForeignKeyField(Cliente)
    tipo = peewee.CharField()
    raca = peewee.CharField()

    class Meta:
        database = db

    def __str__(self):
        return self.tipo + ", " + self.raca + " De: " + str(self.dono)

class Consulta(peewee.Model):
    id_consulta = peewee.IntegerField()
    data = peewee.CharField()
    servico = peewee.CharField()
    horario = peewee.CharField()
    animal = peewee.ForeignKeyField(Animal)
    confirmacao = peewee.CharField()

    class Meta:
        database = db

    def __str__(self):
        return str(self.id_consulta) + "--> " + self.servico + "| data: " + self.data + "; " + self.horario + " | " +\
        str(self.animal) + " | Status: " + self.confirmacao 

if __name__ == "__main__":

    arq = "animalia.db"
    if os.path.exists(arq):
        os.remove(arq)

    try:
        db.connect()
        db.create_tables([Cliente,Animal,Consulta])
    
    except peewee.OperationalError as err:
        print ( "Criação de tabelas NÃO foi realizada !!!" +str (err))

    cliente1 = Cliente(nome="Alfred", telefone="3333-0976")
    cliente1.save()
    
    animal1 = Animal(dono=cliente1, tipo="Cachorro", raca="Cs-17")
    animal1.save()

    consulta1 = Consulta(id_consulta=1, data="21/07/2022", servico="Exame de Rotina",
                         horario="14:30", animal=animal1, confirmacao="Ok")
    consulta1.save()

    lista_consultas = Consulta.select()
    for consulta in lista_consultas:
        print(consulta) 