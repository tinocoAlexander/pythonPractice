tabla = [
[0,0,0],
[1,1,1],
[2,2,2]
]

cubo = tabla, tabla, tabla

for k, tabla in enumerate(cubo):
    for i, fila in enumerate(tabla):
        for j, columna in enumerate(fila):
            print(cubo[k][i][j], end=" ")
        print()
    print()    