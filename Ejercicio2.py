#Ejercicio 2
#Escribir una función iterativa que calcule la potenciación de un numero. 
#Recibe como parámetros dos números (naturales) a y b devuelve el valor de a**b.

def potencia_iterativa(a,b):
    result = 1
    for x in range(b):
        result *= a
        return result
    
