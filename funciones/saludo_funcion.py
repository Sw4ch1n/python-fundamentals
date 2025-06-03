def saludar (name):
    print(f"Hola, {name}")

userName = input("Hola, como te llamas?: ") #Solicitamos el nombre al usuario
saludar(userName) # Llamamos a la funcion y le pasamos el argumento, se indican los argumentos a recibir al momento de definir la funcion
                  # primero se escriben las funciones y despues se llaman pasando los argumentos