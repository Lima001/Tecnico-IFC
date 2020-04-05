class Jogo:

    def __init__(self,id,nome,ano_lancamento,quantidade_estoque):
        self.id = id
        self.nome = nome
        self.ano_lancamento = ano_lancamento
        self.qtd_estoque = quantidade_estoque

jogos = []
jogos.append(Jogo(1,"MK 11",2019,5))
jogos.append(Jogo(2,"GTA VI",2020,10))
jogos.append(Jogo(3,"Dromme",2018,8))