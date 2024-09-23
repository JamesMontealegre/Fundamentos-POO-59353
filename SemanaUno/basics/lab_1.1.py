def get_minor_and_average() :
    number1 = input("Ingrese el primer número: ")
    number2 = input("Ingrese el segundo número: ")

    print(number1 + number2)
 
#get_minor_and_average()


def get_minor_and_average_v2():

    average = None
    largest = None

    number1 = int(input("Ingrese el primer número: "))
    number2 = int(input("Ingrese el segundo número: "))
    number3 = int(input("Ingrese el tercer número: "))

    largest = max(number1, number2, number3)

    average = (number1 + number2 + number3) / 3

    print(f"El promedio para los numeros ingresados {number1}, {number2}, {number3} es: \nPromedio: {average}\nY el número mayor es: {largest} ")

get_minor_and_average_v2()

    
