from numpy import *
from numpy.linalg import inv

funcionar = True
while funcionar == True:
    print("." * 80)
    print("Digite 1-> Para codificar uma mensagem")
    print("Digite 2-> Para descodificar uma mensagem")
    print("Digite 3-> Para Sair")
    print("." * 80)
    
    opcao = int(input("Digite sua opção: "))
    if opcao == 3:
        funcionar = False


    elif opcao == 1:

        matriz_codificadora_linha1 = eval('[' + input("Digite a primeira linha da matriz chave: ") + ']')
        matriz_codificadora_linha2 = eval('[' + input("Digite a segunda linha da matriz chave: ") + ']')

        texto_linha1 = input("Digite a primeira linha de texto")
        texto_linha2 = input("Digite a segunda linha de texto")

        matriz_linha1 = []
        matriz_linha2 = []

        for letra in texto_linha1:
            matriz_linha1.append(ord(letra))
        for letra in texto_linha2:
            matriz_linha2.append(ord(letra))

        matriz_codificada_linha1 = []
        matriz_codificada_linha2 = []
        
        
        for x in range(len(matriz_linha1)):
            matriz_codificada_linha1.append((matriz_linha1[x] * matriz_codificadora_linha1[0]) + matriz_linha2[x] * matriz_codificadora_linha1[1])
            matriz_codificada_linha2.append((matriz_linha1[x] * matriz_codificadora_linha2[0]) + matriz_linha2[x] * matriz_codificadora_linha2[1])

        print(matriz_linha1)
        print(matriz_linha2)
        print("*" * 80)
        print(matriz_codificada_linha1)
        print(matriz_codificada_linha2)

    elif opcao == 2:
        
        matriz_chave_linha1 = eval('[' + input("Digite a primeira linha da matriz chave: ") + ']')
        matriz_chave_linha2 = eval('[' + input("Digite a segunda linha da matriz chave: ") + ']')

        matriz_mensagem_linha1 = eval('[' + input("Digite a primeira linha da matriz mensagem: ") + ']')
        matriz_mensagem_linha2 = eval('[' + input("Digite a segunda linha da matriz mensagem: ") + ']')

        numero1 = []
        numero2 = []

        a = ([matriz_chave_linha1,matriz_chave_linha2])
        inva = inv(a)                                                         


        for x in range(len(matriz_mensagem_linha1)):
            numero1.append(round((matriz_mensagem_linha1[x] * inva[0][0]) + matriz_mensagem_linha2[x] * inva[0][1]))
            numero2.append(round((matriz_mensagem_linha1[x] * inva[1][0]) + matriz_mensagem_linha2[x] * inva[1][1]))

        print(numero1)
        print(numero2)
        print("*" * 80)


        mensagem_linha1 = []
        mensagem_linha2 = []

        for numero in numero1:
            mensagem_linha1.append(chr(int(numero)))
        for numero in numero2:
            mensagem_linha2.append(chr(int(numero)))

        print("Matriz inversa:")
        print(inva)
        print("*" * 80)
        print(mensagem_linha1)
        print(mensagem_linha2)

    else:
        print("Opção inválida!")
