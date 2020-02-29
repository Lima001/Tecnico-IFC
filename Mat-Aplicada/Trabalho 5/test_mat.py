import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.ticker as ticker
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

def desenhar(x,y,x2=None,y2=None,s=None):
    fig, ax = plt.subplots()
    ax.plot(x,y, color="g")
    ax.plot(x2,y2, color="r")
    if s is not None:
        vx = (np.arange(s-10,s+10,1.0))
    else:
        vx = (np.arange(-10,11,1.0))
    ax.set_title("A", fontweight= "bold")
    ax.set_xlabel("Valores de X")
    ax.set_ylabel("Valores de Y")
    
    ax.set_xticks(vx)

    ax.grid(True, linestyle='--')
    ax.tick_params(labelcolor="b", labelsize='medium', width=3)
    plt.show()

def desenhar2(x,y):
    fig, ax = plt.subplots()
    ax.plot(x,y, color="g")
    vx = (np.arange(-10,11,1.0))   
    ax.set_title("A", fontweight= "bold")
    ax.set_xlabel("Valores de X")
    ax.set_ylabel("Valores de Y")
    
    ax.set_xticks(vx)

    ax.grid(True, linestyle='--')
    ax.tick_params(labelcolor="b", labelsize='medium', width=3)
    plt.show()

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
    print("Sistema Possível Determinado")
    print("Solução: " , end="")
    print(X[0], end ="/")
    print(X[1])
    print(X)
    print(type(X))
    print(len(X))
    x = (np.arange(X[0]-10,X[0]+10,0.1))
    y = (c1 - (x*a1))/b1

    x2 = (np.arange(X[0]-10,X[0]+10,0.1))
    y2 = (c2 - (x2*a2))/b2 
    desenhar(x,y,x2,y2,X[0])


    
else: 
        
    cor1 = None
    cor2 = None

    cor1 = ((0,c1/b1), (c1/a1,0))
    cor2 = ((0,c2/b2), (c2/a2,0))

    if cor1 == cor2:
        print("Possivel indeterminado")

        lista = [a1,b1,c1]
        menor = min(lista)
        if menor<0:
            menor = -1*menor 

        if round(menor) == menor:
            for i in range(int(menor),1,-1):
                if a1%i == 0 and b1%i == 0 and c1%i == 0:
                    a1 =  a1/i
                    b1 = b1/i 
                    c1 = c1/i 
                    break

            if a1 < 0:
                print("x,(" + str(c1) + " +" + str(a1*(-1)) + "x)/" + str(b1))
            else:
                print("x,(" + str(c1) + " -" + str(a1) + "x)/" + str(b1))  
        else:
            if a1 < 0:
                print("x,(" + str(c1) + " +" + str(a1*(-1)) + "x)/" + str(b1))
            else:
                print("x,(" + str(c1) + " -" + str(a1) + "x)/" + str(b1))

        #ax by =c
        #
        x = (np.arange(0-10,-+10,0.1))
        y = (c2 - (x*a2))/b2 
        desenhar2(x,y) 

    else:
        print("Imposivel")

        x1 = (np.arange(-10,10,0.1))
        y1 = (c1 - (x1*a1)/b1)

        x2 = (np.arange(-10,10,0.1))
        y2 = (c2 - (x2*a2)/b2)

        desenhar(x1,y1,x2,y2)

