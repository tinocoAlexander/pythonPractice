# Uno de los principios de la POO es la recursividad

# La recursividad es cuando una funcion se llama a si misma una cantidad n de veces

# La siguiente funcion sera una cuenta atras hasta que sea igual a 0

class Recursividad:
    @staticmethod
    def cuenta_atras(num):
        if num > 0:
            print(num)
            num = num - 1
            Recursividad.cuenta_atras(num)
        else:
            print(num)

# Instancia de la clase
instancia = Recursividad()

print("Bienvenido a mi sistema de cuenta atrás")
while True:
    try:
        n = int(input("Ingrese un número entero \n"))
        instancia.cuenta_atras(n)  # Llamada al método estático
        break
    except ValueError:
        print("Error, debe ser un número válido")

