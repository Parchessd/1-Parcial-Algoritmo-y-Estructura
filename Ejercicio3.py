#Ejercicio 3
#Escribir una función recursiva que calcule la potenciación de un numero. 
#Recibe como parámetros dos números (naturales) a y b devuelve el valor de a**b.

def potencia_recursiva(a , b):
    if b <= 0:
        return 1
    else:
        return a * potencia_recursiva(a, b - 1)
    
