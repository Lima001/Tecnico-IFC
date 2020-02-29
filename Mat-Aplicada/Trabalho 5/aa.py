import numpy as np

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


if True:
    
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
    print("Sistema Possível Determinado")
    print("Solução: " , end="")
    print(X[0], end ="/")
    print(X[1])
