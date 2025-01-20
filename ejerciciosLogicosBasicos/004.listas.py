"""""
    Como es que funcionan las listas en python:
    Las listas en python suelen ser un recurso que se usa muchas veces, cada elemento dentro de la lista esta indexado y ordenado
"""""

lista = [0] # Ponemos el 0 como primer valor aunque en los ciclos for "i" empieza con un valor de 0
n = int(input("Ingrese la cantidad de veces que se va a multiplicar: \n")) # Aqui declaramos la cantidad de veces que es la que el ciclo se va a ciclar
for i in range(n): # Con in range declaramos el rango que va a tener
    lista.append((i+1)*2) # Con el metodo append, metemos datos a la lista 

print(f"La lista final es {lista}") # Para finalizar imprimimos la lista
print(f"La longitud de la lista es de {len(lista)}") # La longitud de la lista siempre va a ser de n + 1 al nosotros siempre tener un valor 0 predeterminado
print(f"El ultimo item de la lista es {lista[-1]}") # Aqui usamos indices prara poder traer el ultimo item de la lista
