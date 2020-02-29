import matplotlib.pyplot as plt
x = [0,0,3,2,1,1,4,3,4,7,0]
y = [0,7,4,3,4,1,1,2,3,0,0]

matriz = [[[0,0,3,2,1,1,4,3,4,7,0],[0,7,4,3,4,1,1,2,3,0,0]]]
tamanho_x = (max(matriz[-1][0]) -max(matriz[-1][0])) * 2 
tamanho_y = (max(matriz[-1][1]) - min(matriz[-1][1])) * 2


novo_x = []
for i in range(len(matriz[0][0])):
    novo_x.append(matriz[0][0][i] * -1)
matriz.append([novo_x, matriz[0][1]])

novo_y = []
for i in range(len(matriz[0][1])):
    novo_y.append(matriz[0][1][i] * -1)
matriz.append([matriz[0][0], novo_y])

print(matriz)
print(tamanho_x)
print(tamanho_y)
print()
print()
print(novo_x)
print(novo_y)
matriz.append([matriz[1][0], matriz[2][1]])
print(matriz)
print()
print()
matriz2 = []
for i in range(len(matriz)):
    novo_x = []
    novo_y = []
    for j in range(len(matriz[i][0])):
        novo_x.append(matriz[i][0][j] + tamanho_x)
        novo_y.append(matriz[i][1][j] + tamanho_y)
    matriz2.append([novo_x, novo_y])

matriz3 = []
for i in range(len(matriz)):
    novo_x = []
    novo_y = []
    for j in range(len(matriz[i][0])):
        novo_x.append(matriz[i][0][j] + tamanho_x)
        novo_y.append(matriz[i][1][j] + 0)
    matriz3.append([novo_x, novo_y])

matriz4 = []
for i in range(len(matriz)):
    novo_x = []
    novo_y = []
    for j in range(len(matriz[i][0])):
        novo_x.append(matriz[i][0][j] + 0)
        novo_y.append(matriz[i][1][j] + tamanho_y)
    matriz4.append([novo_x, novo_y])
    
print(matriz)
print(matriz2)

for figura in range(len(matriz)):
    plt.plot(matriz[figura][0], matriz[figura][1])
    plt.plot(matriz2[figura][0], matriz2[figura][1])
    plt.plot(matriz3[figura][0], matriz3[figura][1])
    plt.plot(matriz4[figura][0], matriz4[figura][1])
    
plt.grid(True)
plt.show() 

