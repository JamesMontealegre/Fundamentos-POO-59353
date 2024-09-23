# ==========================================================
# SECCIÓN 1: Variables y Tipos de Datos
# ==========================================================

# Declaración de variables con diferentes tipos de datos
entero = 10             # Tipo de dato entero (int)
flotante = 3.14         # Tipo de dato flotante (float)
cadena = "Hola, Python" # Tipo de dato cadena de texto (str)
booleano = True         # Tipo de dato booleano (bool)

# Imprimir las variables y sus tipos de datos
print(f"El número entero es: {entero}, Tipo: {type(entero)}")
print(f"El número flotante es: {flotante}, Tipo: {type(flotante)}")
print(f"La cadena es: '{cadena}', Tipo: {type(cadena)}")
print(f"El valor booleano es: {booleano}, Tipo: {type(booleano)}")

# ==========================================================
# SECCIÓN 2: Estructura if, elif, else
# ==========================================================

# Evaluación de condiciones utilizando if, elif y else
if entero > 5:
    print("El número entero es mayor que 5.")  # Se cumple esta condición
elif entero == 5:
    print("El número entero es igual a 5.")
else:
    print("El número entero es menor que 5.")

# Otra estructura con elif
if flotante < 2.0:
    print("El número flotante es menor que 2.0.")
elif 2.0 <= flotante <= 5.0:
    print("El número flotante está entre 2.0 y 5.0.")  # Se cumple esta condición
else:
    print("El número flotante es mayor que 5.0.")

# ==========================================================
# SECCIÓN 3: Operadores Booleanos y Comparación
# ==========================================================

x = 5
y = 10

# Operadores booleanos y de comparación
# AND: ambas condiciones deben ser verdaderas
if x > 3 and y < 15:
    print("AND: Ambas condiciones son verdaderas.")

# OR: al menos una de las condiciones debe ser verdadera
if x < 3 or y > 8:
    print("OR: Al menos una condición es verdadera.")

# NOT: invierte el valor booleano
if not (x < 3):
    print("NOT: Es cierto que x no es menor que 3.")

# Comparadores adicionales:
if x == 5:
    print("==: x es igual a 5.")
if x != 10:
    print("!=: x es diferente de 10.")
if y >= 10:
    print(">=: y es mayor o igual que 10.")
if x <= 5:
    print("<=: x es menor o igual que 5.")

# ==========================================================
# SECCIÓN 4: Impresión y Lectura por Consola (Template String)
# ==========================================================

nombre = input("Ingresa su nombre: ")
edad = input("Ingresa su edad: ")

# Imprimir una cadena utilizando f-strings (template strings)
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # f-string

# Ejemplo de entrada de usuario con input() y formateo de salida
# Descomentar las líneas a continuación para probar en consola
# numero_ingresado = int(input("Ingresa un número entero: "))
# print(f"El número que ingresaste es {numero_ingresado} y es del tipo {type(numero_ingresado)}")
