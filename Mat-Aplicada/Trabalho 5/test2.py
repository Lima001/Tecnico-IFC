import numpy as np
import pygame

print("ax + by = c")
print()
a1= float(input("Digite o valor de a da primeira equação: "))
b1= float(input("Digite o valor de b da primeira equação: "))
c1= float(input("Digite o valor de c da primeira equação: "))
print("-" * 30)
a2= float(input("Digite o valor de a da segunda equação: "))
b2= float(input("Digite o valor de b da segunda equação: "))
c2= float(input("Digite o valor de c da segunda equação: "))
print()


if (a1*b2) - (b1*a2):
    
    pontos = []

    y1 = c1/b1
    x1 = c1/a1

    y2 = c2/b2
    x2 = c2/a2

    pontos.append([x1,0])
    pontos.append([0,y1])

    pontos2 = []
    pontos2.append([x2,0])
    pontos2.append([0,y2])

    lista = [[a1,b1],[a2,b2]]
    A = np.array(lista)
    B = np.array([c1,c2])
    X = np.linalg.solve(A,B)
    print(X[1], end ="/")
    print(X[0])
    
else: 
        
    cor1 = None
    cor2 = None

    cor1 = ((0,b1/c1), (a1/c1,0))
    cor2 = ((0,b2/c2), (a2/c2,0))

    if cor1 == cor2:
        print("Possivel indeterminado")

        lista = [a1,b1,c1]
        menor = min(lista)
        if menor<0:
            menor = -1*menor
            
        for i in range(menor,1,-1):
            print("aaa")
            if a1%i == 0 and b1%i == 0 and c1%i == 0:
                a1 =  a1/i
                print(a1)
                b1 = b1/i 
                print(b1)
                c1 = c1/i 
                print(c1) 
                break
        if a1<0:
            print("x,(" + str(c1) + " +" + str(a1*(-1)) + "x)/" + str(b1))
        else:
            print("x,(" + str(c1) + " -" + str(a1) + "x)/" + str(b1))  

    else:
        print("Imposivel")



