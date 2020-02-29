import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class MyFigure(Figure):
    def __init__(self, *args, figtitle='hi mom', **kwargs):
        """
        custom kwarg figtitle is a figure title
        """
        super().__init__(*args, **kwargs)
        self.text(0.5, 0.95, figtitle, ha='center')


formulas = ["2x+3y=7","1x-1y=1"]
a="xand é top"
#while a != "":
#    a = input("Digite: ")
#    if a != "":
#        formulas.append(a)

frmls1 = []
frmls2 = []
def asdasd(formula):
    for f1 in formulas:
        lista = []
        a= ""
        for i in f1:
            if i.isnumeric() or i=="-":
                if a.isnumeric or a=="-":
                    a = a+i
            elif a!="":
                lista.append(int(a))
                a=""
        lista.append(int(a))
        frmls2.append(lista[-1])
        lista.pop(-1)
        frmls1.append(lista)

asdasd(formulas)
#print(frmls1)
#print(frmls2)
        
def resolver(formula):
    x = formula[2]/formula[1]
    y = formula[2]/formula[0]
    return [[x,0],[0,y]]

A = np.array([frmls1])
B = np.array([frmls2])

X = np.linalg.solve(A,B)
fig = plt.figure(FigureClass=MyFigure, figtitle='my title')
ax = fig.subplots()
#print(X)
print(resolver(frmls1[0]+[frmls2[0]]))
print(resolver(frmls1[1]+[frmls2[1]]))

if len(frmls1) == 2:
    ax.plot(resolver(frmls1[0]+[frmls2[0]]))
    ax.plot(resolver(frmls1[1]+[frmls2[1]]))

plt.show()