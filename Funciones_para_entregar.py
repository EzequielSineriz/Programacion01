""" Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe
como parámetro """


def mostrar(numero:int):
    print ("El numero que ingreseo fue:", numero)
numero = int (input("Ingrese un numero: "))
mostrar(numero)

###########################################################################

# Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne.

def mostrar()->int: # Va a retornar un entero
    numero = int(input("Ingrese un numero: "))
    return numero
retorno = mostrar () #Asignamos una variable al retorno
print("El numero ingresado es: ", retorno)


#############################################################################
""" Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La
función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
programa principal realizando la invocación o llamada.
 """
def es_par(numero:int)->bool:
    """Toma el numero y define con True si es par, False si es impar"""
    if numero % 2 == 0:
        retorno = True
    else:
        retorno = False
    return retorno

# Programa principal
numero = int(input("Ingresa un número: "))
if es_par(numero):
    print ("Es Par")
else:
    print("El número es impar.")


#################################################################################
""" Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en
un rango determinado pasado por parámetro “desde”-“hasta” """
def pedir_numero_en_rango(desde, hasta):
    numero = int(input("Ingrese un número entre " + str(desde) + " y " + str(hasta) + ": "))
    while numero < desde or numero > hasta:
        print("El número ingresado no está en el rango " + str(desde) + "-" + str(hasta) + ".")
        numero = int(input("Ingrese un número entre " + str(desde) + " y " + str(hasta) + ": "))
    return numero

# Llamada a la función de prueba
numero_en_rango = pedir_numero_en_rango(1, 10)
print("El número ingresado dentro del rango es: " + str(numero_en_rango))

#################################################################################


""" Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la
función Restar en sus 4 combinaciones.
 Restar1(int, int)->int:
 Restar2()->int:
 Restar3(int, int):
 Restar4(): """

def Restar1(num1=int, num2=int)->int:
    resta = num1 - num2
    return resta

def Restar2()->int:
    num1 = int(input("Ingrese el Primer Numero: "))
    num2 = int(input("Ingresa el Segundo Numero: "))
    resta = num1 - num2
    return resta

def Restar3(num1:int, num2:int):
    resta = num1 - num2
    print("El resultado de Restar3",str(num1),"- ",str(num2)," es: ", str(resta))

def Restar4():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print("El resultado de Restar4() es:",resultado)

#print("Usando Restar1(10, 5):", Restar1(10, 5))
    
#print("Usando Restar2():")
#resultado2 = Restar2()
#print("Resultado de Restar2() es:", resultado2)
    
#print("Usando Restar3(50, 25):")
#Restar3(50, 25)
    
#print("Usando Restar4():") 
#Restar4() 

##########################################################################################

""" Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor
solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
por pantalla. Atención: pueden reutilizarse funciones ya creadas.
 """
import Funciones

numero1 = Funciones.pedir_numero_en_rango(10, 100)
resultado_con_descuento = Funciones.realizar_descuentos(numero1)

print("El valor con descuento aplicado es: ", resultado_con_descuento)

###############################################################################################

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


