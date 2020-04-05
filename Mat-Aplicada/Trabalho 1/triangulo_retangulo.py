import math
import Calculos as calc

print("Para calcular os angulos internos de um triangulo através de seus lados, digite 1")
print()
print("Para calcular os angulos, possuindo um angulo e o valor de 2 lados, digite 3")
print()
print("Para achar o valor de um lado, possuindo 1 angulos e 2 lados, digite 2")
print()
print("Para descobrir a medida de um angulo possuindo 2, digite 4")
print()
print("Caso possua 2 angulos e 1 lado, e deseja o valor dos outros 2 lados, digite 5")
print()

executar = True
while executar:
    
    opção = int(input("Digite a opção: "))

    if opção == 1:
        cat_oposto = float(input("Entre com o valor do cateto oposto: "))
        cat_adjacente = float(input("Entre com o valor do cateto adjacente: "))
        hipotenusa = float(input("Entre com o valor da hipotenusa: "))
        angulos = calc.calcular_angulos_triangulo_retângulo(cat_oposto, cat_adjacente, hipotenusa)
        for numero in angulos:
            print()
            print("Angulos em Graus: " + str(math.degrees(numero)))
            print("Angulos em Radiano: " + str(numero))            

    if opção == 2:
        cat_oposto = float(input("Entre com o valor do cateto oposto: "))
        cat_adjacente = float(input("Entre com o valor do cateto adjacente: "))
        hipotenusa = float(input("Entre com o valor da hipotenusa: "))
        valor = calc.achar_lado(cat_oposto, cat_adjacente, hipotenusa)

        if cat_oposto == 0:
            angulos = calc.calcular_angulos_triangulo_retângulo(valor, cat_adjacente, hipotenusa)                    
            for numero in angulos:
                print()
                print("Angulos em Graus: " + str(math.degrees(numero)))
                print("Angulos em Radiano: " + str(numero))         
        if cat_adjacente == 0:
            angulos = calc.calcular_angulos_triangulo_retângulo(cat_oposto, valor, hipotenusa)                    
            for numero in angulos:
                print()
                print("Angulos em Graus: " + str(math.degrees(numero)))
                print("Angulos em Radiano: " + str(numero))                  
        if hipotenusa == 0:
            angulos = calc.calcular_angulos_triangulo_retângulo(cat_oposto, cat_adjacente, valor)                    
            for numero in angulos:
                print()
                print("Angulos em Graus: " + str(math.degrees(numero)))
                print("Angulos em Radiano: " + str(numero))     

    if opção == 3:
        cat_oposto = float(input("Entre com o valor do cateto oposto: "))
        cat_adjacente = float(input("Entre com o valor do cateto adjacente: "))
        hipotenusa = float(input("Entre com o valor da hipotenusa: "))

        valor = calc.achar_lado(cat_oposto, cat_adjacente, hipotenusa)
        print("O valor do lado é: " + str(valor))

    if opção == 4:
        angulo = float(input("Entre com o valor do angulo: "))
        angulo2 = float(input("Entre com o valor do angulo 2: "))
        resultado = (180 - (angulo+angulo2))

        print("O valor em radianos é: " + str(math.radians(resultado)))
        print("O valor em graus é: " + str(resultado))

    if opção == 5:
        angulo = float(input("Entre com o valor do angulo: "))
        angulo2 = float(input("Entre com o valor do angulo 2: "))
        lado = float(input("Digite o valor do lado: "))
        tipo_lado = input("O lado é digitado é a hipotenusa, o cateto oposto ou o cateto adjacente do angulo1? : ")
        frase = calc.achar_lados_retângulo(angulo, angulo2, tipo_lado, lado)
        print(frase)
