import numpy as np
import matplotlib.pyplot as plt



        

lista_x=[0,7,7,4,5,6,6,3,4,3,0]
lista_y=[7,7,0,3,4,3,6,6,5,4,7]

n_l=[7,14,14,11,12,13,13,10,11,10,7]

n=[6,20,20,14,16,18,18,12,14,12,6]






#Multiplica os elementos a escala
#for i in lista_x:
    #print(i*2)
    
    
    
    


'''
novo_x = 2*[-4,-8,-8,-4]
novo_y = [-2,-1,-4,-2]


'''
#plt.axis([0,10,0,5])

#plt.fill(lista_x,lista_y,'b')
plt.plot(lista_x,lista_y)
plt.fill(n_l,lista_y)
plt.grid(True)
plt.show()


