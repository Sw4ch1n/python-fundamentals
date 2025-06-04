'''Ejercicio A: Números pares del 1 al 100
# Usar for para imprimir todos los pares del 1 al 100

Ejercicio B: Menú interactivo con while
# Mostrar un menú con opciones hasta que el usuario elija "Salir"
# Ej: 1. Saludar  2. Mostrar fecha  3. Salir
'''



def par_number(limit):
    total_pares = 0
    list_par = [] #Se crea una lista para ir guardando los numeros pares
    for i in range (limit): #Para calcular los numeros pares del 1 al 100 se usa una iteracion
        if i % 2 == 0: #una calculo de residuo para validar usando el operador %, la validacion consiste en que si el residuo es 0 es par
            list_par.append(i)
            total_pares += 1
    print(f"En el rango del 0 al {limit} hay {total_pares} numeros pares")
    print(f"Los numeros son:\n{list_par}")
    

def user_menu():
    while True: # Si se coloca un While True se hace una condicion infinita hasta que se termine con un break, se puede usar una condicion seguido del While donde si la condicion no se cumple se vuelve While False y se termina
        choise = int(input("\nSelecciona una opcion:\n1. Saludar\n2. Mostrar fecha\n3. Contar Impares\n4.Salir\n")) #siendo que es True el input siempre se repetira hasta llegar al break
        
        if  choise == 1:
            print("\nHola como estas\n")
             
        elif choise == 2:
            print("\nMas adelante se muestra la fecha\n")
            
        elif choise == 3:
            number_range = int(input("\nHasta que numero quieres saber cuantos pares hay:\n"))
            par_number (number_range)
        
        elif choise == 4:
            print("Hasta luego!")
            break    
        else:
            print("Numero invalido, selecciona otra opcion")
            return



user_menu()