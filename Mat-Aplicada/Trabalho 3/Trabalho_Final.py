import pygame

#Desenha uma linha, matriz por matriz
def desenhar_linha(x0,x1,x2,x3,y,y2):
    matriz1 = []
    matriz2 = []
    matriz3 = []
    matriz4 = []


    for z in range(len(y0)):
        matriz1.append([x0[z],y[z]])
        matriz2.append([x1[z],y2[z]])
        matriz3.append([x2[z],y[z]])
        matriz4.append([x3[z],y2[z]])

    pygame.draw.polygon(tela,(0,255,0), matriz1)
    pygame.draw.polygon(tela,(0,255,255), matriz2)
    pygame.draw.polygon(tela,(0,255,0), matriz3)
    pygame.draw.polygon(tela,(0,255,255), matriz4)
      
x0 = eval('[' + input("Digite a primeira linha da matriz: ") + ']')
y0 = eval('[' + input("Digite a segunda linha da matriz: ") + ']')

#x0 = [0,7,7,4,5,6,6,3,4,3]
#y0 = [7,7,0,3,4,3,6,6,5,4]


maior_x = max(x0) 
maior_y = max(y0)

x1 = []
x2 = []
x3 =[]

y1 = []
y2 = []
y3 = []

#Calcula as outras matrizes
for elemento in range(len(x0)):
    x1.append(x0[elemento]+maior_x)
    x2.append(x1[elemento]+maior_x)
    x3.append(x2[elemento]+maior_x)
        

for elemento in range(len(y0)):
    y1.append(y0[elemento]+maior_y)
    y2.append(y1[elemento]+maior_y)
    y3.append(y2[elemento]+maior_y)


#Calculos que serão usados posteriormentes
valor_x = (800/4)/maior_x
valor_y = (600/4)/maior_y

multiplicador = 0

if valor_y < valor_x:
    multiplicador = valor_y
else:
    multiplicador = valor_x
    
comprimento_x = max(x0) - min(x0)
comprimento_y = max(y0) - min(y0)

#Crio outras matrizes para realizar calculos e não afetar as principais (x0,y0,x1,y1 ...)    
y00 = y0.copy()    
y11 = y1.copy()
y22 = y2.copy()
y33 = y3.copy()

x00 = x0.copy()
x11 = x1.copy()
x33 = x3.copy()
x22 = x2.copy()
x111 = x1.copy()
x333 = x3.copy()

#Aqui é importante, aqui é praticamente a base pra realizar os outros desenhos, pois é onde eu os inverto (Multiplicando por -1) e ajeito sua posição, uma vez que vão pro lado negativo da tela, o qual não dá pra ver, por isso a adição do comprimento das listas
for z in range(len(y0)):
    x00[z] = (x0[z] *-1) + (1*comprimento_x)
    x11[z] = (x1[z] *-1) + (3*comprimento_x)
    x22[z] = (x2[z] *-1) + (5*comprimento_x)
    x33[z] = (x3[z] *-1) + (7*comprimento_x)
    x111[z] = (x111[z] *-1) + (3*comprimento_x)
    x333[z] = (x333[z] *-1) + (7*comprimento_x)
    
    y00[z] = (y00[z] *-1) + (1*comprimento_y)
    y11[z] = (y11[z] *-1) + (3*comprimento_y)
    y22[z] = (y22[z] *-1) + (5*comprimento_y)
    y33[z] = (y33[z] *-1) + (7*comprimento_y)

#Imprimir as matrzies que o professor pediu
print("Matriz desenho 1")
print(x3)
print(y3)
print()

print("Matriz desenho 2")
print(x2)
print(y2)
print()
print(x333)
print(y2)
print()
print(x2)
print(y33)
print()
print(x333)
print(y33)
print()

print("Matriz desenho 3")
print(x22[1:], end ="")
print(x22[0:1])
print(y33[1:], end="")
print(y33[0:1])
print()
print(x3)
print(y3)

#Arrumar os desenhos para ficarem dentro da tela do pygame
for elemento in range(len(x0)):
    x0[elemento] = x0[elemento] * multiplicador
    x1[elemento] = x1[elemento] * multiplicador
    x2[elemento] = x2[elemento] * multiplicador
    x3[elemento] = x3[elemento] * multiplicador
    x00[elemento] = x00[elemento] * multiplicador
    x11[elemento] = x11[elemento] * multiplicador
    x22[elemento] = x22[elemento] * multiplicador
    x33[elemento] = x33[elemento] * multiplicador
    x111[elemento] = x111[elemento] * multiplicador
    x333[elemento] = x333[elemento] * multiplicador
        
    y0[elemento] = y0[elemento] * multiplicador
    y1[elemento] = y1[elemento] * multiplicador
    y2[elemento] = y2[elemento] * multiplicador
    y3[elemento] = y3[elemento] * multiplicador
    y00[elemento] = y00[elemento] * multiplicador
    y11[elemento] = y11[elemento] * multiplicador
    y22[elemento] = y22[elemento] * multiplicador
    y33[elemento] = y33[elemento] * multiplicador

#Inicialização do pygame    
pygame.init()

#Primeiro desenho
tela = pygame.display.set_mode((800, 600), 0, 32)
tela.fill((0,0,0))

desenhar_linha(x0,x1,x2,x3,y0,y0)
desenhar_linha(x0,x1,x2,x3,y1,y1)
desenhar_linha(x0,x1,x2,x3,y2,y2)
desenhar_linha(x0,x1,x2,x3,y3,y3)
pygame.display.update()

#Serve para trocar o desenho, pois em quanto a pessoa não der um enter, não vai sair do input, e quando sair ele desenha a próxima imagem
exe = True
while exe:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            exe = False

#Seegundo desenho
tela = pygame.display.set_mode((800, 600), 0, 32)
tela.fill((0,0,0))

desenhar_linha(x0,x111,x2,x333,y0,y0)
desenhar_linha(x0,x111,x2,x333,y11,y11)
desenhar_linha(x0,x111,x2,x333,y2,y2)
desenhar_linha(x0,x111,x2,x333,y33,y33)
pygame.display.update()

exe = True
while exe:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            exe = False

#Terceiro desenho
tela = pygame.display.set_mode((800, 600), 0, 32)
tela.fill((0,0,0))

desenhar_linha(x0,x11,x2,x33,y0,y00)
desenhar_linha(x00,x1,x22,x3,y11,y1)
desenhar_linha(x0,x11,x2,x33,y2,y22)
desenhar_linha(x00,x1,x22,x3,y33,y3)
pygame.display.update()

#Parte para poder fechar a tela do pygame apertando no x padrão
exe = True
while exe :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exe = False
            exit()
