
# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Suponemos que el número es primo
es_primo = True

# Un número primo es mayor que 1 y no divisible por ningún número excepto 1 y sí mismo
if numero <= 1:
    es_primo = False
else:
    for i in range(2,numero):
        if numero % i == 0:                 
            es_primo = False
            break                           

# Mostrar el resultado
if es_primo:
    print(numero," es un número primo.")
else:
    print(numero, "no es un número primo.")

