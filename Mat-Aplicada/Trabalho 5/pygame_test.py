import numpy as np
import pygame
        
def desenhar_grafico_1(ponto_inicial,ponto_final,cor,tipo=None,ponto_inicial_2=None,ponto_final_2=None):

    pygame.init()
    
    font = pygame.font.SysFont(None, 15)
    tela = pygame.display.set_mode((820, 620))
    tela.fill((255,255,255))
     
    pygame.draw.line(tela, (0,0,0), (0,300), (820,300),2)
    pygame.draw.line(tela, (0,0,0), (400,0), (400,620),2)

    cont = -13
    for x in range(0,850,30):
        texto = font.render(str(cont), True, (0,0,0))
        tela.blit(texto, (x+8,300+5))
        cont += 1

    cont = 10
    for y in range(0,600,30):
        if cont != 0:
            texto = font.render(str(cont), True, (0,0,0))
            tela.blit(texto, (400+5,y))
        cont -= 1
    
    if tipo is None:
        pygame.display.set_caption('Possível Indeterminado')
        ponto_1 = ((400 + ponto_inicial[0]*30), (300 - ponto_inicial[1]*30))
        ponto_2 = ((400 + ponto_final[0]*30) , (300 - ponto_final[1]*30))
        pygame.draw.line(tela, cor, ponto_1, ponto_2,2)
        pygame.display.update()

    else:
        pygame.display.set_caption('Impossível')
        ponto_1 = ((400 + ponto_inicial[0]*30), (300 - ponto_inicial[1]*30))
        ponto_2 = ((400 + ponto_final[0]*30) , (300 - ponto_final[1]*30))
        pygame.draw.line(tela, cor[0], ponto_1, ponto_2,2)

        ponto_3 = ((400 + ponto_inicial_2[0]*30), (300 - ponto_inicial_2[1]*30))
        ponto_4 = ((400 + ponto_final_2[0]*30) , (300 - ponto_final_2[1]*30))
        pygame.draw.line(tela, cor[1], ponto_3, ponto_4,2)

        pygame.display.update()

def desenhar_grafico_2(a1,b1,c1,a2,b2,c2,cor,solucao):

    valores = []
    for x in solucao:
        if x < 0:
            valores.append(x*-1)
        else:
            valores.append(x)

    maior = max(valores)

    divisor = int(round(300/(maior+1)))

    pygame.init()

    font = pygame.font.SysFont(None, 15)


    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Possível Determinado')

    tela.fill((255,255,255))

     
    pygame.draw.line(tela, (0,0,0), (0,300), (820,300),2)
    pygame.draw.line(tela, (0,0,0), (400,0), (400,620),2)

    cont = 0
    for x in range(400,850,int(divisor)):
        texto = font.render(str(cont), True, (0,0,0))
        tela.blit(texto, (x-5,300+5))
        cont += 1

    v = cont
    vn = cont * -1
        
    cont = 0
    for x in range(400,0,int(divisor)*-1):
        if cont !=0:
            texto = font.render(str(cont), True, (0,0,0))
            tela.blit(texto, (x-5,300+5))
        cont -= 1




    cont = int(maior+1)
    for y in range(0,300,int(divisor)):
        if cont != 0:
            texto = font.render(str(cont), True, (0,0,0))
            tela.blit(texto, (400+5,y-5))
        cont -= 1

    cont = 0
    for y in range(300,650,int(divisor)):
        if cont != 0:
            texto = font.render(str(cont), True, (0,0,0))
            tela.blit(texto, (400+5,y-5))
        cont -= 1

    ponto_1 = (400 + ((v)*divisor), 300 - ((c1 - (a1*v))/b1)*divisor)
    ponto_2 = (400 + ((c1- (b1*(maior+1)))/a1)*divisor , 300 - ((maior+1)*divisor))
    pygame.draw.line(tela, cor[0], ponto_1, ponto_2,2)

    ponto_3 = (400 + ((v)*divisor), 300 - ((c2 - (a2*v))/b2)*divisor)
    ponto_4 = (400 + ((c2 - (b2*(maior+1)))/a2)*divisor , 300 - ((maior+1)*divisor))
    pygame.draw.line(tela, cor[1], ponto_3, ponto_4,2)


    ponto_1 = (400 + ((vn)*divisor), 300 - ((c1 - (a1*vn))/b1)*divisor)
    ponto_2 = (400 + ((c1- (b1*(maior+1)))/a1)*divisor , 300 - ((maior+1)*divisor))
    pygame.draw.line(tela, cor[0], ponto_1, ponto_2,2)

    ponto_3 = (400 + ((vn)*divisor), 300 - ((c2 - (a2*vn))/b2)*divisor)
    ponto_4 = (400 + ((c2 - (b2*(maior+1)))/a2)*divisor , 300 - ((maior+1)*divisor))
    pygame.draw.line(tela, cor[1], ponto_3, ponto_4,2)

    ponto = (int(400 + (solucao[1]*divisor)), int(300 - (solucao[0]*divisor)))
    pygame.draw.circle(tela, (0,0,0), (ponto[0],ponto[1]), 5)

    pygame.display.update()

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
    print("Sistema Possível Determinado")
    print("Solução: " , end="")
    print(X[0], end ="/")
    print(X[1])


    desenhar_grafico_2(a1,b1,c1,a2,b2,c2,((0,255,0),(255,255,0)),(X[1],X[0]))
    
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
                    #print(a1)
                    b1 = b1/i 
                    #print(b1)
                    c1 = c1/i 
                    #print(c1) 
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


        ponto_inicial = (13, (c1 - (a1*(+13)))/b1)
        ponto_final = (-13, (c1 - (a1*(-13)))/b1)

        desenhar_grafico_1(ponto_inicial,ponto_final,(255,110,255))

    else:
        print("Imposivel")

        ponto_inicial = (13, (c1 - (a1*(+13)))/b1)
        ponto_final = (-13, (c1 - (a1*(-13)))/b1)

        ponto_inicial_2 = (13, (c2 - (a2*(+13)))/b2)
        ponto_final_2 = (-13, (c2 - (a2*(-13)))/b2)

        desenhar_grafico_1(ponto_inicial,ponto_final,((255,0,0),(0,0,255)),1,ponto_inicial_2,ponto_final_2)
