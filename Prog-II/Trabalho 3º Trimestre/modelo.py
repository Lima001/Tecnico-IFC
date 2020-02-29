import os
import datetime
from peewee import *

arq = "SistemaEspacial.db"
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Astronauta(BaseModel):
    nome = CharField()
    idade = IntegerField()

    def __str__(self):
        return "Astronauta " + self.nome + " - " + str(self.idade) + " anos"

class Treino(BaseModel):
    nome = CharField()
    carga_horaria = FloatField()
    
    def __str__(self):
        return "Treino: " + self.nome + " - " + str(self.carga_horaria) + " hora(s)"


class TreinoDoAstronauta(BaseModel):
    astronauta = ForeignKeyField(Astronauta)
    treino = ForeignKeyField(Treino)
    status = BooleanField()

    def __str__(self):
        situacao = ""
        
        if self.status == True:
            situacao = "Concluido"
        else:
            situacao = "Em progresso"

        return "Astronauta: " + self.astronauta.nome + " - Treino:" + self.treino.nome + " - Status: " + situacao

class CentralTerrestre(BaseModel):
    nome = CharField()
    qtd_empregados = IntegerField()

    def __str__(self):
        return "Central: " + self.nome + " - Empregados: " + str(self.qtd_empregados)

class Equipe(BaseModel):
    nome = CharField()
    astronautas = ManyToManyField(Astronauta)
    central = ForeignKeyField(CentralTerrestre)
    status_comunicacao = BooleanField()
    ativa = BooleanField()

    def __str__(self):
        string_astronautas = ""
        status_atividade = ""

        if self.ativa == True:
            status_atividade = "Ativada"
        else:
            status_atividade = "Desativada"

        for a in self.astronautas:
            string_astronautas += str(a) + "\n"

        return "Equipe: " + self.nome + " - Status: " + status_atividade +\
                " - Comunicacao com a Base: " + str(self.status_comunicacao) + "\n" + string_astronautas

class Nave(BaseModel):
    codigo = CharField()
    central = ForeignKeyField(CentralTerrestre)
    porcentagem_combustivel = FloatField()
    status_funcionamento = BooleanField()

    def __str__(self):
        status = ""
        if self.status_funcionamento == True:
            status = "Operacional"
        else:
            status = "Incapacitada"

        return "Nave cod: " + self.codigo + " - Central: " + str(self.central.nome) + " - Combustivel: " +\
            str(self.porcentagem_combustivel) + " % " + " - Status: " + status 

class RevisaoMecanica(BaseModel):
    descricao = CharField()
    data_conclusao = DateTimeField()
    gastos = FloatField()
    nave_revisada = ForeignKeyField(Nave)

    def __str__(self):
        return "Revisao: " + self.descricao + " - Nave: " + str(self.nave_revisada.codigo) +\
             " - finalizado em: " + str(self.data_conclusao) + " - Gasto Total: " + str(self.gastos) 

class Planeta(BaseModel):
    nome = CharField()
    gravidade = FloatField()
    atmosfera_respiravel = BooleanField()

    def __str__(self):
        atmosfera = ""
        if self.atmosfera_respiravel == True:
            atmosfera = "Respiravel"
        else:
            atmosfera = "Não Respiravel"

        return "Planeta: " + self.nome + " - Gravidade: " + str(self.gravidade) + " - Atmosfera: " + atmosfera

class BasePlanetaria(BaseModel):
    codinome = CharField()
    localizacao = ForeignKeyField(Planeta)
    status_comunicacao_terra = BooleanField()

    def __str__(self):
        comunicacao = ""
        if self.status_comunicacao_terra == True:
            comunicacao = "Ativada"
        else:
            comunicacao = "Desativada"
        return "Base: " + self.codinome + " - Situada em: " + self.localizacao.nome + " - Comunicacao " + comunicacao

class Tarefa(BaseModel):
    astronautas_responsaveis = ManyToManyField(Astronauta)
    descricao = CharField()
    tempo_delimitado = FloatField()

    def __str__(self):
        encarregados = ""
        for a in self.astronautas_responsaveis:
            encarregados += a.nome + "|"
        return "Tarefa: " + self.descricao + " - Encarregados: " + encarregados + " - Duracao: " + str(self.tempo_delimitado)

class Missao(BaseModel):
    codinome = CharField()
    equipe = ForeignKeyField(Equipe)
    nave_utilizada = ForeignKeyField(Nave)
    inicio = DateTimeField()
    termino = DateTimeField()
    local = ForeignKeyField(Planeta)
    status_missao = BooleanField()

    def __str__(self):
        status = ""
        if self.status_missao == True:
            status = "Em andamento"
        else:
            status = "Atracada"

        astronautas = ""
        for a in self.equipe.astronautas:
            astronautas += a.nome + "|"
        
        return "Missao: " + self.codinome + " - Equipe: " + astronautas + " | " + self.equipe.central.nome +\
                " Nave: " + self.nave_utilizada.codigo + " - Local: " + self.local.nome +\
                " Inicio: " + str(self.inicio) + " / Termino: " + str(self.termino) + " - Missao " + status 


class RelatorioDaMissao(BaseModel):
    missao = ForeignKeyField(Missao)
    tarefa = ForeignKeyField(Tarefa)
    descricao = CharField(default="Sem comentarios")
    status_conclusao = BooleanField()

    def __str__(self):
        conclusao = ""
        if self.status_conclusao == True:
            conclusao = "Concluida"
        else:
            conclusao = "Em andamento"

        return "Tarefa: " + self.tarefa.descricao + " - Missao: " + self.missao.codinome + " -> " + self.descricao +\
                " -- " + conclusao

class Ocorrencia(BaseModel):
    autor = ForeignKeyField(Astronauta)
    data = DateTimeField()
    descricao = CharField()
    missao = ForeignKeyField(Missao)

    def __str__(self):
        return str(self.id) + " - Autor: " + self.autor.nome + " - Data: " + str(self.data) + " --> " + self.descricao +\
                " - Missao: " + self.missao.codinome   

if __name__ == "__main__":

    if os.path.exists(arq):
        apagar = int(input("Deseja resetar o BD?   1-Sim | 2-Não  --> "))
        print()
        if apagar == 1:
            os.remove(arq)

    try:
        db.connect()
        db.create_tables([Astronauta, Treino, TreinoDoAstronauta, 
                          CentralTerrestre, Equipe, Equipe.astronautas.get_through_model(),
                          Nave, RevisaoMecanica, Planeta, BasePlanetaria, Tarefa,
                          Tarefa.astronautas_responsaveis.get_through_model(), Missao,
                          RelatorioDaMissao, Ocorrencia
                        ])

    except OperationalError as err:
        print("Erro - " + str(err))

    astronauta1 = Astronauta.create(nome="Amarildo", idade=32)
    astronauta2 = Astronauta.create(nome="Ana", idade=26)
    print(astronauta1, end="\n\n")
    print(astronauta2, end="\n\n")

    treino1 = Treino.create(nome="Pouso de Emergencia", carga_horaria=30)
    treino2 = Treino.create(nome="Primeiro Socorros", carga_horaria=36)
    print(treino1, end="\n\n")
    print(treino2, end="\n\n")

    treinoastronauta1 = TreinoDoAstronauta.create(astronauta=astronauta1, treino=treino1, status=True)
    treinoastronauta2 = TreinoDoAstronauta.create(astronauta=astronauta2, treino=treino2, status=False)
    print(treinoastronauta1, end="\n\n")
    print(treinoastronauta2, end="\n\n")

    central1 = CentralTerrestre.create(nome="AstroBras", qtd_empregados=650)
    print(central1, end="\n\n")

    equipe1 = Equipe.create(nome="Double A", central=central1, status_comunicacao=True, ativa=True)
    equipe1.astronautas.add([astronauta2, astronauta1])
    print(equipe1, end="\n\n")

    nave1 = Nave.create(codigo="DB-128-4", central=central1, porcentagem_combustivel=100.0, status_funcionamento=True)
    print(nave1, end="\n\n")

    revisao1 = RevisaoMecanica.create(descricao="Ajuste Paraquedas Espacial", data_conclusao=datetime.datetime.now(), 
                gastos=45000.0, nave_revisada=nave1)
    revisao2 = RevisaoMecanica.create(descricao="Ajuste Radar Cosmico", data_conclusao=datetime.datetime.now(), 
                gastos=33500.0, nave_revisada=nave1)
    print(revisao1, end="\n\n")
    print(revisao2, end="\n\n")

    planeta1 = Planeta.create(nome="Jupiter", gravidade=24.79, atmosfera_respiravel=False)
    print(planeta1, end="\n\n")

    baseplanetaria1 = BasePlanetaria.create(codinome="J-3545-1", localizacao=planeta1, status_comunicacao_terra=False)
    print(baseplanetaria1, end="\n\n")

    tarefa1 = Tarefa.create(descricao="Explorar Arredores da Base", tempo_delimitado=4.0)
    tarefa1.astronautas_responsaveis.add([astronauta1, astronauta2])
    tarefa2 = Tarefa.create(descricao="Comunicar Central Terrestre", tempo_delimitado=0.30)
    tarefa2.astronautas_responsaveis.add([astronauta2])
    print(tarefa1, end="\n\n")
    print(tarefa2, end="\n\n")

    missao1 = Missao.create(codinome="JupExplore-III", equipe=equipe1, nave_utilizada=nave1,
    inicio=datetime.datetime.now(), termino=datetime.datetime.now(), local=planeta1, status_missao=False)
    print(missao1, end="\n\n")

    relatoriomissao1 = RelatorioDaMissao.create(missao=missao1, tarefa=tarefa1, status_conclusao=False)
    print(relatoriomissao1, end="\n\n")

    ocorrencia1 = Ocorrencia.create(autor=astronauta1, data=datetime.datetime.now(), 
                                    descricao="Observacao de Atividade incomum, cod 09-ti", missao=missao1)
    print(ocorrencia1)

    missao = Missao.select()
    print(missao)