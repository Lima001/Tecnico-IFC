import numpy as np
def resolver(x1,y1,x2,y2):
    lista = [[x1,1],[x2,1]]
    A = np.array(lista)
    B = np.array([y1,y2])
    X = np.linalg.solve(A,B)
    return(X)

eq1=resolver(0,3,3,0)
eq2=resolver(0,3,3,0)
if (eq1[0]*-1) - (-1*eq2[0]):
    print("POSIBRU DETERMINaDO")
else:
    cor1 = ((0,eq1[1]/-1), (eq1[1]/eq1[0],0))
    cor2 = ((0,eq2[1]/-1), (eq2[1]/eq2[0],0))

    if cor1 == cor2:
        print("Possivel indeterminado")
    else:
        print("Imposibru")

eq1= str(eq1[0])+"x-1.0y=-"+str(eq1[1])
eq2= str(eq2[0])+"x-1.0y=-"+str(eq2[1])
print(eq1)
print(eq2)

#OS PONTOSM TENQ SER PASSADOS NO 0