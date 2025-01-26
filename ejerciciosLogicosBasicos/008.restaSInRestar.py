# En el siguiente ejercicio se busca restar dos numeros sin restar

numeroUno = 5
numeroDos = 20

# Como hago para poder restar estos dos numeros sin hacer una resta
resta = 0
if numeroUno>numeroDos:
    while numeroUno != numeroDos:
        numeroUno -= 1  # Se simula la resta disminuyendo manualmente
        resta += 1      # Contamos cuántas veces hemos restado 1
else:
    while numeroDos != numeroUno:
        numeroDos -= 1
        resta +=1

#En este caso estamos haciendo una resta siempre se le resta al numero mayor

print("La resta es igual a: ", resta)