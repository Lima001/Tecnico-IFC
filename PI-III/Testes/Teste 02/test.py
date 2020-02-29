from PIL import Image

imagem = Image.open("imagem5.png")
tamanho = imagem.size
inicio = []


for x in range(tamanho[0]):
    for y in range(tamanho[1]):
            pixel = imagem.getpixel((x,y))
        
            if pixel != (255,255,255,255):
                inicio.append((x,y))
                


#coordenadas.sort()

coordenadas = [inicio[0]]

def achar_ponto(ponto,lista):

    analise = []
    for x in range(ponto[0]-1,ponto[0]+2):
        for y in range(ponto[1]-1,ponto[1]+2):
            pixel = imagem.getpixel((x,y))
            if pixel != (255,255,255,255) and (x,y) != ponto and (x,y) not in lista:
                analise.append((x,y))
    
    if len(analise) != 0 :
        return analise[0]
    
    #elif len(analise) > 1:
    #    for i in analise:
    #        if i[0] == ponto[0] or i[1] == ponto[1]:
    #            return i
        
    #    return analise[0]
    
    else:
        return None

ponto_inicio = inicio[0]
exe = True
while exe:
    
    ponto = achar_ponto(ponto_inicio,coordenadas)
    if ponto is not None:
        coordenadas.append(ponto)
        ponto_inicio = ponto
    else:
        exe = False

print()
print(coordenadas)
print()
print(len(inicio))
print(len(coordenadas))