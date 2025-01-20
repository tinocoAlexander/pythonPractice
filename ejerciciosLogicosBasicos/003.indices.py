# Para poder obtener la posicion de un str, se usa []
texto="Soy una cadena de ejemplo"
print(texto[2]) #Podemos ver que la primera posicion es la 0
print("-------------------")
# Metodo len
longitud = len(texto)
print(longitud)
print("-------------------")
# Obtener una cadena al reves
cadena = "Hola, soy una cadena"
cadena_al_reves= cadena[::-1]
print(cadena_al_reves)
print("-------------------")
# Pedimos que el usuario ingrese la cadena
nombre = input("Ingrese su nombre de pila, ex. Alexander \n")
print(f"Su nombre al reves es: {nombre[::-1]}")
