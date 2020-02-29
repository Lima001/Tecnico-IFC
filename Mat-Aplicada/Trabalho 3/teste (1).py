import pygame

#x0 = eval('[' + input("Digite a primeira linha da matriz: ") + ']')
#y0 = eval('[' + input("Digite a segunda linha da matriz: ") + ']')

x0 = [0,7,7,4,5,6,6,3,4,3]
y0 = [7,7,0,3,4,3,6,6,5,4]



matriz_base = [[0,7],[7,7],[7,0],[4,3],[5,4],[6,3],[6,6],[3,6],[4,5],[3,4]]
matriz_2 = matriz_base.copy()

maior_x= 7
maior_y = 7

valor_x = 200/7
valor_y = 150/7



for x in range(len(matriz_base)):
    matriz_base[x][0] = matriz_base[x][0] * valor_y 
    matriz_base[x][1] = matriz_base[x][1]* valor_y

pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)
tela.fill((0,0,0))
pygame.draw.polygon(tela,(0,255,0), matriz_base)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
