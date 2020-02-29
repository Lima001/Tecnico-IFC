import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.ticker as ticker


def desenhar_linha_1(y,x0,x1,x2,x3):
    plt.plot(x0,y)
    plt.plot(x1,y)
    plt.plot(x2,y)
    plt.plot(x3,y)
    plt.fill(x0,y)    
    plt.fill(x1,y)
    plt.fill(x2,y)
    plt.fill(x3,y)

def desenhar_linha_2(y,x0,x1,x2,x3):
    plt.plot(x0,y)
    plt.plot(x1,y)
    plt.plot(x2,y)
    plt.plot(x3,y)
    plt.fill(x0,y)    
    plt.fill(x1,y)
    plt.fill(x2,y)
    plt.fill(x3,y)
    
def desenhar_linha_3(y,x0,x1,x2,x3):
    plt.plot(x0,y)
    plt.plot(x1,y)
    plt.plot(x2,y)
    plt.plot(x3,y)
    plt.fill(x0,y)    
    plt.fill(x1,y)
    plt.fill(x2,y)
    plt.fill(x3,y)
    
def desenhar_linha_4(y,x0,x1,x2,x3):
    plt.plot(x0,y)
    plt.plot(x1,y)
    plt.plot(x2,y)
    plt.plot(x3,y)
    plt.fill(x0,y)    
    plt.fill(x1,y)
    plt.fill(x2,y)
    plt.fill(x3,y)

x0 = eval('[' + input("Digite a primeira linha da matriz: ") + ']')
y0 = eval('[' + input("Digite a segunda linha da matriz: ") + ']')

primeiro_x = x0[0]
primeiro_y = y0[0]

x0.append(primeiro_x)
y0.append(primeiro_y)

maximo_x = max(x0)
maximo_y = max(y0)

x1 = []
x2 = []
x3 = []

y1 = []
y2 = []
y3 = []

for elemento in range(len(x0)):
    x1.append(x0[elemento]+maximo_x)
    x2.append(x1[elemento]+maximo_x)
    x3.append(x2[elemento]+maximo_x)

for elemento in range(len(y0)):
    y1.append(y0[elemento]+maximo_y)
    y2.append(y1[elemento]+maximo_y)
    y3.append(y2[elemento]+maximo_y)

for z in range(len(y0)):
    y0[z] = y0[z]* -1
    y1[z] = y1[z]* -1
    y2[z] = y2[z]* -1
    y3[z] = y3[z]* -1


desenhar_linha_1(y0,x0,x1,x2,x3)
desenhar_linha_2(y1,x0,x1,x2,x3)
desenhar_linha_3(y2,x0,x1,x2,x3)
desenhar_linha_4(y3,x0,x1,x2,x3)
plt.xticks([])
plt.yticks([])
plt.title("Translação", fontsize = 20)
plt.grid(True, linestyle="")
plt.show()


for z in range(len(y0)):
    y3[z] = y3[z]* -1
print(x3[:-1])
print(y3[:-1])
