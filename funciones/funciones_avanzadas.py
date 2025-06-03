
def additionList (): #Definimos la funcion e indicamos los argumentos en caso de que se requiera
    listNumbers = [] #Creamos una lista vacia
    numers = int(input("Cuantos numeros quieres sumar\n ")) #Solicitamos al usuario cuantos numero va a sumar para generar el codigo que genere la lista con numeros
    for i in range (numers): #Generamos un bucle ir agrgando cada numero a la lista
        listNumbers.append (int(input("Ingresa numero: "))) #Mientras el bucle este activo le solicitaremos un numero entero al usuario
    print(f"La suma es: {sum(listNumbers)}") #Cuando termina el bucle ejecutamos otra linea de codigo, en este caso el print para hacer la suma
    
    

def convertionTemp ():
    celsius = float(input("Ingresa Temperatura en celsius: "))
    fahrenheit = celsius * (9/5) + 32
    print(f"{celsius} grados celsius son {fahrenheit} grados fahrenheit")


def menu(choise):
    if choise == 1 :
        additionList()
    elif choise == 2 :
        convertionTemp()
    else:
        print("Seleccion invalida")
    

choiseByUser = int(input("Selecciona una de las dos opciones:\n 1. Sumar Numeros\n 2. Conversion de temperatura celsius a fahrenheit\n "))
menu(choiseByUser)

'''
Nota: desde mi perspectiva de novato he notado que cuando se escriben las funciones al final se escribe lo que en la interaccion
del programa seria lo primero que se observa, en este ejemplo, el menu lo escribi al final para saber que opciones darle
''' 