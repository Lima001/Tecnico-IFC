import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.ticker as ticker

def funcao_seno(a, b, c, d, x):
    y = a * np.sin(b*x +c) + d
    return y
    
def funcao_cosseno(a, b, c, d, x):
    y = a * np.cos(b*x +c) + d
    return y

def funcao_tangente(a, b, c, d, x):
    y = a * np.tan(b*x +c) + d
    return y

def calcular_periodo(b):
    periodo = (2*np.pi)/b
    return periodo

#########################################################################


#def calcular__valor_x_para_ponto_maximo_minimo(imagem, tipo):
#    valores = []
#    if tipo == "seno":
#        ponto_minimo = np.degrees(np.arcsin(imagem[0]))
#        ponto_maximo = np.degrees(np.arcsin(imagem[1]))
#        valores = [ponto_minimo, ponto_maximo]
#       return valores
#    else:
#        ponto_minimo = np.degrees(np.arccos(imagem[0]))
#        ponto_maximo = np.degrees(np.arccos(imagem[1]))
#        valores = [ponto_minimo, ponto_maximo]
#        return valores

#############################################################################

def valor_ponto_maximo_minimo(imagem):
    valores = []
    maximo = imagem[1]
    minimo = imagem[0]
    valores = [minimo, maximo]
    return valores
    
def calcular_amplitude(imagem):
    amplitude = (imagem[1]-imagem[0])/2
    return amplitude
    
def calcular_imagem(lista):
    lista.sort()
    imagem = []
    imagem.append(lista[0])
    imagem.append(lista[-1])
    imagem.sort
    return imagem


def desenhar_grafico(x, y, tipo_funcao, cor, periodo):
        fig, ax = plt.subplots()
        ax.plot(x,y, color= cor)
        ax.set_title("Função " +str(tipo_funcao), fontweight= "bold")
        ax.set_xlabel("Valores de X")
        ax.set_ylabel("Valores de Y")
        vx = (np.arange(0.0,(periodo+0.5)*np.pi,np.pi/2))
        ax.set_xticks(vx)
        for tick in ax.get_xticklabels():
            tick.set_rotation(-55)
        ax.grid(True, linestyle='--')
        ax.tick_params(labelcolor="b", labelsize='medium', width=3)
        plt.show()    

def limpar_tela(numero_linhas=100):
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print('\n'*numero_linhas)
        
    print("Para função seno, digite 1 ")
    print("Para funão cosseno, digite 2 ")
    print("Para função tangente, digite 3 ")
    print("Para sair, digite 4 ")
    print("Formato:  a* ...(b*x +c) +d ")


if __name__ == "__main__":

    executar = True

    while executar:

        limpar_tela()
        print()
        opcao = int(input("Entre com a opção que deseja: "))

        if opcao == 1:

            a = eval(input("Entre com o valor de 'a': "))
            b = eval(input("Entre com o valor de 'b': "))
            c = eval(input("Entre com o valor de 'c': "))
            d = eval(input("Entre com o valor de 'd': "))

            periodo = 2*(calcular_periodo(b))
            x = np.arange(0.0, periodo+0.1, 0.1)
            y = funcao_seno(a, b, c, d, x)

            desenhar_grafico(x, y, "Seno", "g", 2*(calcular_periodo(b)/np.pi))
            print("Periodo: " + str(calcular_periodo(b)/np.pi) + "π")
            imagem = calcular_imagem(y)
            print("[" + str(d-a) + ",", end="")
            print(" " + str(d+a) + "]")
            print("Imagem: " + str(imagem))
            valor_maximo_minimo = valor_ponto_maximo_minimo(imagem)
            print("Valor minimo: " +str(valor_maximo_minimo[0]) + "; Valor máximo: " + str(valor_maximo_minimo[1]))
            #valor_de_x = calcular__valor_x_para_ponto_maximo_minimo(y, "seno")
            #print(valor_de_x)
            amplitude = calcular_amplitude(imagem)
            print("Amplitude: " + str(amplitude))
            
    
                    
        elif opcao == 2:

            a = eval(input("Entre com o valor de 'a': "))
            b = eval(input("Entre com o valor de 'b': "))
            c = eval(input("Entre com o valor de 'c': "))
            d = eval(input("Entre com o valor de 'd': "))

            periodo = 2*(calcular_periodo(b))

            x = np.arange(0.0, periodo+0.1, 0.1)
            y = funcao_cosseno(a, b, c, d, x)

            desenhar_grafico(x, y, "Cosseno", "r", 2*(calcular_periodo(b)/np.pi))

            print("Periodo: " + str(calcular_periodo(b)/np.pi) + "π")
            imagem = calcular_imagem(y)
            print("Imagem: " + str(imagem))
            print("[" + str(d-a) + ",", end="")
            print(" " + str(d+a) + "]")
            valor_maximo_minimo = valor_ponto_maximo_minimo(imagem)
            print("Valor minimo: " +str(valor_maximo_minimo[0]) + "; Valor máximo: " + str(valor_maximo_minimo[1]))
            #valor_de_x = calcular__valor_x_para_ponto_maximo_minimo(y, "cosseno")
            #print(valor_de_x)
            amplitude = calcular_amplitude(imagem)
            print(amplitude)
            
            
        elif opcao == 3:

            a = eval(input("Entre com o valor de 'a': "))
            b = eval(input("Entre com o valor de 'b': "))
            c = eval(input("Entre com o valor de 'c': "))
            d = eval(input("Entre com o valor de 'd': "))

            periodo = np.pi/b
            print("Periodo: " + str(periodo/np.pi) + "π")

        elif opcao == 4:
            executar = False
        else:
            print("Opção inválida")

        print()
        a = input("Presione enter para continuar")
        limpar_tela()
    print("By Gabreil Eduardo Lima")        
