import numpy as np
import matplotlib.pyplot as plt

matriz = []

def criar_matriz(linhas, colunas):
    global matriz
    for x in range(linhas):
        lista = []
        for y in range(colunas):
            valor= int(input("digite p elemento: [" +str(x)+ "]" + "[" + str(y) + "]"))
            lista.append(valor)
            

        matriz.append(lista)
    return matriz




if __name__== "__main__":
    linhas = int(input("digite a quantidade de linhas: "))
    colunas = int(input("digite a quantidade de colunas: "))
    a= criar_matriz(linhas, colunas)
    for i in range(len(a)):
        print(a[i])


