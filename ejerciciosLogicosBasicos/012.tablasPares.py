matriz = [
    [8,7,0],
    [34,2,-1],
    [5,-5,12]
]

# El objetivo es sustituir los numeros pares por 0 y los impares por 1
for i, fila in enumerate(matriz):
    for j, columna in enumerate(fila):
        if matriz[i][j]%2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print("")