# Método de Bisección

Este repositorio contiene una implementación del método de bisección en Python.

## Descripción

El método de bisección es un algoritmo para encontrar raíces de funciones continuas. Es un método iterativo que reduce el intervalo en el que se encuentra la raíz en cada paso. Este método es especialmente útil para encontrar soluciones a ecuaciones no lineales.

## ¿Cómo Funciona?

1. **Definición del intervalo**: Se selecciona un intervalo `[a, b]` tal que `f(a)` y `f(b)` tengan signos opuestos, indicando que hay al menos una raíz en el intervalo.
2. **Cálculo del punto medio**: Se calcula el punto medio `c = (a + b) / 2`.
3. **Evaluación de la función en el punto medio**: Se evalúa `f(c)`.
4. **Actualización del intervalo**: Dependiendo del signo de `f(c)`, el intervalo se reduce a `[a, c]` o `[c, b]`.
5. **Repetición**: El proceso se repite hasta que se cumple un criterio de parada (como una tolerancia o un número máximo de iteraciones).

El código para hallar una raíz con este método esta hecho en python y se encuentra en este repositorio con nombre "MetodoBiseccion".


# Método de la Secante

Este repositorio contiene una implementación del Método de la Secante en Python.

## Descripción

El Método de la Secante es un algoritmo numérico utilizado para encontrar aproximaciones de las raíces de una función real continua. A diferencia del Método de Newton-Raphson, el Método de la Secante no requiere la evaluación de la derivada de la función en cada iteración, lo que lo hace útil cuando la derivada no está fácilmente disponible o es costosa de calcular.

## Cómo Funciona

1. **Definición del Intervalo Inicial**: Seleccionamos dos puntos iniciales \( x_0 \) y \( x_1 \) en el dominio de la función \( f(x) \). Estos dos puntos iniciales deben estar lo más cerca posible de la raíz que queremos encontrar.

2. **Cálculo de la Pendiente Aproximada**: Utilizamos la diferencia finita para aproximar la pendiente de la recta secante que pasa por los puntos \( (x_0, f(x_0)) \) y \( (x_1, f(x_1)) \). La pendiente aproximada se calcula como:
   \[
   m \approx \frac{{f(x_1) - f(x_0)}}{{x_1 - x_0}}
   \]

3. **Cálculo del Punto Intermedio**: Usamos la ecuación de la recta para encontrar el valor de \( x_2 \) donde la recta secante cruza el eje \( x \):
   \[
   x_2 = x_1 - \frac{{f(x_1) \cdot (x_1 - x_0)}}{{f(x_1) - f(x_0)}}
   \]

4. **Iteración**: Actualizamos los puntos \( x_0 \) y \( x_1 \) con \( x_1 \) y \( x_2 \), respectivamente, y repetimos el proceso hasta que se alcance la convergencia deseada o se cumpla un criterio de parada predefinido.

## Uso

Aquí hay un ejemplo de cómo utilizar el script del Método de la Secante:

```python

# Definir la función
def f(x):
    return x**3 - 2*x - 5

# Definir los puntos iniciales
x0 = 1
x1 = 2

# Llamar al Método de la Secante
raiz = secante(f, x0, x1)

print(f"La raíz aproximada es: {raiz}")

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    iteracion = 0
    while iteracion < max_iter:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0 = x1
        x1 = x2
        iteracion += 1
    return None
```
---

¡Gracias por visitar este repositorio!

---

