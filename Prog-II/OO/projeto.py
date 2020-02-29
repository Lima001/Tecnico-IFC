class Aluno:

    def __init__(self,nome,turma):
        self.nome = nome
        self.turma = turma
    
    def __str__(self):
        return self.nome + " " + self.turma + " "
    
class VeiculoDePublicacao:

    def __init__(self,titulo,sigla):
        self.titulo = titulo
        self.sigla = sigla

class AnaisDeEventoCientifico(VeiculoDePublicacao):

    def __init__(self,titulo,sigla,ano,local):
        super().__init__(titulo,sigla)
        self.ano = ano
        self.local = local

class Periodico(VeiculoDePublicacao):
    
    def __init__(self,titulo,sigla,editora,issn):
        super().__init__(titulo,sigla)
        self.issn = issn
        self.editora = editora

class AreaDeAtuacao:

    def __init__(self,denominacao, publicacao):
        self.denominacao = denominacao
        self.lista_publicacao = publicacao


class Professor:

    def __init__(self,nome,area_atuacao):
        self.nome = nome
        self.area_atuacao = area_atuacao
    
    def __str__(self):
        return self.nome + " " + str(self.area_atuacao)
    

class Projeto:

    def __init__(self,titulo,ano,alunos,professores):
        self.titulo = titulo
        self.ano = ano
        self.alunos = alunos
        self.professores = professores
    
    def __str__(self):
        return "PI: " + self.titulo + "; " + str(self.ano) + " | " +\
        str(self.alunos) + " Orientador: " + str(self.professores)
    
if __name__ == "__main__":

    aluno1 = Aluno("Thomas", "Engenharia Quantica III")
    eve1 = AnaisDeEventoCientifico("ScienceConference2019","SC19", 2019,"....")
    per1 = Periodico("BitScience","BT", "392-0091", "Science-Tx")
    area1 = AreaDeAtuacao("Computacao Quantica", [per1,eve1])
    prof1 = Professor("Edson", area1)
    projeto1 = Projeto("O poder do Quantum Bit",2019,aluno1,prof1)
    print(projeto1)