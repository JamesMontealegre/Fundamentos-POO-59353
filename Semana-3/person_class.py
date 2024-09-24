
# Los métodos __init__ y __repr__ en Python son métodos especiales llamados métodos mágicos 
# o dunder methods (por tener dobles guiones bajos en sus nombres). Son métodos que el lenguaje 
# Python invoca automáticamente en ciertas circunstancias sin que el programador tenga que llamarlos 
# explícitamente.

# __init__: El constructor de la clase
# El método __init__ es el constructor de la clase, y se llama automáticamente cuando se crea una 
# instancia de la clase. No necesitas invocarlo directamente porque Python lo llama por ti cuando 
# creas un nuevo objeto.

# __repr__: La representación del objeto
# El método __repr__ se utiliza para obtener una representación string del objeto. Este método se 
# llama automáticamente cuando:

# Imprimes el objeto.
# Llamas a repr() sobre el objeto.
# El objeto es mostrado en un entorno interactivo (como el intérprete de Python).


class Person:
    def __init__(self, dni: int, name: str, lastname: str, role: int):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.role = role

    def __repr__(self):
        return f"Person(dni={self.dni}, name={self.name}, lastname={self.lastname}, role={self.role})"
    
    # def __repr__(self):
    #     return "Person(dni={}, name={}, lastname={}, role={})".format(self.dni, self.name, self.lastname, self.role)



people = [
    Person(dni=12345678, name='John', lastname='Doe', role=1),  # Estudiante
    Person(dni=23456789, name='Jane', lastname='Smith', role=2),  # Profesor
    Person(dni=34567890, name='Alice', lastname='Johnson', role=3),  # Administrativo
    Person(dni=45678901, name='Bob', lastname='Williams', role=1)  # Estudiante
]


for person in people:
    print(person)
