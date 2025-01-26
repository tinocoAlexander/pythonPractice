class Main:
    def __init__(self):
        pass
    
    def menu(self):
        print("Bienvenido a mi menú de opciones. Selecciona un número para realizar una acción.")
        opciones = {
            1: self.opcion1,
            2: self.opcion2,
            3: self.salir
        }
        while True:
            try:
                opcion = int(input("1. Detectar si el número es par\n2. Detectar si una palabra es un palíndromo\n3. Salir\n"))
                if opcion in opciones:
                    opciones[opcion]()
                else:
                    print("Opción no válida. Por favor, intenta nuevamente.\n")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número.\n")
    
    def opcion1(self):
        while True:
            try:
                num = int(input("Ingresa un número para verificar si es par: "))
                if num % 2 == 0:
                    print(f"Felicidades, el número {num} es par.")
                else:
                    print(f"El número {num} es impar.")
                break
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero.\n")
    
    def opcion2(self):
        palabra = input("Ingresa la palabra que quisieras verificar si es un palíndromo: ").strip().lower()
        if palabra == palabra[::-1]:
            print(f"La palabra '{palabra}' es un palíndromo.")
        else:
            print(f"La palabra '{palabra}' NO es un palíndromo.")
    
    def salir(self):
        input("Hasta pronto. Presiona Enter para salir...")
        exit()

if __name__ == "__main__":
    app = Main()
    app.menu()
