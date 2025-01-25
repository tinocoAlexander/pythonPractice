"""""
    En el siguiente ejercicio vamos a verificar si una palabra es palindromo o no
    Una palabra se considera palindromo si es que esta se lee igual al derecho y al revés
    Un ejemplo de esto es la palabra RECONOCER
    Este ejercicio nos ayudara a mejorar un poco más la lógica de la porgramación
"""""

while True:
    palabra = input("Ingrese su palabra para poder saber si esta es un palindromo o no \n").lower()
    if palabra.isalpha():
        palabra_reves = palabra[::-1]
        if palabra_reves == palabra:
            print(f"La palabra {palabra} es un palindromo")
        else:
            print(f"La palabra {palabra} no es un palindromo")
        break
    else:
        print("Error, la palabra tiene que ser solo letras")
        input("Teclee espacio para volver a intentar")
        