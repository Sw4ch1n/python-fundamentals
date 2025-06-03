def addition(a,b): #Definimos la funcion e indicamos los argumentos
    return a + b #Retornamos la operacion
    
numA = int(input("Ingresa un numero: "))
numB = int(input("Ingresa otro numero: ")) #Solicitamos los numeros al usuario

resultado = addition(numA,numB)#Llamamos a la funcion y le pasamos los argumentos que pide, igual se asigna a una variable para usarla en el print

print(f"La suma de {numA} y {numB} es {resultado}")

'''
Usa return cuando quieras desacoplar la lógica de la presentación.
la presentacoin son los prints
'''