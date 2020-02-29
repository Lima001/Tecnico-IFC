import matplotlib.pyplot as plt


"""
FALTA FAZER
-TRANSLAÇÃO (DESCOBRIR MEIO!)
-ROTAÇÃO - NÃO APARECE NO GRÁFICO
"""



#faz o poligono normal
x = [0,0,3,2,1,1,4,3,4,7,0]
y = [0,7,4,3,4,1,1,2,3,0,0]

#faz o processo de escala o poligono aumentando duas vezes seu tamanho
x_escala = []
y_escala = []

#faz com que possamos fazer a reflexão para o lado, combinando as coordenadas que já possuimos do y normal e do y translatado
#com as coordenadas de x, formando pares no estilo x multiplicado por menos 1 e x normal e y translatado e x da multiplicado por menos para a fazer a reflexão
x_reflexao_lado = []
x_reflexao_lado_escala = []

#faz com que inverta pra baixo no lado esquerdo combinando as coordenadas como foi feito na reflexão do lado
y_reflexão_baixo = []
y_reflexão_baixo_escala = []



#faz rotação de 180 graus
x_rotação_180_origin = []
y_rotação_180_origin = [] 


#rotação_180 graus
for e in x:
    s = e*-1
    x_rotação_180_origin.append(s)

for d  in y:
    ff = d *-1
    y_rotação_180_origin.append(ff)
    

#translata
for j in x:
    a = j / 2
    x_escala.append(a)

for k in y:
    b = k / 2
    y_escala.append(b)

#reflete por ladinho
for r in x:
    ç = r * -1
    x_reflexao_lado.append(ç)

for o in x_escala:
    v = o * -1
    x_reflexao_lado_escala.append(v)

#reflete pra baixo no lado esquerdo
#OBS: PARA O LADO DIREITO BASTA RECOMBINAR AS COORDENADAS
for q in y:
    g = q *-1
    y_reflexão_baixo.append(g)

for t in y_escala:
    w = t*-1
    y_reflexão_baixo_escala.append(w)






#normal
plt.fill(x,y,'b')

"""
#escala
plt.fill(x_escala, y_escala, "r")
"""

#refletir para o lado esquerdo normal
plt.fill(x_reflexao_lado, y, "g")

"""
plt.fill(x_reflexao_lado_escala, y_escala, "b")
"""

#refletir para baixo no lado esquerdo
"""
plt.fill(x_reflexao_lado_escala,y_reflexão_baixo_escala, "r")
"""
plt.fill(x_reflexao_lado, y_reflexão_baixo, "g")

#refletir pra baixo no lado direito
plt.fill(x, y_reflexão_baixo,"b")
"""
plt.fill(x_escala, y_reflexão_baixo_escala, "r")
"""

"""
#rotaciona 180 graus
plt.fill(x_rotação_180_origin, y_rotação_180_origin , "r")
"""
plt.grid(True)
plt.show() 

