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

El código para hallar una raíz esta hecho en python y se encuentra en este repositorio con nombre "MetodoBiseccion".
