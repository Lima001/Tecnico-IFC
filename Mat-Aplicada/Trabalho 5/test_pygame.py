import pygame

s = (4,9)

divisor_x = 400/4
divisor_y = 300/10

pygame.init()

font = pygame.font.SysFont(None, 20)


tela = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Olá mundo')

tela.fill((255,255,255))

 
pygame.draw.line(tela, (0,0,0), (0,300), (820,300),2)
pygame.draw.line(tela, (0,0,0), (400,0), (400,620),2)

cont = 0
for x in range(400,850,int(divisor_y)):
    texto = font.render(str(cont), True, (0,0,0))
    tela.blit(texto, (x-5,300+5))
    cont += 1
    
cont = -14
for x in range(0,400,int(divisor_y)):
    if cont !=0:
        texto = font.render(str(cont), True, (0,0,0))
        tela.blit(texto, (x-5,300+5))
    cont += 1




cont = 9
for y in range(0,300,int(divisor_y)):
    if cont != 0:
        texto = font.render(str(cont), True, (0,0,0))
        tela.blit(texto, (400+5,y-5))
    cont -= 1
cont = 0
for y in range(300,650,int(divisor_y)):
    if cont != 0:
        texto = font.render(str(cont), True, (0,0,0))
        tela.blit(texto, (400+5,y-5))
    cont -= 1

ponto_inicial = ((400 + ((0)*divisor_y)), (300 - (15*divisor_y)))
ponto_final = ((400 + (10*divisor_y)) , (300 - 0*divisor_y))
pygame.draw.line(tela, (255,0,0), ponto_inicial, ponto_final,2)


ponto_inicial = ((400 + ((0)*divisor_y)), (300 - (17*divisor_y)))
ponto_final = ((400 + (8.5*divisor_y)) , (300 - 0*divisor_y))
pygame.draw.line(tela, (255,0,0), ponto_inicial, ponto_final,2)
#ponto_inicial = ((400 + (13*30)), (300 - ((6 -26)/4)*30))
#ponto_final = ((400 + (-13*30)) , (300 - ((6 +26)/4)*30))
#pygame.draw.line(tela, (255,255,0), ponto_inicial, ponto_final,2)

pygame.display.update()
