""" Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2
los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice
la operación de dichos valores a través de una función. Mostrar el resultado por
pantalla. """

import Funciones

numero1 = Funciones.pedir_numero_en_rango(10, 100)
numero2 = Funciones.pedir_numero_en_rango(10,100)

operacion = input("Ingrese que operacion desea realizar(s)sumar/(r)restar: ")
while operacion != "s" and operacion != "r":
    operacion = input("Operacion invalida ingrese (s)para sumar, (r)para restar: ")

resultado = Funciones.realizar_operacion(numero1, numero2, operacion)
print("El resultado de su operacion es:", resultado)
