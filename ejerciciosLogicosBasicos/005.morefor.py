import math
"""""
    Practiquemos un poco mas con el ciclo for y lo interesante que puede llegar
    a ser cuando lo usamos en el lenguaje de python

    Vamos a implementar un poco de condicionales, haciendo el siguiente problema
    1. Un profesor tiene un grupo de alumnos, quiero saber si sus alumnnos
    han aprobado la material con por lo menos un 6.0 de calificacion
"""""

nombre_alumnos = []
calificaciones_alumnos = []
aprobacion_alumnos = []

while True:
    try: #Try para verificar que el numero es entero
        numero_alumnos = int(input("Ingrese la cantidad de alumnnos de los que va a obtener su calificacion \n"))
        if numero_alumnos>0: # Validamos que el numeor sea mayor a 0
            break
        else:
            print("Por favor ingrese un numero mayor a 0")
    except ValueError:    
        #if math.isnan(numero_alumnos):
        print("Incorrecto, ingrese un numero valido") # por si el usuario ingresa un numero no valido

for i in range(numero_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i+1} \n") # Agregamos los nombres de los alumnos a una lista
    nombre_alumnos.append(nombre)
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificacion del alumno {i+1} \n"))
            if 0 <= calificacion <= 10: # Verificacion de calificacion
                calificaciones_alumnos.append(calificacion)
                if(calificacion>=6):
                    aprobacion_alumnos.append("Si")
                    break
                else:
                    aprobacion_alumnos.append("No")
                    break
            else:
                print("Error, la contraseña tiene que ser de un numero entre 0 y 10")
        except ValueError:
            print("Error, ingrese un numero valido") # Excepcion de tipo de valor

print(f"El nombre de los alumnos: {nombre_alumnos}")
print(f"Calificaciones {calificaciones_alumnos}")
print(f"Quienes aprobaron {aprobacion_alumnos}")