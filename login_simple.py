'''Ejercicio login basico'''

userName = input("Enter your username: ")
password = input("Enter your password: ")
if userName == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Login failed! Please check your username and password.")


'''Ejercicio Verificador de Edad
Escribe un programa que pida al usuario su edad y luego imprima un mensaje basado en las siguientes reglas:
Si la edad es menor de 13, imprimir "Eres un niño/a."
Si la edad está entre 13 y 17 (inclusive), imprimir "Eres un adolescente."
Si la edad es 18 o mayor, imprimir "Eres un adulto."'''

print("Hola, para continuar ingresa tu nombre y edad")
name = input("Nombre:  ")
age = int(input("Edad: "))

if age <= 13:
    print("Eres un niño/a.")
elif 14 < age <= 17:
    print("Eres un adolescente.")
elif age > 17 :
    print("Eres un adulto.")
else:
    print("Edad no valida!")


'''Ejercicio 2: Calificación de Examen
Pide al usuario la calificación de un examen (un número del 0 al 100). Luego, imprime la letra de la calificación según esta escala:

90-100: "A"
80-89: "B"
70-79: "C"
60-69: "D"
Menos de 60: "F"'''

score = int(input("Ingres la calificacion: "))    

if  score > 100:
    print("Calificacion invalida")
elif 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
elif 0 <= score <= 59:
    print("F")
else:
    print("Calificacion invalida")

'''Ejercicio 3: ¿Número Positivo, Negativo o Cero?
Pide al usuario que ingrese un número. Determina si el número es positivo, negativo o cero e imprime el mensaje correspondiente.'''   

number = int(input("Ingresa un numero: "))
if number > 0:
    print("Numero positivo") 
elif number < 0:
    print ("Numero negativo")
elif number == 0:
    print("El numero es Cero")
else:
    print("Numero invalido")