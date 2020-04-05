import pygame
import math as mat
import variaveis
from pygame import *
from random import randint

pygame.init()

#=================MENU==========================
class Pagina:

    def __init__(self,fundo):
        self.fundo=fundo
        self.lista_objetos = []
        init()
        self.largura = 800
        self.altura = 600
        self.tela = display.set_mode((self.largura,self.altura))

    def blitar_botoes(self):
        for i in self.lista_objetos:
            i.blitar()

    def rodar_pagina(self):
        while True:
            self.tela.fill((105,105,105))
            self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
            self.click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    sair()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click=True
            self.blitar_botoes()
            display.update()

class Botao_texto():

    def __init__(self,texto,bot_x,bot_y,tam_x,tam_y,fonte,espasamento,pagina,funcao=None,atributos=None):
        self.bot_x = bot_x
        self.bot_y = bot_y
        self.funcao = funcao
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.atributos = atributos
        self.espasamento = espasamento
        self.fonte = font.Font(fonte, 200)
        self.imagem = self.fonte.render(texto, True, (255,255,255))
        self.pagina = pagina
        divisor = min(self.imagem.get_rect()[2],self.imagem.get_rect()[3])/min(tam_x,tam_y)
        self.imagem = transform.scale(self.imagem,(int(self.imagem.get_rect()[2]/divisor),int(self.imagem.get_rect()[3]/divisor)))

    def blitar(self):
        if self.pagina.mouse_x in range(self.bot_x-self.espasamento,self.bot_x+self.tam_x+self.espasamento):
            if self.pagina.mouse_y in range(self.bot_y-self.espasamento,self.bot_y+self.tam_y+self.espasamento):
                draw.rect(self.pagina.tela,(0,255,0),(self.bot_x-self.espasamento,self.bot_y-self.espasamento,self.tam_x+2*self.espasamento,self.tam_y+2*self.espasamento))
                if self.pagina.click:
                    self.funcao(self.atributos)
               
                        
        self.pagina.tela.blit(self.imagem,(self.bot_x,self.bot_y))

class Botao_imagem():
    def __init__(self,imagem,bot_x,bot_y,tam_x,tam_y,espasamento,pagina,funcao=None,atributos=None):
        self.bot_x = bot_x
        self.bot_y = bot_y
        self.funcao = funcao
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.espasamento = espasamento
        self.imagem = image.load(imagem)
        self.pagina = pagina
        self.atributos = atributos
        self.imagem = transform.scale(self.imagem,(tam_x,tam_y))
        self.imagem_com_espasamento = transform.scale(self.imagem,(2*self.espasamento+tam_x,2*self.espasamento+tam_y))

    def blitar(self):
        if self.pagina.mouse_x in range(self.bot_x-self.espasamento,self.bot_x+self.tam_x+self.espasamento):
            if self.pagina.mouse_y in range(self.bot_y-self.espasamento,self.bot_y+self.tam_y+self.espasamento):
                self.pagina.tela.blit(self.imagem_com_espasamento,(self.bot_x-self.espasamento, self.bot_y-self.espasamento))
                if self.pagina.click:
                    self.funcao(self.atributos)
            else:
                self.pagina.tela.blit(self.imagem,(self.bot_x,self.bot_y))
        else:
            self.pagina.tela.blit(self.imagem,(self.bot_x,self.bot_y))
class Texto():
    def __init__(self,texto,tex_x,tex_y,tam_x,tam_y,fonte,pagina,color=(255,255,255)):
        self.tex_x = tex_x
        self.tex_y = tex_y
        self.tam_x = tam_x
        self.tam_y = tam_y
        self.fonte = font.Font(fonte, 200)
        self.imagem = self.fonte.render(texto, True, color)
        self.pagina = pagina
        divisor = min(self.imagem.get_rect()[2],self.imagem.get_rect()[3])/min(tam_x,tam_y)
        self.imagem = transform.scale(self.imagem,(int(self.imagem.get_rect()[2]/divisor),int(self.imagem.get_rect()[3]/divisor)))
    def blitar(self):
        self.pagina.tela.blit(self.imagem,(self.tex_x,self.tex_y))

#PAGINAS

def executar_menu_principal(null=None):
    pagina = Pagina((0,0,0))
    objetos = [Botao_texto("Jogar",20,350,140,70,"bebas.ttf",5,pagina,jogo.loop),
    Botao_texto("Loja",20,430,140,70,"bebas.ttf",5,pagina,executar_loja_pg0,True),
    Botao_texto("Sair",20,510,140,70,"bebas.ttf",5,pagina,sair),
    Texto("DROMME",160,20,400,150,"fonte.ttf",pagina)]
    for i in objetos:
        pagina.lista_objetos.append(i)
    pagina.rodar_pagina()

def executar_loja_pg0(menu):
    pagina = Pagina((0,0,0))
    objetos = [Texto("$",10,10,20,20,"bebas.ttf",pagina,(0,255,0)),
    Texto("$ " + str(variaveis.lista_armas[3].texto),10,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_armas[4].texto),275,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_armas[5].texto),540,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Botao_imagem(variaveis.lista_armas[3].imagem_lateral,10,170,250,67,10,pagina,comprar_arma,[variaveis.lista_armas[3],menu]),
    Botao_imagem(variaveis.lista_armas[4].imagem_lateral,275,170,250,67,10,pagina,comprar_arma,[variaveis.lista_armas[4],menu]),
    Botao_imagem(variaveis.lista_armas[5].imagem_lateral,540,170,250,67,10,pagina,comprar_arma,[variaveis.lista_armas[5],menu]),
    Botao_texto("Anterior",220,450,130,40,"bebas.ttf",5,pagina,printar1),
    Botao_texto("Proximo",410,450,130,45,"bebas.ttf",5,pagina,executar_loja_pg1,menu),
    Texto(str(variaveis.dinheiro),35,15,40,40,"bebas.ttf",pagina,(0,255,0))]
    if menu==True:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,executar_menu_principal))
    else:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,voltar))

    for i in objetos:
        pagina.lista_objetos.append(i)
    pagina.rodar_pagina()  

def executar_loja_pg1(menu):
    pagina = Pagina((0,0,0))
    objetos = [Texto("$",10,10,20,20,"bebas.ttf",pagina,(0,255,0)),
    Texto("$ " + str(variaveis.lista_armas[0].texto),10,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_armas[1].texto),275,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_armas[2].texto),570,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Botao_imagem(variaveis.lista_armas[0].imagem_lateral,10,170,250,67,10,pagina,comprar_arma,[variaveis.lista_armas[0],menu]),
    Botao_imagem(variaveis.lista_armas[1].imagem_lateral,275,170,250,67,10,pagina,comprar_arma,[variaveis.lista_armas[1],menu]),
    Botao_imagem(variaveis.lista_armas[2].imagem_lateral,570,170,100,67,10,pagina,comprar_arma,[variaveis.lista_armas[2],menu]),
    Botao_texto("Anterior",220,450,130,40,"bebas.ttf",5,pagina,executar_loja_pg0,menu),
    Botao_texto("Proximo",410,450,130,45,"bebas.ttf",5,pagina,executar_loja_pg2,menu),
    Texto(str(variaveis.dinheiro),35,15,40,40,"bebas.ttf",pagina,(0,255,0))]
    if menu==True:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,executar_menu_principal))
    else:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,voltar))
    for i in objetos:
        pagina.lista_objetos.append(i)
    pagina.rodar_pagina()

def executar_loja_pg2(menu):
    pagina = Pagina((0,0,0))
    objetos = [Texto("$",10,10,20,20,"bebas.ttf",pagina,(0,255,0)),
    Texto("$ " + str(variaveis.preco_incremento_vida),60,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.preco_incremento_municao),325,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_skin[0].texto),600,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Botao_imagem(variaveis.imagem_kit,100,170,67,67,10,pagina,comprar_incremento_vida),
    Botao_imagem(variaveis.imagem_municao,365,170,67,67,10,pagina,comprar_incremento_municao),
    Botao_imagem(variaveis.lista_skin[0].endereco_imagem,630,170,80,80,10,pagina,comprar_skin_personagem, [variaveis.lista_skin[0],menu]),
    Botao_texto("Anterior",220,450,130,40,"bebas.ttf",5,pagina,executar_loja_pg1,menu),
    Botao_texto("Proximo",410,450,130,45,"bebas.ttf",5,pagina,executar_loja_pg3,menu),
    Texto(str(variaveis.dinheiro),35,15,40,40,"bebas.ttf",pagina,(0,255,0))]
    if menu==True:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,executar_menu_principal))
    else:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,voltar))
    for i in objetos:
        pagina.lista_objetos.append(i)
    pagina.rodar_pagina()

def executar_loja_pg3(menu):
    pagina = Pagina((0,0,0))
    objetos = [Texto("$",10,10,20,20,"bebas.ttf",pagina,(0,255,0)),
    Texto("$ " + str(variaveis.lista_skin[1].texto),60,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_skin[2].texto),325,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_skin[3].texto),600,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Botao_imagem(variaveis.lista_skin[1].endereco_imagem,100,170,67,67,10,pagina,comprar_skin_personagem, [variaveis.lista_skin[1],menu]),
    Botao_imagem(variaveis.lista_skin[2].endereco_imagem,365,170,67,67,10,pagina,comprar_skin_personagem, [variaveis.lista_skin[2],menu]),
    Botao_imagem(variaveis.lista_skin[3].endereco_imagem,630,170,80,80,10,pagina,comprar_skin_personagem, [variaveis.lista_skin[3],menu]),
    Botao_texto("Anterior",220,450,130,40,"bebas.ttf",5,pagina,executar_loja_pg2,menu),
    Botao_texto("Proximo",410,450,130,45,"bebas.ttf",5,pagina,executar_loja_pg4,menu),
    Texto(str(variaveis.dinheiro),35,15,40,40,"bebas.ttf",pagina,(0,255,0))]
    if menu==True:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,executar_menu_principal))
    else:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,voltar))
    for i in objetos:
        pagina.lista_objetos.append(i)
    pagina.rodar_pagina()

def executar_loja_pg4(menu):
    pagina = Pagina((0,0,0))
    objetos = [Texto("$",10,10,20,20,"bebas.ttf",pagina,(0,255,0)),
    Texto("$ " + str(variaveis.lista_skin[4].texto),60,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_skin[5].texto),325,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_skin[6].texto),600,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Botao_imagem(variaveis.lista_skin[4].endereco_imagem,100,170,67,67,10,pagina,comprar_skin_personagem, [variaveis.lista_skin[4],menu]),
    Botao_imagem(variaveis.lista_skin[5].endereco_imagem,365,170,67,67,10,pagina,comprar_skin_personagem, [variaveis.lista_skin[5],menu]),
    Botao_imagem(variaveis.lista_skin[6].endereco_imagem,630,170,80,80,10,pagina,comprar_skin_personagem, [variaveis.lista_skin[6],menu]),
    Botao_texto("Anterior",220,450,130,40,"bebas.ttf",5,pagina,executar_loja_pg3,menu),
    Botao_texto("Proximo",410,450,130,45,"bebas.ttf",5,pagina,executar_loja_pg5,menu),
    Texto(str(variaveis.dinheiro),35,15,40,40,"bebas.ttf",pagina,(0,255,0))]
    if menu==True:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,executar_menu_principal))
    else:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,voltar))
    for i in objetos:
        pagina.lista_objetos.append(i)
    pagina.rodar_pagina()

def executar_loja_pg5(menu):
    pagina = Pagina((0,0,0))
    objetos = [Texto("$",10,10,20,20,"bebas.ttf",pagina,(0,255,0)),
    Texto("$ " + str(variaveis.lista_skin[7].texto),60,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_skin[8].texto),325,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Texto("$ " + str(variaveis.lista_skin[9].texto),600,300,40,40,"bebas.ttf",pagina,(255,255,0)),
    Botao_imagem(variaveis.lista_skin[7].endereco_imagem,100,170,67,67,10,pagina,comprar_skin_personagem, [variaveis.lista_skin[7],menu]),
    Botao_imagem(variaveis.lista_skin[8].endereco_imagem,365,170,67,67,10,pagina,comprar_skin_personagem, [variaveis.lista_skin[8],menu]),
    Botao_imagem(variaveis.lista_skin[9].endereco_imagem,630,170,80,80,10,pagina,comprar_skin_personagem, [variaveis.lista_skin[9],menu]),
    Botao_texto("Anterior",220,450,130,40,"bebas.ttf",5,pagina,executar_loja_pg4,menu),
    Botao_texto("Proximo",410,450,130,45,"bebas.ttf",5,pagina,printar1),
    Texto(str(variaveis.dinheiro),35,15,40,40,"bebas.ttf",pagina,(0,255,0))]
    if menu==True:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,executar_menu_principal))
    else:
        objetos.append(Botao_texto("Voltar",20,520,150,60,"bebas.ttf",5,pagina,voltar))
    for i in objetos:
        pagina.lista_objetos.append(i)
    pagina.rodar_pagina()

def historinha1(nada):
    pagina = Pagina((0,0,0))
    botao_historinha = Botao_imagem("historinha1.jpeg",20,20,760,560,10,pagina,historinha2)
    pagina.lista_objetos = [botao_historinha]
    pagina.rodar_pagina()

def historinha2(nada):
    pagina = Pagina((0,0,0))
    botao_historinha = Botao_imagem("historinha2.jpeg",20,20,760,560,10,pagina,historinha3)
    pagina.lista_objetos = [botao_historinha]
    pagina.rodar_pagina()

def historinha3(nada):
    pagina = Pagina((0,0,0))
    botao_historinha = Botao_imagem("historinha3.jpeg",20,20,760,560,10,pagina,historinha4)
    pagina.lista_objetos = [botao_historinha]
    pagina.rodar_pagina()

def historinha4(nada):
    pagina = Pagina((0,0,0))
    botao_historinha = Botao_imagem("historinha4.jpeg",20,20,760,560,10,pagina,historinha5)
    pagina.lista_objetos = [botao_historinha]
    pagina.rodar_pagina()

def historinha5(nada):
    pagina = Pagina((0,0,0))
    botao_historinha = Botao_imagem("historinha5.jpeg",20,20,760,560,10,pagina,executar_menu_principal)
    pagina.lista_objetos = [botao_historinha]
    pagina.rodar_pagina()

def historinha6(nada):
    pagina = Pagina((0,0,0))
    botao_historinha = Botao_imagem("historinha6.jpeg",20,20,760,560,10,pagina,historinha7)
    pagina.lista_objetos = [botao_historinha]
    pagina.rodar_pagina()

def historinha7(nada):
    pagina = Pagina((0,0,0))
    botao_historinha = Botao_imagem("historinha7.jpeg",20,20,760,560,10,pagina,historinha8)
    pagina.lista_objetos = [botao_historinha]
    pagina.rodar_pagina()

def historinha8(nada):
    pagina = Pagina((0,0,0))
    botao_historinha = Botao_imagem("historinha8.jpeg",20,20,760,560,10,pagina,executar_menu_principal)
    pagina.lista_objetos = [botao_historinha]
    pagina.rodar_pagina()

#FUNCOES PASSADAS PARA OS BOTOES

def voltar(nada=None):
    global jogo
    pygame.mouse.set_visible(False)
    jogo.avancar_fase()

def comprar_incremento_vida(menu):
    if variaveis.dinheiro - variaveis.preco_incremento_vida >= 0:
        variaveis.vida_jogador += variaveis.valor_evolucao_vida
        variaveis.dinheiro -= variaveis.preco_incremento_vida
        variaveis.valor_evolucao_vida += 150
        variaveis.preco_incremento_vida *= 2
        executar_loja_pg2(menu)

def comprar_incremento_municao(menu):
    if variaveis.dinheiro - variaveis.preco_incremento_municao >= 0:
        variaveis.municao_inicio_fase += variaveis.incremento_municao
        variaveis.dinheiro -= variaveis.preco_incremento_municao

        variaveis.incremento_municao += int(variaveis.incremento_municao*0.50)
        variaveis.preco_incremento_municao *= 2
        executar_loja_pg2(menu)    

def comprar_skin_personagem(skin_e_menu): 
    if variaveis.dinheiro - skin_e_menu[0].preco >= 0 and skin_e_menu[0].status_compra == False:
        skin_e_menu[0].status_compra = True        
        variaveis.dinheiro -= skin_e_menu[0].preco
        skin_e_menu[0].texto = "comprado"
    
    if skin_e_menu[0].status_compra == True:
        jogo.jogador.endereco_imagem = skin_e_menu[0].endereco_imagem
        skin_e_menu[0].texto = "Selecionado"
        for objeto in variaveis.lista_skin:
            if objeto != skin_e_menu[0] and objeto.status_compra==True:
                objeto.texto = "Comprado"

    if variaveis.lista_skin.index(skin_e_menu[0]) >= 7:
        executar_loja_pg5(skin_e_menu[1])

    elif variaveis.lista_skin.index(skin_e_menu[0]) == 0:
        executar_loja_pg2(skin_e_menu[1])

    elif variaveis.lista_skin.index(skin_e_menu[0]) >= 1 and variaveis.lista_skin.index(skin_e_menu[0]) <= 3:
        executar_loja_pg3(skin_e_menu[1])

    else:
        executar_loja_pg4(skin_e_menu[1])

def comprar_arma(arma_e_menu):

    if variaveis.dinheiro - arma_e_menu[0].preco >= 0 and arma_e_menu[0].status_compra == False: 
        arma_e_menu[0].status_compra = True
        variaveis.dinheiro -= arma_e_menu[0].preco
        arma_e_menu[0].texto = "comprado"

    if arma_e_menu[0].status_compra == True:
        selecionar(arma_e_menu[0])

    if variaveis.lista_armas.index(arma_e_menu[0]) < 3:
        executar_loja_pg1(arma_e_menu[1])
    else:
        executar_loja_pg0(arma_e_menu[1])
    

def selecionar(arma):
    jogador.inventario.arma_adicional = arma
    arma.texto = "Selecionado"

    for objeto in variaveis.lista_armas:
        if objeto != arma and objeto.status_compra == True:
            objeto.texto = "comprado"

    
def printar1(nada=None):
    pass

def sair(null=None):
    quit()
    exit()


#=================JOGO==========================

class Objeto():

    def __init__(self, pos_x,pos_y, altura, largura, endereco_imagem,status):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.altura = altura
        self.largura = largura
        self.endereco_imagem = endereco_imagem
        self.status = status
        self.imagem = None
        self.imagem_rotacionada = None

    def iniciar_imagem(self):
    	self.imagem = pygame.image.load(self.endereco_imagem)
    	self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))

    def mostrar_imagem(self,surface):
            surface.tela.blit(self.imagem_rotacionada, ((self.pos_x-self.largura//2 + surface.dx), (self.pos_y-self.altura//2 + surface.dy)))

    def mudar_status(self):
    	if self.status == True:
    		self.status = False
    	
    	else:
    		self.status = True

    def calcular_angulo(self, x,y, tela):

        x += tela.pos_x
        y += tela.pos_y
        rx = x- self.pos_x
        ry = y- self.pos_y
        rad = mat.atan2(rx,ry)
        angulo = rad/(mat.pi/180)
        if angulo < 0:
            angulo += 360
        return angulo

    def rotacionar(self, x,y,tela):
        

        angulo_imagem = self.calcular_angulo(x,y,tela)
        orig_rect = self.imagem.get_rect()
        imagem_rotacionada = pygame.transform.rotate(self.imagem, angulo_imagem-90)
        rot_rect = orig_rect.copy()
        rot_rect.center = imagem_rotacionada.get_rect().center
        imagem_rotacionada = imagem_rotacionada.subsurface(rot_rect).copy()
        
        self.imagem_rotacionada = imagem_rotacionada


    def verificar_colisao(self, lista_objetos_colisao, direcao=None):

        soma_x = 0
        soma_y = 0
        
        total_colisoes = []
        
        if direcao is not None:
            if direcao[0] == "-":
                if direcao[1] == "x":
                    soma_x = (self.velocidade * -1) - self.largura//2
                else:
                    soma_y = (self.velocidade * -1) - self.altura//2
            
            if direcao[0] == "+":
                if direcao[1] == "x":
                    soma_x = self.velocidade + self.largura//2
                else:
                    soma_y = self.velocidade + self.altura//2

            
            for objeto in lista_objetos_colisao:
                if (self.pos_x + soma_x >= objeto.pos_x - objeto.largura//2) and (self.pos_x + soma_x  <= objeto.pos_x + objeto.largura//2) and (self.pos_y + soma_y >= objeto.pos_y - objeto.altura//2) and (self.pos_y + soma_y  <= objeto.pos_y + objeto.altura//2):
                    total_colisoes.append(0)
            
        else:
            for objeto in lista_objetos_colisao:
                if (self.pos_x + self.largura//2 >= objeto.pos_x - objeto.largura//2) and (self.pos_x - self.largura//2  <= objeto.pos_x + objeto.largura//2) and (self.pos_y + self.altura//2 >= objeto.pos_y - objeto.altura//2) and (self.pos_y - self.altura//2  <= objeto.pos_y + objeto.altura//2):
                    total_colisoes.append(0)            


        if len(total_colisoes) == 0:
            return False
        else:
            return True	

class Skin(Objeto):

    def __init__(self,endereco_imagem,preco,status_compra):
        self.endereco_imagem = endereco_imagem
        self.preco = preco
        self.status_compra = status_compra
        self.texto = self.preco


class Consumivel(Objeto):

    def __init__(self,pos_x,pos_y,altura,largura,endereco_imagem,status,valor_recuperacao,tipo):
        super().__init__(pos_x,pos_y,altura,largura,endereco_imagem,status)
        self.valor_recuperacao = valor_recuperacao
        self.tipo = tipo

    def recuperar_valor(self, jogador, valor_maximo):
        if self.tipo == "munição":
            if jogador.inventario.arma_uso.raridade == "comum":
                jogador.inventario.arma_uso.municao += int(self.valor_recuperacao)
            
            elif jogador.inventario.arma_uso.raridade == "rara":
                jogador.inventario.arma_uso.municao += int(self.valor_recuperacao*0.75)

            elif jogador.inventario.arma_uso.raridade == "epica":
                jogador.inventario.arma_uso.municao += int(self.valor_recuperacao*0.50)
            
            elif jogador.inventario.arma_uso.raridade == "lendaria":
                jogador.inventario.arma_uso.municao += int(self.valor_recuperacao*0.25)
        
        elif self.tipo == "kit_medico":
            if jogador.vida + self.valor_recuperacao <= valor_maximo:
                jogador.vida += self.valor_recuperacao
            
            else:
                jogador.vida = valor_maximo
                
        self.status = False

class Jogador(Objeto):

    def __init__(self,pos_x,pos_y,altura,largura,endereco_imagem,velocidade,status,inventario,vida):
        Objeto.__init__(self,pos_x,pos_y,altura,largura,endereco_imagem,status)
        self.velocidade = velocidade
        self.inventario = inventario
        self.vida = vida 

    def verificar_status(self):
        if self.vida <= 0:
            self.status = False


    def locomover(self,keys,tela,fase):
        if keys[pygame.K_d] and keys[pygame.K_s]:
            
            if tela.pos_y + tela.altura + tela.velocidade < fase.mapa.altura and self.pos_y > tela.altura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("+", "y")) == False:
                tela.pos_y += tela.velocidade

            if self.pos_y + self.altura//2 + self.velocidade < fase.mapa.altura  and self.verificar_colisao(fase.lista_objetos_colisao,("+", "y")) == False:
                self.pos_y += self.velocidade
            
            if tela.pos_x + tela.largura + tela.velocidade < fase.mapa.largura and self.pos_x > tela.largura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("+", "x")) == False:
                tela.pos_x += tela.velocidade 

            if self.pos_x + self.largura//2 + self.velocidade < fase.mapa.largura and self.verificar_colisao(fase.lista_objetos_colisao,("+", "x")) == False:
                self.pos_x += self.velocidade


        elif keys[pygame.K_d] and keys[pygame.K_w]:
            
            if tela.pos_y - tela.velocidade > 0 and self.pos_y - self.velocidade < fase.mapa.altura - tela.altura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "y")) == False:
                tela.pos_y -= tela.velocidade
            if self.pos_y - self.altura//2 - self.velocidade >= 0 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "y")) == False:
                self.pos_y -= self.velocidade
            if tela.pos_x + tela.largura + tela.velocidade < fase.mapa.largura and self.pos_x + self.velocidade > tela.largura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("+", "x"))== False:
                tela.pos_x += tela.velocidade
            if self.pos_x + self.largura//2 + self.velocidade < fase.mapa.largura and self.verificar_colisao(fase.lista_objetos_colisao,("+", "x"))== False:
                self.pos_x += self.velocidade

        elif keys[pygame.K_a] and keys[pygame.K_s]:
            
            if tela.pos_y + tela.altura + tela.velocidade < fase.mapa.altura and self.pos_y > tela.altura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("+", "y"))== False:
                tela.pos_y += tela.velocidade
            if self.pos_y + self.altura//2 + self.velocidade < fase.mapa.altura and self.verificar_colisao(fase.lista_objetos_colisao,("+", "y"))== False:
                self.pos_y += self.velocidade
            if tela.pos_x - tela.velocidade > 0 and self.pos_x - self.velocidade < fase.mapa.largura - tela.largura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "x")) == False:
                tela.pos_x -= tela.velocidade
            if self.pos_x - self.largura//2 - self.velocidade >= 0 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "x")) == False:
                self.pos_x -= self.velocidade

        elif keys[pygame.K_a] and keys[pygame.K_w]:
            
            if tela.pos_y - tela.velocidade > 0 and self.pos_y - self.velocidade < fase.mapa.altura - tela.altura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "y")) == False:
                tela.pos_y -= tela.velocidade
            if self.pos_y - self.altura//2 - self.velocidade >= 0 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "y")) == False:
                self.pos_y -= self.velocidade
            if tela.pos_x - tela.velocidade > 0 and self.pos_x - self.velocidade < fase.mapa.largura - tela.largura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "x")) == False:
                tela.pos_x -= tela.velocidade
            if self.pos_x - self.largura//2 - self.velocidade >= 0 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "x")) == False:
                self.pos_x -= self.velocidade

        elif keys[pygame.K_a]:
            
            if tela.pos_x - tela.velocidade > 0 and self.pos_x - self.velocidade < fase.mapa.largura - tela.largura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "x")) == False:
                tela.pos_x -= tela.velocidade
            if self.pos_x - self.largura//2 - self.velocidade >= 0 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "x")) == False:
                self.pos_x -= self.velocidade

        elif keys[pygame.K_d]:
            
            if tela.pos_x + tela.largura + tela.velocidade < fase.mapa.largura and self.pos_x + self.velocidade > tela.largura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("+", "x"))== False:
                tela.pos_x += tela.velocidade
            if self.pos_x + self.largura//2 + self.velocidade < fase.mapa.largura and self.verificar_colisao(fase.lista_objetos_colisao,("+", "x"))== False:
                self.pos_x += self.velocidade

        elif keys[pygame.K_w]:
            
            if tela.pos_y - tela.velocidade > 0 and self.pos_y - self.velocidade < fase.mapa.altura - tela.altura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "y")) == False:
                tela.pos_y -= tela.velocidade
            if self.pos_y - self.altura//2 - self.velocidade >= 0 and self.verificar_colisao(fase.lista_objetos_colisao,("-", "y")) == False:
                self.pos_y -= self.velocidade

        elif keys[pygame.K_s]:
            
            if tela.pos_y + tela.altura + tela.velocidade < fase.mapa.altura and self.pos_y > tela.altura//2 and self.verificar_colisao(fase.lista_objetos_colisao,("+", "y"))== False:
                tela.pos_y += tela.velocidade
            if self.pos_y + self.altura//2 + self.velocidade < fase.mapa.altura and self.verificar_colisao(fase.lista_objetos_colisao,("+", "y"))== False:
                self.pos_y += self.velocidade

class Inimigo(Objeto):

    def __init__(self,pos_x,pos_y,altura,largura,endereco_imagem,velocidade,status,dano,vida,quadrante,recompensa):
        super().__init__(pos_x,pos_y,altura,largura,endereco_imagem,status)
        self.velocidade = velocidade
        self.dano = dano
        self.vida = vida
        self.quadrante = quadrante
        self.recompensa = recompensa

    def verificar_status(self):
        if self.vida <= 0:
            self.status = False

    def perseguir_objeto(self, objeto, lista_objeto):

        lista_objetos = lista_objeto.copy()
        lista_objetos.append(objeto)

        if (self.pos_x,self.pos_y) != (objeto.pos_x, objeto.pos_y):

            if self.pos_y < objeto.pos_y and self.verificar_colisao(lista_objetos,("+","y")) == False:
                self.pos_y += self.velocidade
            if self.pos_y < objeto.pos_y and self.verificar_colisao([objeto],("+","y")) == True:
                self.dar_dano(objeto)
                

            if self.pos_y  > objeto.pos_y and self.verificar_colisao(lista_objetos,("-","y"))  == False:
                self.pos_y -= self.velocidade
            if self.pos_y  > objeto.pos_y and self.verificar_colisao([objeto],("-","y"))  == True:
                self.dar_dano(objeto)
        

            if self.pos_x < objeto.pos_x and self.verificar_colisao(lista_objetos,("+","x")) == False:
                self.pos_x += self.velocidade
            if self.pos_x < objeto.pos_x and self.verificar_colisao([objeto],("+","x")) == True:
                self.dar_dano(objeto)
                

            if self.pos_x > objeto.pos_x and self.verificar_colisao(lista_objetos,("-","x")) == False:
                self.pos_x -= self.velocidade
            if self.pos_x > objeto.pos_x and self.verificar_colisao([objeto],("-","x")) == True:
                self.dar_dano(objeto)
		
    def dar_dano(self,alvo):
        alvo.vida -= self.dano


class Arma(Objeto):

    def __init__(self,pos_x,pos_y,altura,largura,endereco_imagem,status,dano,municao_pente,capacidade_municao_total,molde_tiro,raridade,municao,imagem_lateral,preco,status_compra):
        super().__init__(pos_x,pos_y,altura,largura,endereco_imagem,status)
        self.dano = dano
        self.municao = municao
        self.capacidade_municao_total = capacidade_municao_total
        self.municao_pente = municao_pente
        self.molde_tiro = molde_tiro
        self.raridade = raridade
        self.preco = preco
        self.texto = self.preco
        self.imagem_lateral = imagem_lateral

        self.status_compra = status_compra
        self.lista_tiros = []

    def ajustar_posicao(self,jogador):
        self.pos_x = jogador.pos_x
        self.pos_y = jogador.pos_y

    def recarregar(self,jogador):
      	if self.municao_pente < self.capacidade_municao_total:
            for cont in range(self.municao_pente, self.capacidade_municao_total):
                if (self.municao - 1) >= 0:
                  self.municao_pente += 1
                  self.municao -= 1

    def atirar(self,angulo_tiro,jogador,x,y,tela):
        
        if self.municao_pente > 0:
            tiro = Tiro(self.pos_x,self.pos_y-jogador.altura+self.altura//2,self.molde_tiro.altura,self.molde_tiro.largura,self.molde_tiro.endereco_imagem,True,self.molde_tiro.velocidade,angulo_tiro,self.molde_tiro.desl_max)
            tiro.definir_desl_tiro()
            tiro.iniciar_imagem()
            tiro.rotacionar(x,y,tela)
            self.lista_tiros.append(tiro)
            self.municao_pente -= 1

    def atualizar_tiros(self,fase):

        for tiro in self.lista_tiros:
            tiro.somar_desl_tiro()
            if tiro.desl == tiro.desl_max:
                tiro.status = False
            else:
                for inimigo in fase.lista_inimigos:
                    if tiro.verificar_colisao([inimigo]) == True:
                        inimigo.vida -= self.dano
                        tiro.status = False
                try:
                    for objeto in fase.lista_objetos:
                        if tiro.verificar_colisao([objeto]):
                            tiro.status = False
                except:
                    pass
            if tiro.status == False:
                self.lista_tiros.remove(tiro)



class Tiro(Objeto):

    def __init__(self,pos_x,pos_y,altura,largura,endereco_imagem,status,velocidade,angulo_tiro,desl_max):
        super().__init__(pos_x,pos_y,altura,largura,endereco_imagem,status)
        self.angulo_tiro = angulo_tiro
        self.desl_tiro_y = 0
        self.desl_tiro_x = 0
        self.velocidade = velocidade
        self.desl_max = desl_max
        self.desl = 0

    def definir_desl_tiro(self):
        self.desl_tiro_x = mat.sin(mat.radians(self.angulo_tiro))*self.velocidade
        self.desl_tiro_y = mat.cos(mat.radians(self.angulo_tiro))*self.velocidade

    def somar_desl_tiro(self):
        self.pos_x += self.desl_tiro_x
        self.pos_y+= self.desl_tiro_y
        self.desl += 1

class Inventario():

    def __init__(self, arma_base, arma_adicional, dinheiro):
        self.arma_base = arma_base
        self.arma_adicional = arma_adicional
        self.dinheiro = dinheiro
        self.arma_uso = self.arma_base

    def trocar_arma(self):
        if self.arma_uso == self.arma_base:
            self.arma_uso = self.arma_adicional

        else:
            self.arma_uso = self.arma_base


class Mapa():
    def __init__(self,endereco_imagem,largura,altura):
        self.endereco_imagem = endereco_imagem
        self.largura = largura
        self.altura = altura
        self.fundo = None

    def criar_fundo(self):
        self.fundo = pygame.image.load(self.endereco_imagem)
        self.fundo = pygame.transform.scale(self.fundo,(self.largura,self.altura))

    def mostrar_fundo(self, surface):
    	if surface.tela is not None:
            surface.tela.blit(self.fundo, (surface.dx, surface.dy))

class Fase():

    def __init__(self,mapa,jogador,numero_fase):
        self.mapa = mapa
        
        
        self.lista_objetos_colisao = [] 
        self.lista_consumiveis = []
        self.lista_inimigos = []
        self.lista_objetos = []
        self.lista_decoracoes = []

        self.numero_fase = numero_fase 


    def criar_inimigos(self):

        cont = 0
        
        while cont < int(variaveis.quant_inimigos*0.25):

            tamanho = variaveis.tamanho_inimigos
            pos_x = randint(0+tamanho[0]+50, self.mapa.largura//2)
            pos_y = randint(0+tamanho[1]+50, self.mapa.altura//2)

            endereco_imagem = variaveis.imagem_inimigo
            dano = variaveis.dano_inimigo
            velocidade = variaveis.velocidade_inimigo
            vida = variaveis.vida_inimigo
            recompensa = variaveis.recompensa_inimigos

            inimigo = Inimigo(pos_x,pos_y,tamanho[0],tamanho[1],endereco_imagem,True,velocidade,dano,vida, 1,recompensa)
            if inimigo.verificar_colisao(self.lista_objetos_colisao) == False:
                cont += 1
                self.lista_objetos_colisao.append(inimigo)
                self.lista_inimigos.append(inimigo)
        cont = 0
        while cont < int(variaveis.quant_inimigos*0.25):    
            tamanho = variaveis.tamanho_inimigos
            pos_x = randint(self.mapa.largura//2, self.mapa.largura-tamanho[0]-50)
            pos_y = randint(self.mapa.altura//2, self.mapa.altura-tamanho[1]-50)   

            endereco_imagem = variaveis.imagem_inimigo
            dano = variaveis.dano_inimigo
            velocidade = variaveis.velocidade_inimigo
            vida = variaveis.vida_inimigo
            recompensa = variaveis.recompensa_inimigos

            inimigo = Inimigo(pos_x,pos_y,tamanho[0],tamanho[1],endereco_imagem,True,velocidade,dano,vida, 4,recompensa)
            if inimigo.verificar_colisao(self.lista_objetos_colisao) == False:
                cont += 1
                self.lista_objetos_colisao.append(inimigo)
                self.lista_inimigos.append(inimigo)

        cont = 0
        while cont < int(variaveis.quant_inimigos*0.25):     
            tamanho = variaveis.tamanho_inimigos
            pos_x = randint(0+tamanho[0]+50, self.mapa.largura//2)
            pos_y = randint(self.mapa.altura//2, self.mapa.altura-tamanho[1]-50)

            endereco_imagem = variaveis.imagem_inimigo
            dano = variaveis.dano_inimigo
            velocidade = variaveis.velocidade_inimigo
            vida = variaveis.vida_inimigo
            recompensa = variaveis.recompensa_inimigos

            inimigo = Inimigo(pos_x,pos_y,tamanho[0],tamanho[1],endereco_imagem,True,velocidade,dano,vida, 3,recompensa)
            if inimigo.verificar_colisao(self.lista_objetos_colisao) == False:
                cont += 1
                self.lista_objetos_colisao.append(inimigo)
                self.lista_inimigos.append(inimigo)

        cont = 0
        while cont < int(variaveis.quant_inimigos*0.25):

            tamanho = variaveis.tamanho_inimigos
            pos_x = randint(self.mapa.largura//2, self.mapa.largura-tamanho[0]-50)
            pos_y = randint(0+tamanho[1]+50, self.mapa.altura//2)
        
            endereco_imagem = variaveis.imagem_inimigo
            dano = variaveis.dano_inimigo
            velocidade = variaveis.velocidade_inimigo
            vida = variaveis.vida_inimigo
            recompensa = variaveis.recompensa_inimigos

            inimigo = Inimigo(pos_x,pos_y,tamanho[0],tamanho[1],endereco_imagem,True,velocidade,dano,vida, 2,recompensa)
            
            if inimigo.verificar_colisao(self.lista_objetos_colisao) == False:
                cont +=1
                self.lista_objetos_colisao.append(inimigo)
                self.lista_inimigos.append(inimigo)


        if self.numero_fase%2 ==0:
            if self.numero_fase%10 != 0:
                cont = 0
                while cont == 0:
                    tamanho = variaveis.mini_boss_tamanho
                    pos_x = randint(self.mapa.largura//2, self.mapa.largura-tamanho[0]-50)
                    pos_y = randint(0+tamanho[1]+50, self.mapa.altura//2)
                
                    endereco_imagem = variaveis.mini_boss_imagem
                    dano = variaveis.mini_boss_dano
                    velocidade = variaveis.mini_boss_velocidade
                    vida = variaveis.mini_boss_vida
                    recompensa = variaveis.mini_boss_recompensa

                    inimigo = Inimigo(pos_x,pos_y,tamanho[0],tamanho[1],endereco_imagem,True,velocidade,dano,vida, 2,recompensa)
                    
                    if inimigo.verificar_colisao(self.lista_objetos_colisao) == False:
                        cont +=1
                        self.lista_objetos_colisao.append(inimigo)
                        self.lista_inimigos.append(inimigo)
            
            else:
                cont = 0
                while cont == 0:
                    tamanho = variaveis.boss_tamanho
                    pos_x = randint(self.mapa.largura//2, self.mapa.largura-tamanho[0]-50)
                    pos_y = randint(0+tamanho[1]+50, self.mapa.altura//2)
                
                    endereco_imagem = variaveis.boss_imagem
                    dano = variaveis.boss_dano
                    velocidade = variaveis.boss_velocidade
                    vida = variaveis.boss_vida
                    recompensa = variaveis.boss_recompensa

                    inimigo = Inimigo(pos_x,pos_y,tamanho[0],tamanho[1],endereco_imagem,True,velocidade,dano,vida, 2,recompensa)

                    if inimigo.verificar_colisao(self.lista_objetos_colisao) == False:
                        cont +=1
                        self.lista_objetos_colisao.append(inimigo)
                        self.lista_inimigos.append(inimigo)
                        


    def criar_consumiveis(self):

        cont = 0
        while cont < int(variaveis.quantidade_consumiveis*0.75):

            tamanho = variaveis.tamanho_kit
            pos_x = randint(tamanho[0]+50, self.mapa.largura)
            pos_y = randint(tamanho[1]+50, self.mapa.altura)
        
            endereco_imagem = variaveis.imagem_kit

            modificadores = variaveis.modificadores
            valor_recuperacao = variaveis.recuperacao_kit * int(modificadores[randint(0,len(modificadores)-1)])

            consumivel = Consumivel(pos_x,pos_y,tamanho[0],tamanho[1],endereco_imagem,True,valor_recuperacao,"kit_medico")
            
            lista_colisao =  self.lista_inimigos + self.lista_objetos + self.lista_consumiveis
            
            if consumivel.verificar_colisao(lista_colisao) == False:
                self.lista_consumiveis.append(consumivel)
                cont +=1

        cont = 0
        while cont < int(variaveis.quantidade_consumiveis*0.25):

            tamanho = variaveis.tamanho_kit
            pos_x = randint(tamanho[0]+50, self.mapa.largura)
            pos_y = randint(tamanho[1]+50, self.mapa.altura)
        
            endereco_imagem = variaveis.imagem_municao

            
            valor_recuperacao = variaveis.recuperacao_municao

            consumivel = Consumivel(pos_x,pos_y,tamanho[0],tamanho[1],endereco_imagem,True,valor_recuperacao,"munição")
            
            lista_colisao =  self.lista_inimigos + self.lista_objetos + self.lista_consumiveis
            if consumivel.verificar_colisao(lista_colisao) == False:
                cont += 1
                self.lista_consumiveis.append(consumivel)

    def criar_decoracoes(self):
        cont = 0
        while cont < variaveis.quantidade_objetos_decorativos:

            tamanho = variaveis.tamanho_decoracao
            pos_x = randint(tamanho[0]+50, self.mapa.largura)
            pos_y = randint(tamanho[1]+50, self.mapa.altura)
        
            if self.numero_fase < 10:
                endereco_imagem = variaveis.decoracao_floresta
            else:
                endereco_imagem = variaveis.decoracao_cidade

            decoracao = Objeto(pos_x,pos_y,tamanho[0],tamanho[1],endereco_imagem,True)
            
            lista_colisao =  self.lista_inimigos + self.lista_objetos + self.lista_consumiveis
            if decoracao.verificar_colisao(lista_colisao) == False:
                cont += 1
                self.lista_decoracoes.append(decoracao)


    def criar_objetos(self):
        self.lista_objetos_colisao = []
        if self.numero_fase <= 10:
            self.lista_objetos = variaveis.lista_objetos_floresta
        else:
            self.lista_objetos = variaveis.lista_objetos_cidade
        
        self.lista_objetos_colisao = self.lista_objetos_colisao + self.lista_objetos

class Mira():
    def __init__(self,largura,altura,endereco_imagem):
        self.largura = largura
        self.altura = altura
        self.endereco_imagem = endereco_imagem
        self.mira = None
    
    def criar_mira(self):
        self.mira = pygame.image.load(self.endereco_imagem)
        self.mira = pygame.transform.scale(self.mira,(self.largura,self.altura))
        
    def mostrar_imagem(self,surface,pos_x,pos_y):
        surface.tela.blit(self.mira, (pos_x,pos_y))

class Tela():

    def __init__(self, largura, altura, pos_x,pos_y,velocidade,mira):
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.dx = 0
        self.dy = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tela = None
        self.mira = mira
        self.fonte = None

    
    def iniciar_fonte(self,fonte,tamanho_fonte):
        self.fonte = pygame.font.Font(fonte, tamanho_fonte)

    def atualizar_dx_dy(self):
        self.dx = self.pos_x * -1
        self.dy = self.pos_y * -1

    def criar_tela(self):
        self.tela = pygame.display.set_mode((self.largura,self.altura))


    def atualizar_tela(self):
        if self.tela is not None:
            pygame.display.update()

class Jogo():
    def __init__(self, tela,fase,jogador):
        self.tela = tela
        self.executar = False
        self.situacao_final = None
        self.jogador = jogador
        self.fase = fase
        self.progresso = None
        self.quadrante_atual = 1

    def capturar_evento(self):
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sair()

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_e:
                    for objeto in self.fase.lista_consumiveis:
                        if self.jogador.verificar_colisao([objeto]) == True:
                            objeto.status = False
                            objeto.recuperar_valor(self.jogador,variaveis.vida_jogador)

                if event.key == pygame.K_q:
                    self.jogador.inventario.trocar_arma()
                
                if event.key == pygame.K_k:
                    self.executar = False
                    self.jogador.status = False
                    self.fim_do_jogo()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    self.jogador.inventario.arma_uso.recarregar(self.jogador)
                    

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                self.jogador.locomover(keys,self.tela,self.fase)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==  1:
                    self.jogador.inventario.arma_uso.atirar(self.jogador.calcular_angulo(x,y,self.tela),self.jogador,x,y,self.tela)
        
        
        self.tela.atualizar_dx_dy()
        self.jogador.rotacionar(x,y,self.tela)        
        self.atualizar_quadrante()



    def configurar_inicio_loop(self):

        pygame.key.set_repeat(10,10)
        
        self.tela.criar_tela()
        self.tela.iniciar_fonte(variaveis.lista_fontes[0],variaveis.tamanho_fonte)
        self.fase.mapa.criar_fundo()
        self.tela.mira.criar_mira()


        self.fase.criar_objetos()
        self.fase.criar_consumiveis()
        self.fase.criar_inimigos()
        self.fase.criar_decoracoes()

        self.jogador.inventario.arma_uso.iniciar_imagem()
        self.jogador.inventario.arma_base.iniciar_imagem()
        self.jogador.inventario.arma_adicional.iniciar_imagem()
        

        for objeto in self.fase.lista_objetos_colisao:
            objeto.iniciar_imagem()

        for objeto in self.fase.lista_consumiveis:
            objeto.iniciar_imagem()

        for objeto in self.fase.lista_decoracoes:
            objeto.iniciar_imagem()

        self.jogador.iniciar_imagem()

        self.jogador.inventario.arma_uso.iniciar_imagem()

        pygame.mouse.set_visible(False)        

    def remover_objetos(self):

        for objeto in self.fase.lista_consumiveis:
            if objeto.status == False:
                self.fase.lista_consumiveis.remove(objeto)

        for objeto in self.fase.lista_inimigos:
            objeto.verificar_status()
            if objeto.status == False:
                self.jogador.inventario.dinheiro += objeto.recompensa
                self.fase.lista_inimigos.remove(objeto)
                self.fase.lista_objetos_colisao.remove(objeto) 

    def atualizar_quadrante(self):
        if self.jogador.pos_x < self.fase.mapa.largura//2 and self.jogador.pos_y < self.fase.mapa.altura//2:
            self.quadrante_atual = 1

        if self.jogador.pos_x > self.fase.mapa.largura//2 and self.jogador.pos_y > self.fase.mapa.altura//2:
            self.quadrante_atual = 4
    
        if self.jogador.pos_x < self.fase.mapa.largura//2 and self.jogador.pos_y > self.fase.mapa.altura//2:
            self.quadrante_atual = 3

        if self.jogador.pos_x > self.fase.mapa.largura//2 and self.jogador.pos_y < self.fase.mapa.altura//2:
            self.quadrante_atual = 2

    def mostrar_imagens(self):
            
        self.fase.mapa.mostrar_fundo(self.tela)
        
        for objeto in self.fase.lista_decoracoes:
            objeto.imagem_rotacionada = objeto.imagem
            objeto.mostrar_imagem(self.tela)

        for objeto in self.fase.lista_consumiveis:
            objeto.imagem_rotacionada = objeto.imagem
            objeto.mostrar_imagem(self.tela)

        for objeto in self.fase.lista_objetos:
            objeto.imagem_rotacionada = objeto.imagem
            objeto.mostrar_imagem(self.tela)

        for inimigo in self.fase.lista_inimigos:
            if inimigo.quadrante == self.quadrante_atual:
                inimigo.perseguir_objeto(self.jogador, self.fase.lista_objetos_colisao)
                inimigo.rotacionar(self.jogador.pos_x+self.tela.dx,self.jogador.pos_y+self.tela.dy,self.tela)
            else:
                inimigo.imagem_rotacionada = inimigo.imagem
            inimigo.mostrar_imagem(self.tela)

        self.jogador.mostrar_imagem(self.tela)

        x,y = pygame.mouse.get_pos()

        self.jogador.inventario.arma_base.ajustar_posicao(self.jogador)
        self.jogador.inventario.arma_adicional.ajustar_posicao(self.jogador)
        self.jogador.inventario.arma_base.rotacionar(x,y,self.tela)
        self.jogador.inventario.arma_adicional.rotacionar(x,y,self.tela)
        
        self.jogador.inventario.arma_base.atualizar_tiros(self.fase)    
        self.jogador.inventario.arma_adicional.atualizar_tiros(self.fase)

        self.jogador.inventario.arma_uso.mostrar_imagem(self.tela)

        for tiro in self.jogador.inventario.arma_base.lista_tiros:
            tiro.mostrar_imagem(self.tela)
        for tiro in self.jogador.inventario.arma_adicional.lista_tiros:
            tiro.mostrar_imagem(self.tela)
            

        self.tela.mira.mostrar_imagem(self.tela,x,y)

    def verificar_progresso(self):
        
        self.jogador.verificar_status()
        if self.jogador.status == False:
            self.executar = False
            self.progresso = False
        
        if len(self.fase.lista_inimigos) == 0:
            self.executar = False
            self.progresso = True
    
    def carregar_informacoes(self):
        index = str(float(self.jogador.vida)).index(".")        
        vida = str(self.jogador.vida)[0:index]
        vida_txt = self.tela.fonte.render(vida,True,(255,255,255))
        quant_inimigos_txt = self.tela.fonte.render(str(len(self.fase.lista_inimigos)), True, (0,0,255))
        municao_txt = self.tela.fonte.render(str(self.jogador.inventario.arma_uso.municao_pente)+"I"+str(self.jogador.inventario.arma_uso.municao),True,(255,140,0))
        fase_atual_txt = self.tela.fonte.render("Fase " +str(self.fase.numero_fase),True,(0,0,255))

        self.tela.tela.blit(vida_txt, (10,10))
        self.tela.tela.blit(quant_inimigos_txt, (760,60))
        self.tela.tela.blit(municao_txt, (650,560))
        self.tela.tela.blit(fase_atual_txt, (680,10))

    def avancar_fase(self):
        variaveis.dinheiro += self.jogador.inventario.dinheiro
        self.jogador.inventario.dinheiro = 0
        self.fase.lista_objetos = []
        self.fase.lista_objetos_colsiao = []
        self.jogador.pos_x = variaveis.pos_x_jogador
        self.jogador.pos_y = variaveis.pos_y_jogador
        self.tela.pox_x = 0
        self.tela.pos_y = 0

        self.jogador.vida = variaveis.vida_jogador
        if self.fase.numero_fase == 1:
            variaveis.quant_inimigos += variaveis.quant_inimigos_base
        
        municao_recuperacao = Consumivel(0,0,0,0,None,True,variaveis.municao_inicio_fase,"munição")
        self.jogador.inventario.arma_uso = self.jogador.inventario.arma_adicional
        municao_recuperacao.recuperar_valor(self.jogador,None)
        self.jogador.inventario.arma_uso = self.jogador.inventario.arma_base
        municao_recuperacao.recuperar_valor(self.jogador,None)


        self.fase.numero_fase += 1
        if self.fase.numero_fase == 10:
            variaveis.quant_inimigos += variaveis.quant_inimigos_base
        if self.fase.numero_fase == 15:
            variaveis.quant_inimigos += variaveis.quant_inimigos_base
        if self.fase.numero_fase == 20:
            variaveis.quant_inimigos = 100

        if self.fase.numero_fase%5:
            variaveis.quantidade_consumiveis -= 2
        
        if self.fase.numero_fase%2 == 0 and self.fase.numero_fase > 2:
            if self.fase.numero_fase%10 == 0 and self.fase.numero_fase > 10:
                variaveis.boss_vida += 10000
                variaveis.boss_dano += 100
                variaveis.boss_recompensa += 10000
            
            else:
                variaveis.mini_boss_vida += 200
                variaveis.mini_boss_dano += 5
                variaveis.mini_boss_recompensa += 500

        variaveis.dano_inimigo += variaveis.dano_inimigo_base/10
        variaveis.vida_inimigo += variaveis.vida_inimigo_base/10

        if self.fase.numero_fase == 11:
            self.fase.mapa = Mapa(variaveis.imagem_mapa_cidade, variaveis.tamanho_mapa[0] , variaveis.tamanho_mapa[1])
            self.tela.pos_x = variaveis.tela_pos_x
            self.tela.pos_y = variaveis.tela_pos_y
            variaveis.recuperacao_kit += int(variaveis.recuperacao_kit*0.25)
            variaveis.recuperacao_municao += int(variaveis.recuperacao_municao*0.25)
            variaveis.velocidade_inimigo += variaveis.velocidade_inimigo_base/2
        self.loop()

    def loop(self,null=None):
        self.configurar_inicio_loop()
        self.executar = True
        while self.executar:
            
            self.verificar_progresso()
            self.capturar_evento()
            self.jogador.inventario.arma_uso.atualizar_tiros(self.fase)
            self.mostrar_imagens()
            self.remover_objetos()
            self.carregar_informacoes()
            self.tela.atualizar_tela()


        if self.fase.numero_fase == 20 and self.jogador.vida > 0:  
            self.situacao_final = "ganhou"
            self.fim_do_jogo()
        
        elif self.progresso == True:
            pygame.mouse.set_visible(True)
            executar_loja_pg0(False)
        
        if self.jogador.status == False:
            self.fim_do_jogo()
        

    def resetar_valores(self):

        variaveis.vida_inimigo = variaveis.vida_inimigo_base
        variaveis.dano_inimigo = variaveis.dano_inimigo_base
        variaveis.velocidade_inimigo = variaveis.velocidade_inimigo_base
        variaveis.recompensa_inimigos = variaveis.recompensa_inimigos_base

        variaveis.mini_boss_dano = variaveis.mini_boss_dano_base
        variaveis.mini_boss_vida = variaveis.mini_boss_vida_base
        variaveis.mini_boss_recompensa = variaveis.mini_boss_recompensa_base

        variaveis.boss_dano = variaveis.boss_dano_base
        variaveis.boss_vida = variaveis.boss_vida_base
        variaveis.boss_recompensa = variaveis.boss_recompensa_base

        variaveis.quant_inimigos = variaveis.quant_inimigos_base
        variaveis.quantidade_consumiveis = variaveis.quantidade_consumiveis_base
    
        
        self.tela = variaveis.objeto_tela
        
        inventario = variaveis.inventario
        inventario.arma_base.municao = 0
        inventario.arma_adicional.municao = 0

        self.jogador = variaveis.objeto_jogador
        self.jogador.vida = variaveis.vida_jogador

        self.progresso = None
        self.jogador.status = True
        
        municao_recuperacao = Consumivel(0,0,0,0,None,True,variaveis.municao_inicio_fase,"munição")
        self.jogador.inventario.arma_uso = self.jogador.inventario.arma_adicional
        municao_recuperacao.recuperar_valor(self.jogador,None)
        self.jogador.inventario.arma_uso = self.jogador.inventario.arma_base
        municao_recuperacao.recuperar_valor(self.jogador,None)

        self.mapa = variaveis.objeto_mapa

        self.fase = Fase(self.mapa,self.jogador,1)

    def fim_do_jogo(self):


        pygame.mouse.set_visible(True)
        texto_ajuda = self.tela.fonte.render(str("Pressione ESC para voltar"), True, (255,255,255))
        texto_derrota = self.tela.fonte.render("Derrota" , True, (255,0,0))
        texto_vitoria = self.tela.fonte.render("Vitória", True, (0,255,0))
        
        if self.situacao_final == "ganhou":
            executar = True
            while executar:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            executar = False            
                self.tela.tela.fill((0,0,0))
                self.tela.tela.blit(texto_vitoria, (300,200))
                self.tela.tela.blit(texto_ajuda, (125,350))
                self.tela.atualizar_tela()
            
        
        else:
            executar = True
            while executar:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            executar = False
                
                self.tela.tela.fill((0,0,0))
                self.tela.tela.blit(texto_derrota, (300,200))
                self.tela.tela.blit(texto_ajuda, (125,350))                
                self.tela.atualizar_tela()
        self.resetar_valores()
        historinha6(None)

if __name__ == "__main__":

    tela = variaveis.objeto_tela

    inventario = variaveis.inventario

    jogador = variaveis.objeto_jogador

    mapa = variaveis.objeto_mapa
    fase = Fase(mapa,jogador,1)

    jogo = Jogo(tela,fase,jogador)
    historinha1(None)
