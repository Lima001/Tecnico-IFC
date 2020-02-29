from PIL import Image
from matplotlib import pyplot


exe = True
imagem1 = Image.open("image.jpg")
imagem2 = Image.open("image.png")
imagem3 = Image.open("fundo.png")
imagem4 = Image.open("noz.png")
while exe:

        op = int(input("entre com a opcao"))

        if op == 1:
                imagem1.load()
                imagem1.show()
        
        elif op == 2:
                horizontal = imagem2.transpose(Image.FLIP_LEFT_RIGHT)
                vertical = imagem2.transpose(Image.FLIP_TOP_BOTTOM)
                
                pyplot.subplot(311)
                pyplot.imshow(imagem2)
                pyplot.subplot(312)
                pyplot.imshow(horizontal)
                pyplot.subplot(313)
                pyplot.imshow(vertical)
             
                pyplot.show()
                
        elif op == 3:
                lista_pixels = []
                tamanho = imagem1.size
                for x in range(tamanho[0]):
                        for y in range(tamanho[1]):
                                pixel = imagem1.getpixel((x,y))
                                if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                                        lista_pixels.append((x,y))
                print(lista_pixels[0::150])

        elif op == 4:
                tamanho = imagem2.size
                print(tamanho)
                corte = imagem2.crop((125,125,tamanho[0]-125,tamanho[1]-125))
        
                pyplot.subplot(311)
                pyplot.imshow(imagem2)
                pyplot.subplot(313)
                pyplot.imshow(corte)

                pyplot.show()
        
        elif op == 5:
                print(type(imagem2))
                print(imagem2.size)
                print(imagem2.format)
                print(imagem2.mode)
        
        elif op == 6:
                imagem_copia = imagem2.copy()
                imagem1_menor = imagem1.resize((100, 100))
                position = ((0), (0))
                imagem_copia.paste(imagem1_menor, position)
                imagem_copia.show()

        elif op == 7:
                imagem_cinza = imagem2.convert('L')
                imagem_cinza.show()

        elif op == 8:
                copia = imagem2.copy()
                for x in range(imagem2.size[0]):
                        for y in range(imagem2.size[1]):
                                if x%2 == 0 and y%2 != 0:
                                        copia.putpixel((x, y), (255, 0, 255))
                                elif x%2 == 0 and y%2 == 0:
                                        copia.putpixel((x, y), (0, 0, 0))
                copia.show()

        elif op == 9:
                copia = imagem1.copy()
                lista_pixels = []
                tamanho = imagem1.size
                for x in range(tamanho[0]):
                        for y in range(tamanho[1]):
                                pixel = imagem1.getpixel((x,y))
                                if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
                                        lista_pixels.append((x,y))
                
                for pixel in lista_pixels:
                        copia.putpixel(pixel, (255, 0, 0))

                copia.show()

        elif op == 10:
                copia = imagem3.copy()
                lista_pixels_noz = []
                tamanho_noz = imagem4.size
                tamanho_fundo = imagem3.size
                for x in range(tamanho_noz[0]):
                        for y in range(tamanho_noz[1]):
                                if imagem4.getpixel((x,y)) != (255,255,255):
                                        lista_pixels_noz.append(imagem4.getpixel((x,y)))


                for x in range(tamanho_fundo[0]):
                        for y in range(tamanho_fundo[1]):
                                pixel = imagem3.getpixel((x,y))
                                if pixel in lista_pixels_noz:
                                        copia.putpixel( (x,y), (255, 0, 0))

                copia.show()

                
        elif op == 11:
                exe = False