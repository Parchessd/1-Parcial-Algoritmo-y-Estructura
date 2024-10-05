#Ejercicio 1
#Dadas las funciones ExVar1(), ExVar2(), y ExVar3(), calcular el resultado de ejecutar cada función considerando el alcanze de sus variables.
#Nota: Las funciones son ejecutadas en orden

x,y = 1,2

def ExVar1():
    x = 2 
    print(x)
    
def ExVar2():
    x = 5
    def ExVar21():
        global x
        print(x)
        ExVar21()
        print(x)
    
def ExVar3():   
    def ExVar31():
        global x
        print(x)
    x = 7    
    def ExVar32():
        nonlocal x
        ExVar31()
    ExVar32()    
    print(x)
    
def ExVar4():
    global x
    def ExVar41():
        x = 5
        print(x)
        ExVar41()
        print(x)
