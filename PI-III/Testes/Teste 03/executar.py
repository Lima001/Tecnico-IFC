import os
import socket, time, threading
from drone import *
from imagem import *
from interpretador import *

exe = True
while exe:

    trava = input(">>>")

    num_im = input("Digite o numero da imagem a ser analisada: ")
    im = "../BancoImagem/imagem" + num_im + ".png"
    imagem1 = ImagemAnalise(im)
    imagem1.inicializar()

    print(imagem1.pontos)

    trava = input(">>>")

    interpretador1 = Interpretador(imagem1,"h",info_arq=("arq_comandos.txt","a"))
    interpretador1.executar()

    print(interpretador1.diferenca)

    interpretador1.gerar_comandos_com_arquivo("arq_comandos.txt")

    print(interpretador1.comandos)

    trava = input(">>>")
    '''
    conexao1 = ConexaoDrone('',9000,("192.168.10.1", 8889))
    comandos = interpretador1.comandos
    conexao1.executar_sequencia_comando(comandos)'''

    con = None
    while con not in (1,2):
        con = int(input("Executar Novamente  1:Sim / 2:Não --> "))
        if con not in (1,2):
            print("Digite a opção corretamente ...")
    if con == 2:
        exe = False
