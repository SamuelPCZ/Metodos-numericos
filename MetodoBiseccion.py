#Método de bisección

def funcion(x):
    y = (x-3)**3
    return y

def puntoMedio(a, b):
    xn = (a+b)/2
    return xn

def error(Xactual, Xantiguo):
    return abs((Xactual - Xantiguo)/Xactual)*100
    
a = 1
b = 6
error_ = 100
tolerancia = 1E-3
Error_ = []
Xtotal = []
Itotal = []
i = 0
fa = funcion(a)
fb = funcion(b)
  
while (error_ >= tolerancia):
       
    if (fa == 0):
        print(f"La raíz está en el punto a: {a}")
        break
    elif (fb == 0):
        print(f"La raíz está en el punto b: {b}")
        break

    xn = puntoMedio(a, b)
    fxn = funcion(xn)
    Xtotal.append(xn)
    Itotal.append(i)

    if (i == 0):
        Error_.append(100)
    else:
        error_ = error(Xtotal[i], Xtotal[i-1])
        Error_.append(error_)

    if (fa * fxn) < 0:
        b = xn 
        fb = fxn
    else:
        a = xn
        fa = fxn          

    if (error_ < tolerancia):
        print(f"La raíz aproximada está en el punto Xn: {xn}")
        break

    i += 1

# Imprimir los resultados
for j in range(len(Xtotal)):
    print(f"Iteración {j}: Xn = {Xtotal[j]}, Error = {Error_[j]}%")


