# En python existen las matrices que podemos recorrer de la siguiente manera

tabla = [
[0,0,0],
[1,1,1],
[2,2,2]
]

for i, fila in enumerate(tabla):
    for j, columna in enumerate(tabla):
        print(tabla[i][j], end=" ")
    print("")


"""""
for i, fila in enumerate(tabla):  # Primer ciclo
    print(f"DEBUG: i={i}, fila={fila}")  # Debug para ver la fila actual
    for j, columna in enumerate(fila):  # Segundo ciclo
        print(f"  DEBUG: j={j}, columna={columna}")  # Debug para ver el valor actual
        print(tabla[i][j], end=" ")
    print("")  # Salto de línea después de cada fila
"""""