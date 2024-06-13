#Falsa posición
def funcion(x):
    y = x**4 - 8*(x**3)-35*(x**2)+ 450*x - 1001
    return y

def errorAprox(Xactual, Xantiguo):
    return abs((Xactual - Xantiguo)/Xactual)*100

def errorAbs(XCalculado, Xverdadero):
    return abs(Xverdadero - XCalculado)

def falsaPosicion(a, b, fa, fb):
    return (a-fa)*((b-a)/ (fb-fa))

a = 3.0
b = 6.0
fa = funcion(a)
fb = funcion(b)
i = 0
error_ = 1
Erroresabs = []
ErroresAprox = []
Xntotal = []
raiz = 5.60979
tolerancia = 0.01

while(i < 5 and error_ >= tolerancia):

    if(fa == 0):
        print(f"la raíz esta en el punto {a}")
        break
    elif(fb == 0):
        print(f"La raíz esta el el punto {b}")
        break

    xn = falsaPosicion(a,b,fa,fb)
    fxn =  funcion(xn)
    Xntotal.append(xn)

    if(i == 0):
        error_ = 100
        ErroresAprox.append(error_)
        Erroresabs.append(error_)
    else:
        error_ = errorAprox(Xntotal[i], Xntotal[i-1])
        ErroresAprox.append(error_)
        Erroresabs.append(errorAbs(xn, raiz))

    if((fa * fb) <= 0):
            if(fxn == 0):
             print(f"La raíz de la función esta en el punto Xn: {xn}")
             break
            else:
                 if((fa * fxn) < 0):
                      b = xn
                      fb = fxn
                 else:
                      a = xn
                      fa = fxn
    else:
             print(f"La raíz no se encuentra entre a [{a}] y b [{b}]")
             break
    i = i+1

print(f"la raíz aproximadamente está en: {Xntotal}")
