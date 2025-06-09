'''
Ejercicio A: División segura
# Pedir dos números y dividirlos
# Si el segundo número es cero, capturar el error con try/except y mostrar mensaje

Ejercicio B: Entrada segura
# Pedir al usuario que escriba un número
# Si escribe texto, capturar ValueError y mostrar error

'''

def validation ():
    while True:        
        try :
            num_A = float(input("\nIngresa primer numero para divir: "))
            num_B = float(input("\nIngresa segundo numero para divir: "))
            try:
                resultado = num_A / num_B
                print(resultado)
                
                while True : 
                    choise = input("Deseas volver a divir?: ").lower()
                    if choise == "n":
                        return
                    elif choise == "y":
                        break
                    else:
                        print("Solo puedes ingresar y o n")
                
            except ZeroDivisionError:
                print("No se puede divir entre cero, vuelva a intentarlo")
        except ValueError:
            print("Solo puedes ingresar numeros")

            

            
validation()