'''
Importar modulos
Mostrar opciones, pedir números, ejecutar operación y mostrar resultado
'''

import calculadora #hay dos formas de importar, puede ser todas las funciones importando todo el script
from calculadora import sumar #O una funcion especifica


def user_menu():
    while True: # Si se coloca un While True se hace una condicion infinita hasta que se termine con un break, se puede usar una condicion seguido del While donde si la condicion no se cumple se vuelve While False y se termina
        choise = int(input("\nSelecciona una opcion:\n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Hacer todas las operaciones\n6. Salir\n")) #siendo que es True el input siempre se repetira hasta llegar al break

        if 1 <= choise <= 5 :
            num1 = float(input("Ingresa primer numero:\n"))
            num2 = float(input("Ingresa segundo numero\n"))
            
            if  choise == 1:
                result1 = sumar(num1,num2) #Aqui llamamos la funcion importada y le pasamos los argumentos que solicita
                print(result1)

            elif choise == 2:
                result2 = calculadora.restar(num1,num2) #Aqui llamamoa la funcion escribiendo el modulo seguido de un punto funcion e igual se le pasan los parametros que solicita
                print(f"\n{result2}\n")

            elif choise == 3:
                result3 = calculadora.multiplicar(num1,num2)
                print(f"\n{result3}\n")

            elif choise == 4:
                result4 = calculadora.dividir(num1,num2)
                print(f"\n{result4}\n")

            elif choise == 5:
                print(f"la suma: {sumar(num1,num2)}")
                print(calculadora.restar(num1,num2))
                print(calculadora.multiplicar(num1,num2))
                print(calculadora.dividir(num1,num2))

        elif choise == 6:
            print("Bye")
            break
                
        else:
            print("Opcion invalida, selecciona otra opcion")


user_menu()