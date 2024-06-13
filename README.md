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

## Cómo Funciona el Método de la Secante

1. **Definición del Intervalo Inicial:** Se seleccionan dos puntos iniciales `x0 y x1` en el dominio de la función `f(x)`. Estos puntos iniciales deben estar lo más cerca posible de la raíz que se desea encontrar.

2. **Cálculo de la Pendiente Aproximada:** Utilizando la diferencia finita, se aproxima la pendiente de la recta secante que pasa por los puntos `(x0, f(x0))` y `(x1, f(x1))`. La pendiente aproximada se calcula como:

   `m ≈ (f(x1) - f(x0)) / (x1 - x0)`

3. **Cálculo del Punto Intermedio:** Se utiliza la ecuación de la recta para encontrar el valor de x2, donde la recta secante cruza el eje x:

   `x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))`

4. **Iteración:** Se actualizan los puntos `x0` y `x1` con `x1` y `x2`, respectivamente. Este proceso se repite hasta alcanzar la convergencia deseada o cumplir un criterio de parada predefinido.

Este enfoque ofrece una comprensión paso a paso del método, mostrando cómo se seleccionan los puntos iniciales, se calcula la pendiente aproximada, se encuentra el punto intermedio y se repite el proceso hasta encontrar una aproximación satisfactoria de la raíz.

---

¡Gracias por visitar este repositorio!

---

