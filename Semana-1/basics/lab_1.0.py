def get_minor_and_average(a, b, c):
    minor = 0
    average = 0

    if a < b and a < c:
        minor = a
    elif b < a and b < c:
        minor = b
    else:
        minor = c

    average = a + b + c/3

    print(f"El promedio de los numeros: {a}, {b}, {c} es: \npromedio: {average} \n y el menor de los tres numeros es:\nMenor: {minor}")


get_minor_and_average(8, 24, 1)
    


        
