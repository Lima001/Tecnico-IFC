import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.ticker as ticker



x0 = [0,7,7,4,5,6,6,3,4,3,0]
y0 = [7,7,0,3,4,3,6,6,5,4,7]

x1 = []
for elemento in range(len(x0)):
    x1.append(x0[elemento]+7)

x2 = []
for elemento in range(len(x0)):
    x2.append(x1[elemento]+7)

x3 = []
for elemento in range(len(x0)):
    x3.append(x2[elemento]+7)

y1 = []
for elemento in range(len(x0)):
    y1.append(y0[elemento]+7)

y2 = []
for elemento in range(len(x0)):
    y2.append(y1[elemento]+7)

y3 = []
for elemento in range(len(x0)):
    y3.append(y2[elemento]+7)


x =[]
y = []
for a in range(4):
    for z in range(len(x0)):
        x.append(x0[z])
    for z in range(len(x0)):
        x.append(x1[z])
    for z in range(len(x0)):
        x.append(x2[z])
    for z in range(len(x0)):
        x.append(x3[z])

print(x)
for v in range(4):
    for a in range(len(y0)):
        y.append(y0[a])
for v in range(4):
    for a in range(len(y0)):
        y.append(y1[a])
for v in range(4):
    for a in range(len(y0)):
        y.append(y2[a])
for v in range(4):
    for a in range(len(y0)):
        y.append(y3[a])
print(y)
"""
for z in range(len(y0)):
    y0[z] = y0[z]* -1
    y1[z] = y1[z]* -1
    y2[z] = y2[z]* -1
    y3[z] = y3[z]* -1

"""

x0 = [0,7,7,4,5,6,6,3,4,3,0]
y0 = [7,7,0,3,4,3,6,6,5,4,7]

x11 = [7,0,0,3,2,1,1,4,3,4,7]
y00 = [0,0,7,4,3,4,1,1,2,3,0]


plt.plot(x11,y00)
plt.plot(x2,y0)
plt.plot(x3,y0)
"""

plt.plot(x1,y1)
plt.plot(x2,y1)
plt.plot(x3,y1)

plt.plot(x0,y2)
plt.plot(x1,y2)
plt.plot(x2,y2)
plt.plot(x3,y2)

plt.plot(x0,y3)
plt.plot(x1,y3)
plt.plot(x2,y3)
plt.plot(x3,y3)
"""
plt.grid(True, linestyle="--")
plt.show()

print(x3)
print(y3)
print()
print(x3)
print(y2)
print()
print(x2)
print(y2)
