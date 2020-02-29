from PIL import Image

class ImagemAnalise:

    def __init__(self,endereco,cor=(0,0,0,255),cor_fundo=(255,255,255,255),cor_referencia_inicial=(255,0,0,255)):
        self.endereco = endereco
        self.cor = cor
        self.cor_referencia_inicial = cor_referencia_inicial
        self.cor_fundo = cor_fundo
        self.imagem = None
        self.tamanho = None
        self.pixel_inicio = None
        self.direcao = (0,0)
        self.pontos = None

    #Cor padrão da trajetória = Preto --- Cor de fundo padrão = Branco
    def inicializar(self):
        self.imagem = Image.open(self.endereco)
        self.tamanho = self.imagem.size
        
        self.achar_pixel_inicio()
        self.pontos = [self.pixel_inicio]
        self.preencher_pontos()
        self.achar_pixels_faltantes()


    def preencher_pontos(self):
        referencia = self.pixel_inicio
        direcao = self.direcao
        exe = True
        
        while exe:
            resultado = self.achar_pixels(referencia,direcao)
            if resultado is None:
                    exe = False
            try:
                    referencia = resultado[0]
                    direcao = resultado[1]
                    self.pontos.append(referencia)
            except:
                    exe = False

    def achar_pixel_inicio(self):
        for x in range(self.tamanho[0]):
                for y in range(self.tamanho[1]):
                        pixel = self.imagem.getpixel((x,y))
                
                        if pixel == self.cor_referencia_inicial:
                                self.pixel_inicio = (x,y)
                                return True
        return False

    #Dependendo da imagem, tal método não encontra todos os pontos, 
    #por isso é necessário um outro método complementar (achar_pixels_faltantes)
    def achar_pixels(self,referencia,direcao):
        area = []
        for x in range(referencia[0]-1,referencia[0]+2):
                for y in range(referencia[1]-1,referencia[1]+2):
                        pixel = self.imagem.getpixel((x,y))

                        if pixel != self.cor_fundo:
                                if (x,y) not in self.pontos:
                                        area.append((x,y))
        if len(area) != 0:
                for ponto in area:
                        if ponto[0] - referencia[0] == direcao[0] and ponto[1] - referencia[1] == direcao[1]:
                                return (ponto,direcao)

                return (area[0], (area[0][0]-referencia[0],area[0][1]-referencia[1]))

        return None

    def achar_pixels_faltantes(self):
        area = []
        for referencia in self.pontos:
                for x in range(referencia[0]-1,referencia[0]+2):
                        for y in range(referencia[1]-1,referencia[1]+2):
                                pixel = self.imagem.getpixel((x,y))

                                if pixel != self.cor_fundo:
                                        if (x,y) not in self.pontos and (x,y) not in area:
                                                area.append((x,y))
                                                index = self.pontos.index(referencia)
                                                self.pontos.insert(index+1,(x,y))


if __name__ == "__main__":
    
    num_im = input("Digite o numero da imagem a ser analisada: ")
    im = "../BancoImagem/imagem" + num_im + ".png"
    imagem1 = ImagemAnalise(im)
    imagem1.inicializar()
    print(imagem1.pontos)
    print(imagem1)