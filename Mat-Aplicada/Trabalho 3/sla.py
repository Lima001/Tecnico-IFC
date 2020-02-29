import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 640
tela = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
tela.fill((0,0,0))

for x in range(4):
    poligono = [[0,70],[70,70],[70,0],[40,30],[50,40],[60,30],[60,60],[30,60],[40,50],[30,40]]
    for j in range(4):
        pygame.draw.polygon(tela, (255,0,255), poligono)
        for i in range(len(poligono)):
          poligono[i][1] += 70
    for j in range(4):
        pygame.draw.polygon(tela, (255,0,255), poligono)
        for i in range(len(poligono)):
          poligono[i][0] += 70


'''
for j in range(4):

    pygame.draw.polygon(tela, (255,0,255), poligono)
    for i in range(len(poligono)):
        poligono[i][1] += 70
    print(poligono)
'''
pygame.exit()
