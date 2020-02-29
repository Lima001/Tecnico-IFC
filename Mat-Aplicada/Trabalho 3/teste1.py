import pygame

def desenhar_linha(x0,x1,x2,x3,y):
    matriz1 = []
    matriz2 = []
    matriz3 = []
    matriz4 = []


    for z in range(len(y0)):
        matriz1.append([x0[z],y[z]])
        matriz2.append([x1[z],y[z]])
        matriz3.append([x2[z],y[z]])
        matriz4.append([x3[z],y[z]])

    pygame.draw.polygon(tela,(0,255,0), matriz1)
    pygame.draw.polygon(tela,(0,255,255), matriz2)
    pygame.draw.polygon(tela,(0,255,0), matriz3)
    pygame.draw.polygon(tela,(0,255,255), matriz4)
      
#x0 = eval('[' + input("Digite a primeira linha da matriz: ") + ']')
#y0 = eval('[' + input("Digite a segunda linha da matriz: ") + ']')

x0 = [0,7,7,4,5,6,6,3,4,3]
y0 = [7,7,0,3,4,3,6,6,5,4]

maior_x = max(x0) 
maior_y = max(y0)

x1 = []
x2 = []
x3 =[]

y1 = []
y2 = []
y3 = []

for elemento in range(len(x0)):
    x1.append(x0[elemento]+maior_x)
    x2.append(x1[elemento]+maior_x)
    x3.append(x2[elemento]+maior_x)
        

for elemento in range(len(y0)):
    y1.append(y0[elemento]+maior_y)
    y2.append(y1[elemento]+maior_y)
    y3.append(y2[elemento]+maior_y)
    
print(x3)
print(y3)

valor_x = (800/4)/maior_x
valor_y = (600/4)/maior_y

multiplicador = 0

if valor_y < valor_x:
    multiplicador = valor_y
else:
    multiplicador = valor_x

for elemento in range(len(x0)):
    x0[elemento] = x0[elemento] * multiplicador
    x1[elemento] = x1[elemento] * multiplicador
    x2[elemento] = x2[elemento] * multiplicador
    x3[elemento] = x3[elemento] * multiplicador
        
    y0[elemento] = y0[elemento] * multiplicador
    y1[elemento] = y1[elemento] * multiplicador
    y2[elemento] = y2[elemento] * multiplicador
    y3[elemento] = y3[elemento] * multiplicador

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
tela.fill((0,0,0))

desenhar_linha(x0,x1,x2,x3,y0)
desenhar_linha(x0,x1,x2,x3,y1)
desenhar_linha(x0,x1,x2,x3,y2)
desenhar_linha(x0,x1,x2,x3,y3)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
