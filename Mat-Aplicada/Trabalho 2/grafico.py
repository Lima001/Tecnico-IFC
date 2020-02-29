#import matplotlib
from matplotlib.pyplot import figure, show
import matplotlib.pyplot as plt
from numpy import arange, sin, pi, cos, tan
import numpy as np
import math

def a1(x,a,b,c,d):
    return a*sin(b*x+c)+d

def a2(x,a,b,c,d):
    return a*cos(b*x+c)+d

def a3(x,a,b,c,d):
    return a*tan(b*x+c)+d


if __name__ == '__main__':
    
    

    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    d = float(input("D: "))

    p = ((2*math.pi)/b)
    x = arange(0.0,p,0.1)
    fig = figure(0.5)

    y1 = a1(x,a,b,c,d)
    y2 = a2(x,a,b,c,d)
    y3 = a3(x,a,b,c,d)

   
    ax1 = fig.add_subplot(111)
    ax1.set_xticks([0., .5*np.pi, np.pi, 1.5*np.pi, 2*np.pi])
    ax1.set_xticklabels(["$0$", r"$\frac{1}{2}\pi$",r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
    ax1.plot(x, sin(2*math.pi*x))
    ax1.grid(True)
    ax1.set_ylim((-3, 3))
    ax1.set_ylabel('')
    ax1.set_title('seno')

    plt.draw()   
    plt.show()
