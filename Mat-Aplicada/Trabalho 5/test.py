import numpy as np

a = 2
b = 4
c = 6

a2 =3
b2 =6
c2 =9

#1x + 1y = 5

pontos = []

y = c/b
x = c/a

y2 = c2/b2
x2 = c2/a2

pontos.append([x,0])
pontos.append([0,y])

pontos2 = []
pontos2.append([x2,0])
pontos2.append([0,y2])

lista = [[a,b],[a2,b2]]
A = np.array(lista)
B = np.array([c,c2])
X = np.linalg.solve(A,B)
print(X)
