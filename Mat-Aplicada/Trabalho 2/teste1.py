import matplotlib.pyplot as plt
import numpy

def funcao_seno(a,b,c,d,x):
    y = a*numpy.sin(b*x+c)+d
    return y

def funcao_cosseno(a,b,c,d,x):
    y = a*numpy.cos(b*x+c)+d
    return y

if __name__=="__main__":
    a= float(input("digite a: "))
    b= float(input("digite b: "))
    c= float(input("digite c: "))
    d= float(input("digite d: "))

    p = 2*((2*numpy.pi)/b)
    x = numpy.arange(0.0,p,0.1)
    y1 = funcao_seno(a,b,c,d,x)
    fig, ax = plt.subplots()
    ax.plot(x,y1)

    plt.show()
