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

lista_variaveis =[]
lista_equacoes = []
solucao = None

quantidade = int(input("Considere nxn, Digite o valor de n: "))

for cont in range(quantidade):

    simbolo = input("Digite o simbolo da variavel: ")

    codigo_string = "simbolo = symbols(simbolo)"
    exec(codigo_string)
    
    lista_variaveis.append(simbolo)
    
for cont in range(quantidade):

    equacao = input("Digite a equação (ex: ax+by = C --> ax+by-c): ")
    lista_equacoes.append(formatar(equacao))

print(lista_variaveis)
print()
print(lista_equacoes)
print()
solucao = solve(lista_equacoes,lista_variaveis)
print(solucao)

