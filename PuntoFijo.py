#metodo del punto fijo
import math
import matplotlib.pyplot as plt
def funcion(x):
    return -x**2 + 1.8*x + 2.5

a = 0
b = 4

xs = []
fxs = []

#buscamos 0
for x in range(a, b+1):
    xs.append(x)
    fxs.append(funcion(x))
    if(fxs[x] == 0):
        print(f"La raíz está en x ={x}")
        break
    else: None


# Buscamos el rango en el que fx cambia de signo, debido a que ahí está la raíz
# en este caso, la raíz está entre 0 y 1

#Proponemos un nuevo valor inicial

a = 5

#Hacemos el cálculo del error

def error(xi, xold):
    return abs((xi - xold) / xi) * 100

#hecho esto, usaremos la funcion despejada

def funcionDespejada(x):
    return -x**2 + 2.8*x + 2.5

# Empezamos a iterar mientras el error sea mayor a la tolerancia
error_ = 100
tolerancia = 0.5
i = 0
iteraciones = 10

xi = []
errores = []

while(i <= 5):
    xi.append(a)
    a = funcionDespejada(a)

    if(a == 0):
        break
    i = i+1

print(xi, errores)