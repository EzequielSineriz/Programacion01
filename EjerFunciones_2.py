# Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.

def mostrar()->int: # Va a retornar un entero
    numero = int(input("Ingrese un numero: "))
    return numero
retorno = mostrar () #Asignamos una variable al retorno
print("El numero ingresado es: ", retorno)