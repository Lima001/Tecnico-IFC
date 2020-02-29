
import pygame

matrizes=[]

def listar_lista(lista):
    nova_lista=[]
    for i in lista:
        nova_lista.append(list(i))
    return nova_lista


def desenhar_linha(pontos,max_x):
    lista_pontos=listar_lista(pontos)
    for i in range(4):
        matrizes.append(list(listar_lista(lista_pontos)))
        for i in lista_pontos:
            i[0]+=max_x
    return matrizes

def desenhar_varias_linhas(pontos):
    max_x=descobrir_max(pontos,0)
    max_y=descobrir_max(pontos,1)
    lista_pontos=listar_lista(pontos)
    for i in range(4):
        desenhar_linha(lista_pontos,max_x)
        for i in lista_pontos:
            i[1]+=max_y


def descobrir_max(pontos,x_y):
    max=0
    for i in pontos:
        if i[x_y]>max:
            max=i[x_y]
    return max

def desenho_padrão():
    desenhar_varias_linhas(pontos)
    for i in matrizes:
        pygame.draw.polygon(tela,(0,255,0), i)

def printar_4x4():
    matriz_4x4=[]
    for i in matrizes[15]:
        matriz_4x4.append([(i[0]/tamanho_maior),(i[1]/tamanho_maior)])
    return matriz_4x4



def desenho_2():
    desenhar_varias_linhas(pontos)
    valor_somado_x=descobrir_max(matrizes[0],0)
    valor_somado_y=descobrir_max(matrizes[0],1)
    for i in range(len(matrizes)):
        for y in range(len(matrizes[i])):
            if i%2!=0:
                matrizes[i][y][0]*=-1
                if i not in [3,7,11,15]:
                     matrizes[i][y][0]+=3*valor_somado_x
                else:
                    matrizes[i][y][0]+=7*valor_somado_x
            
            if i in [4,5,6,7]:
                matrizes[i][y][1]*=-1
                matrizes[i][y][1]+=3*valor_somado_y
            if i in [12,13,14,15]:
                matrizes[i][y][1]*=-1
                matrizes[i][y][1]+=7*valor_somado_y            
               
                
    for i in matrizes:
        pygame.draw.polygon(tela,(0,255,0), i)




pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
tela.fill((0,0,0))
 
pontos=[[0,7],[7,7],[7,0],[4,3],[5,4],[6,3],[6,6],[3,6],[4,5],[3,4]]

tamanho_x=200/descobrir_max(pontos,0)
tamanho_y=150/descobrir_max(pontos,1)

if tamanho_x<tamanho_y:
    tamanho_maior=tamanho_x
else:
    tamanho_maior=tamanho_y

for i in pontos:
    i[0]=i[0]*tamanho_maior
    i[1]=i[1]*tamanho_maior

desenho_2()
print(printar_4x4())

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
