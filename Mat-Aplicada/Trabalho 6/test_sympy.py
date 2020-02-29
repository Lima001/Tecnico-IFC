from sympy import *


def formatar(eq):
    eq_formatada = eq[:eq.index("=")]
    eq_formatada = eq_formatada + "-" + eq[eq.index("=")+1:]
    equacao = list(eq_formatada)
    for x in equacao:
        if x == " ":
            equacao.remove(x)

    for x in range(len(equacao)):
        if equacao[x].isalpha() and x!= 0 and equacao[x-1].isalnum():
            equacao[x-1] = equacao[x-1] + "*"
        
    retorno = ""
    for x in equacao:
        retorno = retorno + x
    return retorno


            

print(formatar("2x + y = 2"))


'''
x, y = symbols('x, y')

eq1 = '4*x+2*y-3 - -4'
eq2 = '4*x+2*y-3 - -4'


print(solve(['2*x + y -7', 'x + 2*y -5'], (x, y)))


#############
eq_original = '1 x + 1 y = -3'
eq = eq_original[0:eq_original.index("=")] + "-" + eq_original[eq_original.index("=")+1:]
for x in range(len(eq)):
    try:
    	numero = int(eq[x])
    	if eq[x+1] == 'x' or eq[x+1] == 'y':
		    eq = eq[0:x] + eq[x] + '*' + eq[x+1:]
    except:
        pass
print(eq)
print(type(eq))
##############

x, y = symbols('x, y')
print(x)
print(y)
eq1 = eq
eq2 = eq

print(eq)
print(solve([eq1, eq2], [x, y]))
'''
