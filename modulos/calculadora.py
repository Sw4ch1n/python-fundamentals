'''
Ejercicio:
Define funciones:

sumar(a, b)

restar(a, b)

multiplicar(a, b)

dividir(a, b)

main.py
Importa las funciones de calculadora.py y ejecuta un pequeño menú:


from calculadora import sumar, restar

# Mostrar opciones, pedir números, ejecutar operación y mostrar resultado

'''

def sumar(a,b):
    resultado_sum = a + b
    return resultado_sum

def restar(a,b): 
    return a - b #Es una forma mas facil y con menos lineas de devolver un valor

def multiplicar(a,b):
    resultado_mult = a * b
    return resultado_mult

def dividir(a,b):
    resultado_div = a / b
    print(resultado_div)
    return resultado_div
