from dromme import *

#Uso do jogador
dinheiro = 100000
municao_inicio_fase = 300

#Skins
valor_skin = 500
lista_skin = []

skin_padrao = Skin("azolf_guerra.png",0,True)
skin_padrao.texto = "Selecionado"
skin1 = Skin("donald.png",valor_skin,False)
skin2 = Skin("acenta_tijolo.png",valor_skin,False)
skin3 = Skin("hiro_shima.png",valor_skin,False)
skin4 = Skin("Iudy.png",valor_skin,False)
skin5 = Skin("carla.png",valor_skin,False)
skin6 = Skin("jackeline.png",valor_skin,False)
skin7 = Skin("nicolau.png",valor_skin,False)
skin8 =Skin("takamassa.png",valor_skin,False)
skin9 = Skin("zumbi.png",valor_skin*3,False)
lista_skin = [skin_padrao,skin1,skin2,skin3,skin4,skin5,skin6,skin7,skin8,skin9]

#Incremento de habilidades
preco_incremento_vida = 1000
valor_evolucao_vida = 200
preco_incremento_municao = 200 
incremento_municao = 1000

#Mira
imagem_mira = "mira.png"
tamanho_mira = (40,40)
objeto_mira = Mira(tamanho_mira[0],tamanho_mira[1],imagem_mira)

#Tela
tamanho_tela = (800,600)
tela_pos_x = 0
tela_pos_y = 0
tela_velocidade = 5
objeto_tela = Tela(tamanho_tela[0],tamanho_tela[1],tela_pos_x,tela_pos_y,tela_velocidade,objeto_mira)

#Mapa
imagem_mapa_floresta = "mapa_floresta.png"
imagem_mapa_cidade = "mapa_cidade.png"
tamanho_mapa = (4000,4000)
objeto_mapa = Mapa(imagem_mapa_floresta,tamanho_mapa[0],tamanho_mapa[1])

#Fontes
fonte = "fonte.ttf"
tamanho_fonte = 40
lista_fontes = [fonte]

#Consumiveis
quantidade_consumiveis_base = 12
quantidade_consumiveis = 12
recuperacao_kit = 400
recuperacao_municao = 100

modificadores = [1]

tamanho_kit = (30,30)
imagem_kit = "kit_medico.png"
imagem_municao = "municao.png"


#Inimigos Simples
imagem_inimigo = "zumbi.png"
dano_inimigo_base = 0.1
dano_inimigo = 0.1
velocidade_inimigo_base = 2
velocidade_inimigo = 2
vida_inimigo_base = 100
vida_inimigo = 100
quant_inimigos_base = 20
quant_inimigos = 20
tamanho_inimigos = (80,80)
recompensa_inimigos = 10
recompensa_inimigos_base = 10

#Mini boss
mini_boss_vida_base = 1200
mini_boss_vida = 1200
mini_boss_imagem = "zumbi.png"
mini_boss_dano_base= 5
mini_boss_dano = 5
mini_boss_velocidade = 3
mini_boss_tamanho = (120,120)
mini_boss_recompensa_base = 1000
mini_boss_recompensa = 1000

#Boss
boss_vida_base = 15000
boss_vida = 15000
boss_imagem = "zumbi.png"
boss_dano_base = 100
boss_dano = 100
boss_velocidade = 1
boss_tamanho = (200,200)
boss_recompensa = 10000
boss_recompensa_base = 10000

#Objetos do mapa
imagem_objeto = "predio.png"

quantidade_objetos_decorativos = 10
decoracao_cidade = "sangue.png"
decoracao_floresta = "sangue.png"
tamanho_decoracao = (60,60)

predio1 = Objeto(942.5,1281,426,343,imagem_objeto,True)
predio2 = Objeto(2169,1332,280,466,imagem_objeto,True)
predio3 = Objeto(3516,1729,352,504,imagem_objeto,True)
predio4 = Objeto(2481,2301,312,432,imagem_objeto,True)
predio5 = Objeto(1245,2637,448,376,imagem_objeto,True)
predio6 = Objeto(2179,3693,424,604,imagem_objeto,True)
predio7 = Objeto(3477,3257,336,632,imagem_objeto,True)
predio8 = Objeto(1969,390,264,640,imagem_objeto,True)

lista_objetos_floresta = [predio1,predio2,predio3,predio4,predio5,predio6,predio7,predio8]


edifio1 = Objeto(712.5,506.5,463,841,imagem_objeto,True)
edifio2 = Objeto(713,1270,462,842,imagem_objeto,True)
edifio3 = Objeto(717.5,2064,510,847,imagem_objeto,True)
edifio4 = Objeto(713.5,2837,446,833,imagem_objeto,True)
edifio5 = Objeto(714,3545.5,367,848,imagem_objeto,True)
edifio6 = Objeto(1921,505.5,397,920,imagem_objeto,True)
edifio7 = Objeto(1922,1268,400,918,imagem_objeto,True)
edifio8 = Objeto(1923,2056.5,445,926,imagem_objeto,True)

edifio9 = Objeto(1468+(912/2),2643+(386/2),386,912,imagem_objeto,True)
edifio10 = Objeto(1458+(926/2),3393+(303/2),303,926,imagem_objeto,True)
edifio11 = Objeto(2710+(1003/2),284+(444/2),444,1003,imagem_objeto,True)
edifio12 = Objeto(2719+(1004/2),1048+(444/2),444,1004,imagem_objeto,True)
edifio13 = Objeto(2709+(1008/2),1812+(491/2),491,1008,imagem_objeto,True)
edifio14 = Objeto(2713+(996/2),2622+(428/2),428,996,imagem_objeto,True)
edifio15 = Objeto(2706+(1010/2),3370+(349/2),349,1010,imagem_objeto,True)

lista_objetos_cidade = [edifio1,edifio2,edifio3,edifio4,edifio5,edifio6,edifio7,edifio8,edifio9,edifio10,edifio11,edifio12,edifio13,edifio14,edifio15]


#Armas e Tiros
# -- Tiros
tiro1 = Tiro(0,0,7,7,"tiro.png",True,15,0,30)
tiro2 = Tiro(0,0,8,8,"tiro.png",True,25,0,80)

# -- Armas
tamanho_jogador = (80,80)
tamanho_arma = tamanho_jogador[0]*2 + 10

arma_scar = Arma(0,0,tamanho_arma,tamanho_arma,"scar.png",True,80,30,30,tiro2,"lendaria",60,"scar_lateral.png",100,False)
arma_ak = Arma(0,0,tamanho_arma,tamanho_arma,"ak.png",True,40,30,30,tiro2,"rara",60,"ak1_lateral.png",100,False)
arma_deagle = Arma(0,0,tamanho_arma,tamanho_arma,"deagle.png",True,100,7,7,tiro1,"epica",21,"deagle_lateral.png",100,False)
arma_m16 = Arma(0,0,tamanho_arma,tamanho_arma,"m16.png",True,60,30,30,tiro2,"epica",60,"m16_lateral.png",100,False)
arma_uzi = Arma(0,0,tamanho_arma,tamanho_arma,"uzi.png",True,20,25,25,tiro2,"rara",75,"uzi1.png",100,True)
arma_pistola = Arma(0,0,tamanho_arma,tamanho_arma,"pistola.png",True,10,14,14,tiro1,"comum",300,"pistola_lateral.png",100,None) 

arma_pistola.texto = "Fixo"
arma_uzi.texto = "Comprado"

lista_armas = [arma_scar,arma_ak,arma_deagle,arma_pistola,arma_uzi,arma_m16]

arma_base_padrao = arma_pistola
arma_adicional_padrao = arma_uzi
arma_base_padrao.status_compra = arma_base_padrao
arma_adicional_padrao.status_compra = arma_adicional_padrao

arma_base = arma_base_padrao
arma_adicional = arma_adicional_padrao

#Inventario
inventario = Inventario(arma_base,arma_adicional,dinheiro)

#Jogador
vida_jogador = 300
pos_x_jogador = 100
pos_y_jogador = 100
tamanho_jogador = (80,80)
imagem_jogador_padrao = skin_padrao.endereco_imagem
imagem_jogador = skin_padrao.endereco_imagem
velocidade_jogador = 5
objeto_jogador = Jogador(pos_x_jogador,pos_y_jogador,tamanho_jogador[0],tamanho_jogador[1],imagem_jogador,velocidade_jogador,True,inventario,vida_jogador)