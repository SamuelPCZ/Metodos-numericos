a = 0
b = 7
i = 0
error = 100
tolerancia = 0.01

def funcion(x):
    return x**2 - 3*x - 4

def pendiente(x0, x1):
    return (funcion(x1) - funcion(x0)) / (x1 - x0)

def error_(xant, xnuev):
    return abs((xnuev - xant) / xnuev) * 100

while error >= tolerancia:
    try:
        xn = a - (funcion(a) / pendiente(a, b))
    except ZeroDivisionError:
        print("División entre cero en el cálculo de la pendiente. Verifica los valores de entrada.")
        break

    #print(f"Iteración {i}: xn = {xn}, error = {error:.6f}%")

    error = error_(a, xn)
    
    if error < tolerancia:
        print(f"La raíz aproximada está en el punto Xn: {xn} con un error de {error:.6f}%")
        break

    a, b = b, xn 

    i += 1

    #Vamos a crear una condición para evitar bucles infinitos
    if i > 1000:  
        print("Número máximo de iteraciones alcanzado.")
        break
