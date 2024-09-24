#-----------------
#Person

#dni: int
#name: str
#lastname: int
#role: int


#-----------------

from faker import Faker
import random

# Inicializa Faker
fake = Faker()
people_list = []

def generate_people(num_people: int):
    for i in range(num_people):
        person = {
            'dni': i + 1,
            'name': fake.first_name(),
            'lastname': fake.last_name(),
            'role': random.randint(1, 3)
        }
        people_list.append(person)
    return people_list


def add_people():
    quantity = int(input('Por favor digite la cantidad de usuarios que desea agregar:\n'))
    generate_people(quantity)
    match_role()
    get_people()


def get_people():
    for person in people_list:
        print(person)


def select_role():
    for person in people_list:
        if(person["role"] == 1):
            person["role"] = "Estudiantes"
        elif(person["role"] == 2):
            person["role"] = "Profesor"
        else:
            person["role"] = "Administrativo"


def match_role():
    for persona in people_list:
        match persona["role"]:
            case 1:
                persona["role"] = "Estudiantes"
            case 2:
                persona["role"] = "Profesor"
            case 3:
                persona["role"] = "Administrativo"
    
    
def main():
    while True:
        add_people()
        response = input("¿Desea continuar agregando usuarios al sistema? s/n\n")
        if(response != "s"):
            break



main()


