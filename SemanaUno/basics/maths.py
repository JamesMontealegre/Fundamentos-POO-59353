# Este es nuestro primer programa en Python

# 1. Imprimir un mensaje en la consola
print("¡Hola, bienvenidos a su primera clase de programación en Python!")

# 2. Operaciones matemáticas básicas
print("Ahora vamos a hacer algunas operaciones matemáticas básicas:")
print("Suma: 5 + 3 =", 5 + 3)
print("Resta: 10 - 4 =", 10 - 4)
print("Multiplicación: 6 * 7 =", 6 * 7)
print("División: 20 / 4 =", 20 / 4)
print("Potencia: 2 ** 3 =", 2 ** 3) # 2 elevado a la potencia de 3
print("División entera: 17 // 3 =", 17 // 3) # División entera (sin decimales)
print("Módulo: 17 % 3 =", 17 % 3) # Módulo (resto de la división)

# 3. Variables: guardamos datos en una variable
nombre = "Estudiante"
edad = 18
print("Hola,", nombre, "tienes", edad, "años.")

# 4. Pedir información al usuario (Entrada de datos)
print("\nAhora vamos a interactuar con el usuario.")
nombre_usuario = input("¿Cuál es tu nombre? ")
print("¡Hola, " + nombre_usuario + "!")

# 5. Procesar la información proporcionada
numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))

# 6. Realizar varias operaciones con los datos ingresados
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
potencia = numero1 ** numero2
division_entera = numero1 // numero2
modulo = numero1 % numero2

# 7. Mostrar el resultado en pantalla (Salida de datos)
print("\nResultados de las operaciones:")
print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(f"La división de {numero1} entre {numero2} es: {division}")
print(f"{numero1} elevado a la potencia de {numero2} es: {potencia}")
print(f"La división entera de {numero1} entre {numero2} es: {division_entera}")
print(f"El módulo de {numero1} entre {numero2} es: {modulo}")
