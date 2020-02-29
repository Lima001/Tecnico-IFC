import math
import Calculos as calc

print("Para calcular os angulos internos de um triangulo através de seus lados, digite 1")
print()
print("Para calcular o lado, possuindo um angulo e o valor de 2 lados, digite 2")
print()
print("Para achar o valor de 1 angulo, possuindo 2 lados e 1 angulos, digite 3")
print()
print("Para descobrir a medida de um angulo possuindo 2, digite 4")
print()
print("Caso possua 2 angulos e 1 lado, e deseja o valor dos outros 2 lados, digite 5")
print()
print("Para converter graus em radianos digite 6")
print()
print("Para converter radianos em graus, digite 7")
print()
executar = True
while executar:
    opção = int(input("Entre com a opção que vc deseja: "))

    if opção == 1:

        a = float(input("Entre com o lado 'a' do triângulo: "))
        b = float(input("Entre com o lado 'b' do triângulo: "))
        c = float(input("Entre com o lado 'c' do triângulo: "))

        angulos_radianos = calc.calcular_angulos_internos_3_lados(a,b,c)

        for numero in angulos_radianos:
            print()
            print("Angulos em Graus: " + str(math.degrees(numero)))
            print("Angulos em Radiano: " + str(numero))

    if opção == 2:

        print("Caso não possua um dos valores, digite 0")

        a = float(input("Entre com o lado 'a' do triângulo: "))
        b = float(input("Entre com o lado 'b' do triângulo: "))
        c = float(input("Entre com o lado 'c' do triângulo: "))
        A = float(input("Entre com o angulo 'A' do triângulo: "))
        B = float(input("Entre com o angulo 'B' do triângulo: "))
        C = float(input("Entre com o angulo 'C' do triângulo: "))

        valor_lado = calc.calcular_lado(a, b, c, A, B, C)
        print()
        print(valor_lado)

    if opção == 3:

        print("Caso não possua um dos valores, digite 0")

        a = float(input("Entre com o lado 'a' do triângulo: "))
        b = float(input("Entre com o lado 'b' do triângulo: "))
        c = float(input("Entre com o lado 'c' do triângulo: "))
        A = float(input("Entre com o angulo 'A' do triângulo: "))
        B = float(input("Entre com o angulo 'B' do triângulo: "))
        C = float(input("Entre com o angulo 'C' do triângulo: "))

        if a > 0 and b > 0 and B > 0 and c == 0 and A == 0 and C ==0:
            angulo = calc.calcular_angulo_A_B(a, b, B)
            print()
            print("O angulo A em radianos é: " + str(angulo))
            print("O angulo A em graus é: " + str(math.degrees(angulo)))

        if a > 0 and c > 0 and C > 0 and b == 0 and B ==0 and A ==0:
            angulo = calc.calcular_angulo_A_C(a, c, C)
            print()
            print("O angulo A em radianos é: " + str(angulo))
            print("O angulo A em graus é: " + str(math.degrees(angulo)))

        if c > 0 and b > 0 and B > 0 and a ==0 and C==0 and A==0:        
            angulo = calc.calcular_angulo_C_B(b,c, B)
            print()
            print("O angulo C em radianos é: " + str(angulo))
            print("O angulo C  em graus é: " + str(math.degrees(angulo)))

        if c > 0 and a > 0 and A > 0 and b ==0 and B==0 and C==0:        
            angulo = calc.calcular_angulo_C_A(a, c, A)
            print()
            print("O angulo C em radianos é: " + str(angulo))
            print("O angulo C  em graus é: " + str(math.degrees(angulo)))

        if a > 0 and b > 0 and A > 0 and c ==0 and C ==0 and B==0:            
            angulo = calc.calcular_angulo_B_A(a, b, A)
            print()
            print("O angulo B em radianos é: " + str(angulo))
            print("O angulo B  em graus é: " + str(math.degrees(angulo)))

        if c > 0 and a > 0 and C > 0 and b ==0 and B ==0 and A==0:        
            angulo = calc.calcular_angulo_B_C(b, c, C)
            print()
            print("O angulo B em radianos é: " + str(angulo))
            print("O angulo B  em graus é: " + str(math.degrees(angulo)))            

    if opção == 4:
        A = float(input("Entre com o angulo 'A' do triângulo: "))
        B = float(input("Entre com o angulo 'B' do triângulo: "))

        angulo = calc.calcular_angulo_dois(A, B)
        print("O angulo desconhecido em radianos é: " + str(angulo))
        print("O angulo desconhecido em graus é: " + str(math.degrees(angulo)))

    if opção == 5:
        
        print("Caso não possua um dos valores, digite 0")

        a = float(input("Entre com o lado 'a' do triângulo: "))
        b = float(input("Entre com o lado 'b' do triângulo: "))
        c = float(input("Entre com o lado 'c' do triângulo: "))
        A = float(input("Entre com o angulo 'A' do triângulo: "))
        B = float(input("Entre com o angulo 'B' do triângulo: "))
        C = float(input("Entre com o angulo 'C' do triângulo: "))

        if A > 0 and B >0:
            C = calc.calcular_angulo_dois(A, B)
            C = math.degrees(C)
        if A > 0 and C>0:
            B = calc.calcular_angulo_dois(A, C)
            B = math.degrees(B)
        if B>0 and C>0:
            A = calc.calcular_angulo_dois(B, C)
            A = math.degrees(A)



        if A > 0 and b > 0 and B > 0:
            lado = calc.calcular_lado_A_B(b, A, B)
            a = lado
            print()
            print("O lado A é: " + str(lado))
            
        if c > 0 and A > 0 and C > 0:
            lado = calc.calcular_lado_A_C(c, A, C)
            a = lado
            print()
            print("O lado A é: " + str(lado))

        if C > 0 and b > 0 and B > 0:        
            lado = calc.calcular_lado_C_B(b, C, B)
            c = lado
            print()
            print("O lado C é: " + str(lado))

        if C > 0 and a > 0 and A > 0:        
            lado = calc.calcular_lado_C_A(a, C, A)
            c = lado
            print()
            print("O lado C é: " + str(lado))

        if A > 0 and a > 0 and B > 0:            
            lado = calc.calcular_lado_B_A(a, B, A)
            b = lado
            print()
            print("O lado B é: " + str(lado))

        if c > 0 and C > 0 and B > 0:        
            lado = calc.calcular_lado_B_C(c, C, B)
            b = lado
            print()
            print("O lado B é: " + str(lado))          

    if opção == 6:

        graus = float(input("Digite o tanto de graus para realizar a conversão: "))
        print(str(graus)+ " em radianos é: " + str(math.radians(graus)))

    if opção == 7:

        radianos = float(input("Digite o tanto de radianos para realizar o conversão: "))
        print(str(radianos)+ " em graus é: " + str(math.degrees(radianos)))

    if opção == 8:
        executar = False

print("Espero que o programa tenha sido útil, até mais")        
