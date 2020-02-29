#ax + by = c

a1=-1
b1=1
c1=3

a2=-8
b2=8
c2=24


cor1 = None
cor2 = None

cor1 = ((0,b1/c1), (a1/c1,0))
cor2 = ((0,b2/c2), (a2/c2,0))

if cor1 == cor2:
    print("Possivel indeterminado")

    lista = [a1,b1,c1]
    menor = min(lista)
    if menor<0:
        menor = -1*menor
    
    for i in range(menor,1,-1):
        print("aaa")
        if a1%i == 0 and b1%i == 0 and c1%i == 0:
            a1 =  a1/i
            print(a1)
            b1 = b1/i 
            print(b1)
            c1 = c1/i 
            print(c1) 
            break
    if a1<0:
        print("x,(" + str(c1) + " +" + str(a1*(-1)) + "x)/" + str(b1))
    else:
        print("x,(" + str(c1) + " -" + str(a1) + "x)/" + str(b1))  

else:
    print("Imposivel")