# En python existen cosas que son iteradores

# Estos cumplen la misma funcion que la misma funcion que un for, iterar pues una lista o algo asi

miListaMercado = ["manzanas", "platanos", "aguacates"]
iterarLista = iter(miListaMercado)

print(next(iterarLista))  # "manzanas"
print(next(iterarLista))  # "platanos"
print(next(iterarLista))  # "aguacates"

# 