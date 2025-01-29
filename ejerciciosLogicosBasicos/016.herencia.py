class Animal:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def __str__(self):
        return f"Este es un {self.nombre} y tiene la edad de {self.edad} años"

    def comer(self):
        print("El animal está comiendo")

class Burro(Animal):
    def __init__(self, nombre, edad, genero, color):
        super().__init__(nombre, edad, genero)
        self.color = color

    def __str__(self):
        return super().__str__() + f" y su color es {self.color}"

    def comer(self):
        print(super().comer() + f"y su color es {self.color}")

animal1 = Animal("animalito",10,"Masculino")
print(animal1)

burro1 = Burro("Burrito", 2, "Femenino", "Cafe")
print(burro1)