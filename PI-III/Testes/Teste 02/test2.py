from PIL import Image

n_imagem = input("Digite o numero da imagem: ")
im = "../BancoImagem/imagem" + n_imagem + ".png"
imagem = Image.open(im)
tamanho = imagem.size

tudo = []
for x in range(tamanho[0]):
    for y in range(tamanho[1]):
            pixel = imagem.getpixel((x,y))
        
            if pixel != (255,255,255,255):
                tudo.append((x,y))

#Procura por pixels em uma area 3X3 tendo o pixel informado como centro
def achar_pixel(referencia,direcao,lista,imagem):
        area = []
        for x in range(referencia[0]-1,referencia[0]+2):
                for y in range(referencia[1]-1,referencia[1]+2):
                        pixel = imagem.getpixel((x,y))

                        if pixel != (255,255,255,255):
                                if (x,y) not in lista:
                                        area.append((x,y))
        if len(area) != 0:
                for ponto in area:
                        if ponto[0] - referencia[0] == direcao[0] and ponto[1] - referencia[1] == direcao[1]:
                                return (ponto,direcao)

                return (area[0], (area[0][0]-referencia[0],area[0][1]-referencia[1]))

        return None

#Acha o primeiro pixel com a cor informada
def achar_inicio(imagem,tamanho,cor=(0,0,0,255)):
        for x in range(tamanho[0]):
                for y in range(tamanho[1]):
                        pixel = imagem.getpixel((x,y))
                
                        if pixel == cor:
                                return (x,y)
                                

inicio = achar_inicio(imagem,tamanho,(255,0,0,255))
referencia = inicio
direcao = (0,0)
lista = [inicio]
exe = True

while exe:

        resultado = achar_pixel(referencia,direcao,lista,imagem)
        if resultado is None:
                exe = False
        try:
                referencia = resultado[0]
                direcao = resultado[1]
                lista.append(referencia)
        except:
                exe = False

print(len(lista))
print(len(tudo))

cont = 1
for x in tudo:
        if x not in lista:
                print(str(cont) + " " + str(x))
                cont += 1


progress = input("Digite 0 para parar. Para prosseguir, pressione qualquer tecla. --> ")
if progress == "0":
        exit(0)



# Pegar pontos faltantes e adicionar na lista de coordenadas
area = []
for referencia in lista:
        for x in range(referencia[0]-1,referencia[0]+2):
                for y in range(referencia[1]-1,referencia[1]+2):
                        pixel = imagem.getpixel((x,y))

                        if pixel != (255,255,255,255):
                                if (x,y) not in lista and (x,y) not in area:
                                        area.append((x,y))
                                        index = lista.index(referencia)
                                        lista.insert(index+1,(x,y))

print()
print(len(lista))
print(len(tudo), end="\n")
for i in area:
        print(i, end=" / ")
print()

# Checar se os pontos foram adicionandos no local correto

for i in lista:
        print(i)

#Calcular diferença entre ponto_x e ponto_x+1 --- passar para o interpretador --- passar para o drone
diferenca = []
for x in range(len(lista)):
        if x+1 == len(lista):
                break
        else:
                ele1 = lista[x]
                ele2 = lista[x+1]
                dif = (ele1[0]-ele2[0],ele1[1]-ele2[1])
                diferenca.append(dif)

print(diferenca)