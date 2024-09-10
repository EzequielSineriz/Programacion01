"""  1. Mostrar los números ascendentes desde el 1 al 10
 """

""" for i in range (1,11):
    print(i)
 """
""" 2. Mostrar los numeros decendientes del 10 al 0 """

""" for i in range(10, 0, -1):
    print(i) """

""" 3-Ingresar un número. Mostrar los números desde 0 hasta el número
ingresado.
 """
""" i = int(input("Ingrese un mumero: "))
for i in range(1,i+1):
    print(i) """

""" Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
ejemplo si se ingresa el numero 5: """
""" 
numero = int(input("Ingrese el numero que desea realizar la tabla: "))

for i in range (1,11):
    resultado = numero * i
    print(numero, "x", i,"=",resultado) """

""" 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
número 0. Mostrar la suma y el promedio de todos los números """
""" 
suma = 0
contador = 0

for i in range(10):
    numero = int(input("Ingrese un número (0 para terminar): "))
    
    if numero == 0: #al ingresar 0 sale del for con la funcion del break
        break
    
    suma += numero
    contador += 1


if contador > 0:
    promedio = suma / contador
else:
    promedio = 0

print("La suma de los numeros es", suma, "y el promedio es:", promedio) """

""" 6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*) """
""" 
for i in range(1, 11):
    if i % 3 == 0: #Esta condición verifica si i es divisible por 3 sin dejar residuo, lo que significa que es un múltiplo de 3.
        print(i) """

"""  7.Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
 """

""" for i in range (1,51):
    if i % 2 == 0:  # Verificar si el número es par
        print(i) """

""" 8. Realizar un programa que permita mostrar una pirámide de números. Por
ejemplo: si se ingresa el numero 5, la salida del programa será la
siguiente: """


""" # Definir la altura de la pirámide
altura = 10

# Bucle externo para las filas
for i in range(1, altura + 1):
    # Bucle interno para imprimir los números en cada fila
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  """

""" 9.Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
el número ingresado. Mostrar la cantidad de divisores encontrados. """

""" # Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
contador_divisores = 0
# Bucle para encontrar y mostrar los divisores
print(f"Los divisores de {numero} son:")
for i in range(1, numero + 1):
    if numero % i == 0:  # Verificar si 'i' es un divisor de 'numero'
        print(i)
        contador_divisores += 1

# Mostrar la cantidad de divisores encontrados
print(f"Cantidad de divisores encontrados: {contador_divisores}")
"""
""" 10.Ingresar un número. Determinar si el número es primo o no. """

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Suponemos que el número es primo
es_primo = True

# Un número primo es mayor que 1 y no divisible por ningún número excepto 1 y sí mismo
if numero <= 1:
    es_primo = False
else:
    for i in range(2,numero + 1):#Se recorre desde 2 hasta la raíz cuadrada del número para verificar si 
        if numero % i == 0:                 #tiene divisores. Si se encuentra un divisor, el número no es primo.
            es_primo = False
            break                           

# Mostrar el resultado
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")


