import os
from imagem import *

class Interpretador:

    def __init__(self,imagem=None,orientacao=None,deslocamento=20,velocidade=10,info_arq=None):
        self.imagem = imagem 
        self.diferenca = []
        self.comandos = []
        self.info_arq = info_arq  # (endereço_arquivo/nome_arquivo, modo_leitura)
        self.info_movimento = (orientacao,deslocamento,velocidade)
        

    def executar(self):
        self.calcular_diferenca()
        self.gerar_comandos()

        if self.info_arq is not None:
            self.salvar_em_arquivo()

    def calcular_diferenca(self):
        for x in range(len(self.imagem.pontos)):
                if x+1 == len(self.imagem.pontos):
                        break
                else:
                        ele1 = self.imagem.pontos[x]
                        ele2 = self.imagem.pontos[x+1]
                        dif = (ele2[0]-ele1[0],ele2[1]-ele1[1])
                        self.diferenca.append(dif)
    
    def gerar_comandos(self):

        self.comandos = ["command","takeoff"]
        
        if self.info_movimento[0] == "h":
            for ocorrencia in (self.diferenca):
                x = ocorrencia[0] * self.info_movimento[1]
                y = ocorrencia[1] * self.info_movimento[1]

                self.comandos.append("go " + str(x) + " " + str(y) + " 0 " + str(self.info_movimento[2]))                

        if self.info_movimento[0] == "v":
            for ocorrencia in self.diferenca:
                z = ocorrencia[0] * self.info_movimento[1]
                x = ocorrencia[1] * self.info_movimento[1]

                self.comandos.append("go " + str(x) + " 0 " + " " + str(z) + " " + str(self.info_movimento[2]))
                
         
        self.comandos.append("land")

    def salvar_em_arquivo(self):
        arq = open(self.info_arq[0], self.info_arq[1])
        arq.write(self.imagem.endereco + "\n")
        for c in range(len(self.comandos)):
            if c != 2: 
                arq.write(self.comandos[c] + "\n")
            else:
                seq = self.comandos[c].split(";")
                for i in seq:
                    arq.write("- " + i + "\n")
        arq.close()

    # Arquivo deve seguir formato igual ao gerado pelo método salvar_em_arquivo
    def gerar_comandos_com_arquivo(self,arquivo):
        arq = open(arquivo)
        dados = arq.read().splitlines()
        
        self.comandos = ["command","takeoff"]
        cmd = ""
        for x in dados[3:-1]:
            cmd += x[2:] + ";"
        self.comandos.append(cmd[:-1])
        self.comandos.append("land")
        
        arq.close()

if __name__ == "__main__":
    num_im = input("Digite o numero da imagem a ser analisada: ")
    im = "../BancoImagem/imagem" + num_im + ".png"
    imagem1 = ImagemAnalise(im)
    imagem1.inicializar()

    print(imagem1.pontos)
    trava = input(">>>")
    
    interpretador1 = Interpretador(imagem1,"h",info_arq=("arq_comandos.txt","a"))
    interpretador1.executar()
    
    print(interpretador1.diferenca)
    
    for x in interpretador1.comandos:
        print(x)

    print(interpretador1.comandos)    