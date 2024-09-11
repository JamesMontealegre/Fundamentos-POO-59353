# Este es un programa para mostrar los diferentes tipos de datos en Python

# 1. Enteros (int)
entero = 10
print("Este es un número entero:", entero)
print("Tipo de dato de 'entero':", type(entero))

# 2. Flotantes (float)
flotante = 3.14
print("\nEste es un número flotante:", flotante)
print("Tipo de dato de 'flotante':", type(flotante))

# 3. Cadenas de texto (str)
cadena = "¡Hola, Python!"
print("\nEsta es una cadena de texto:", cadena)
print("Tipo de dato de 'cadena':", type(cadena))

# 4. Booleanos (bool)
verdadero = True
falso = False
print("\nEste es un valor booleano (verdadero):", verdadero)
print("Este es un valor booleano (falso):", falso)
print("Tipo de dato de 'verdadero':", type(verdadero))
print("Tipo de dato de 'falso':", type(falso))

# 5. Listas (list)
lista = [1, 2, 3, "cuatro", 5.0, True]
print("\nEsta es una lista que contiene diferentes tipos de datos:", lista)
print("Tipo de dato de 'lista':", type(lista))

# 6. Interacción con el usuario
print("\nAhora vamos a interactuar con el usuario para ver más tipos de datos.")
numero_entero = int(input("Ingresa un número entero: "))
numero_flotante = float(input("Ingresa un número flotante: "))
cadena_usuario = input("Ingresa una cadena de texto: ")

# 7. Mostrar los tipos de datos ingresados por el usuario
print("\nMostrando los datos ingresados:")
print(f"El número entero que ingresaste es {numero_entero} y su tipo de dato es:", type(numero_entero))
print(f"El número flotante que ingresaste es {numero_flotante} y su tipo de dato es:", type(numero_flotante))
print(f"La cadena que ingresaste es '{cadena_usuario}' y su tipo de dato es:", type(cadena_usuario))
