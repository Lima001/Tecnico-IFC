import math


def calcular_angulos_internos_3_lados(a,b,c):
    A= ((((b**2) + (c**2))- a**2)/ (2*(b*c))) 
    B = ((((a**2) + (c**2)) - b**2)/ (2*(a*c)))
    C = ((((a**2) + (b**2)) - c**2)/ (2*(a*b)))
    A = math.acos(A)
    B = math.acos(B)    
    C = math.acos(C)
    Angulos = [A,B,C]
    return Angulos
    
def calcular_lado(a, b, c, angulo_A, angulo_B, angulo_C):
    angulo_A = math.radians(angulo_A)
    angulo_B = math.radians(angulo_B)
    angulo_C = math.radians(angulo_C)
    if a == 0:
        resultado = math.sqrt(((b**2) + (c**2)) - ((2*(b*c))* math.cos(angulo_A)))
    elif b == 0:
        resultado = math.sqrt(((a**2) + (c**2)) - ((2*(a*c))* math.cos(angulo_B)))
    else:
        resultado = math.sqrt(((b**2) + (a**2)) - ((2*(b*a))* math.cos(angulo_C)))
    return resultado

def calcular_angulo_A_B(a,b, angulo_B):
    angulo_B = math.radians(angulo_B)
    resultado = math.asin(((a * (math.sin(angulo_B)))/b))
    return resultado

def calcular_angulo_A_C(a,c, angulo_C):
    angulo_C = math.radians(angulo_C)
    resultado = math.asin(((a * (math.sin(angulo_C)))/c))
    return resultado

def calcular_angulo_C_B(b, c, angulo_B):
    angulo_B = math.radians(angulo_B)
    resultado = math.asin(((c * (math.sin(angulo_B)))/b))
    return resultado

def calcular_angulo_C_A(a, c, angulo_A):
    angulo_A = math.radians(angulo_A)
    resultado = math.asin(((c * (math.sin(angulo_A)))/a))
    return resultado

def calcular_angulo_B_A(a, b, angulo_A):
    angulo_A = math.radians(angulo_A)
    resultado = math.asin(((b * (math.sin(angulo_A)))/a))
    return resultado

def calcular_angulo_B_C(b, c, angulo_C):
    angulo_C = math.radians(angulo_C)
    resultado = math.asin(((b * (math.sin(angulo_C)))/c))
    return resultado



def calcular_angulo_dois(angulo_1, angulo_2):
    resultado = math.radians(180 - (angulo_1 + angulo_2))
    return resultado




def calcular_lado_A_B(b, angulo_A, angulo_B):
    angulo_B = math.radians(angulo_B)
    angulo_A = math.radians(angulo_A)

    resultado = ((b* (math.sin(angulo_A)))/ math.sin(angulo_B))
    return resultado

def calcular_lado_A_C(c, angulo_A, angulo_C):
    angulo_C = math.radians(angulo_C)
    angulo_A = math.radians(angulo_A)
    resultado = ((c* (math.sin(angulo_A)))/ math.sin(angulo_C))
    return resultado

def calcular_lado_C_B(b, angulo_C, angulo_B):
    angulo_C = math.radians(angulo_C)
    angulo_B = math.radians(angulo_B)
    resultado =((b* (math.sin(angulo_C)))/ math.sin(angulo_B))
    return resultado

def calcular_lado_C_A(a, angulo_C, angulo_A):
    angulo_A = math.radians(angulo_A)
    angulo_C = math.radians(angulo_C)
    resultado = ((a* (math.sin(angulo_C)))/ math.sin(angulo_A))
    return resultado

def calcular_lado_B_A(a, angulo_B, angulo_A):
    angulo_A = math.radians(angulo_A)
    angulo_B = math.radians(angulo_B)
    resultado = ((a* (math.sin(angulo_B)))/ math.sin(angulo_A))
    return resultado

def calcular_lado_B_C(c, angulo_C, angulo_B):
    angulo_C = math.radians(angulo_C)
    angulo_B = math.radians(angulo_B)
    resultado = ((c* (math.sin(angulo_B)))/ math.sin(angulo_C))
    return resultado



def calcular_angulos_triangulo_retângulo(cat_oposto, cat_adjacente, hipotenusa):
    angulos = []
    angulo1 = math.atan((cat_oposto/cat_adjacente))
    angulo2 = (90 - (math.degrees(angulo1)))
    angulos = [angulo1, math.radians(angulo2)]
    angulos.append(math.radians(90))
    return angulos    

def achar_lados_retângulo(angulo1, angulo2, tipo_lado, lado):
    if tipo_lado == "hipotenusa":
        cat_oposto = lado* (math.sin(math.radians(angulo1)))
        cat_adjacente =  cat_oposto * (math.tan(math.radians(angulo1)))
        return "cateto oposto: " + str(cat_oposto) + "cateto adjacente: " + str(cat_adjacente)
    
    elif tipo_lado == "cateto oposto":
        cat_adjacente = lado * (math.tan(math.radians(angulo1)))
        hipotenusa = math.sqrt((lado*lado)+(cat_adjacente*cat_adjacente))
        return "cateto adjacente: " + str(cat_adjacente) + "hipotenusa: " + str(hipotenusa)
    
    else:
        cat_oposto = lado * (math.tan(math.radians(angulo1)))
        hipotenusa = math.sqrt((lado**2)+(cat_oposto**2))
        return "cateto oposto: " + str(cat_oposto) + "hipotenusa: " + str(hipotenusa)


def achar_lado(cat_oposto, cat_adjacente, hipotenusa):
    if hipotenusa == 0:
        hipotenusa = math.sqrt((cat_oposto**2)+(cat_adjacente**2))
        return hipotenusa
    elif cat_oposto == 0:
        cat_oposto = math.sqrt((hipotenusa**2)- (cat_adjacente**2))
        return cat_oposto
    if cat_adjacente == 0:
        cat_adjacente = math.sqrt((hipotenusa**2)- (cat_oposto**2))
        return cat_adjacente




