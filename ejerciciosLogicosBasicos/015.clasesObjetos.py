# Las clases y los objetos son parte fundamental en nuestro dia a dia como programadores para poder reutilizar codigo de mejor manera

# Vamos a hacer un ejemplo de un zoologico

class Animal:
    def __init__(self,nombre,edad,dieta,genero):
        self.nombre = nombre
        self.edad = edad
        self.dieta = dieta
        self.genero = genero

    def __str__(self): # Con el metodo str podemos hacer que la instancia se pueda leer directamente los datos que le estamos pasando
        return f"Este es un {self.nombre}"

    def comer(self): # Diferentes metodos que un animal tendria, aqui hacemos el molde
        print(f"El animal {self.nombre}, con edad {self.edad} esta comiendo")

    def beber(self):
        print(f"El animal {self.nombre}, con edad {self.edad} esta bebiendo")



animalUno = Animal("Leopardo", 10, "Carnivoro", "Masculino") # Aqui yo estoy haciendo una instancia de mi clase Animal y le estoy pasando los datos
print(animalUno)