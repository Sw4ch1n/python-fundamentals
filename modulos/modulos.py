'''
Importar modulos
Mostrar opciones, pedir números, ejecutar operación y mostrar resultado
'''

import calculadora #hay dos formas de importar, puede ser todas las funciones importando todo el script
from calculadora import sumar #O una funcion especifica



def user_menu():
    while True: # Si se coloca un While True se hace una condicion infinita hasta que se termine con un break, se puede usar una condicion seguido del While donde si la condicion no se cumple se vuelve While False y se termina
        choise = int(input("\nSelecciona una opcion:\n1. Sumar\n2. Restar\n3. Multiplicar\n4.Dividir\n5. Mostrar todos los resultados\n6. Salir\n")) #siendo que es True el input siempre se repetira hasta llegar al break
        num1 = float(input("Ingresa primer numero:\n"))
        num2 = float(input("Ingresa segundo numero\n"))
        
        if  choise == 1:
            result1 = sumar(num1,num2) #Aqui llamamos la funcion importada y le pasamos los argumentos que solicita
            print(result1)
             
        elif choise == 2:
            result2 = calculadora.restar(num1,num2) #Aqui llamamoa la funcion escribiendo el modulo seguido de un punto funcion e igual se le pasan los parametros que solicita
            print(f"\n{result2}\n")
            
        elif choise == 3:
            number_range = int(input("\nHasta que numero quieres saber cuantos pares hay:\n"))
            #par_number (number_range)
        
        elif choise == 4:
            print("Hasta luego!")
        
        elif choise == 5:
            print("Hasta luego!")
        
        elif choise == 6:
            print("Hasta luego!")
            break
                
        else:
            print("Numero invalido, selecciona otra opcion")
            return



user_menu()