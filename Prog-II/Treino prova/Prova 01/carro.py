class Carro:

    def __init__(self,numero_serie, modelo, marca, ano):
        self.numero_serie = numero_serie
        self.modelo = modelo
        self.marca = marca
        self.ano = ano

lista_de_carros = []
numero_serie = 97

for cont in range(0,5):

    modelo = chr(numero_serie).upper()
    marca = modelo*2
    ano = (1903 + numero_serie)

    lista_de_carros.append(Carro(numero_serie,modelo,marca,ano))
    numero_serie = numero_serie + 1  