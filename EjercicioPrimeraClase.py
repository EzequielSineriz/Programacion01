""" Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su sueldo para esa persona.
Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), adolescente (entre 13 y 17 años) o niño (menor a 13 años).
Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.
Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil distinto a "Soltero", mostrar el siguiente mensaje:
 'Es muy pequeño para NO ser soltero.'
Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 por cada estadía como base,
 se pide el ingreso de una estación del año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del Plata/Córdoba) 
 para vacacionar para poder calcular el precio final: -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un 
 descuento del 10% Mar del Plata tiene un descuento del 20% -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene 
 un aumento del 10% Mar del Plata tiene un aumento del 20% -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene
un aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el precio sin descuento.
Validar el ingreso de datos. """


""" Ezequiel Siñeriz
Div 213
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su sueldo para esa persona. """
""" 
nombre = input("Ingrese su nombre: ")
sueldo = float(input("Ingrese su sueldo: "))
incremento = 10
cuenta_sueldo = sueldo+(sueldo*10)/100
# print("su sueldo con aumento es: ", cuenta_sueldo)
print("su sueld actual es:" + str(cuenta_sueldo)) # tengo que castear el float que me vuelve de cuenta sueldo porque concatenamos str con float
 """
""" Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), adolescente (entre 13 y 17 años) o niño (menor a 13 años).
 """

""" edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("Ud es mayor de edad.")
elif edad >= 13:
    print("Usted es adolescente.")
elif edad > 0:
    print("Usted es niño")
else:
    print("Edad incorrecta. No Existe edad negativa") """


""" Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos. """

""" 
cantidad_pares = 0
cantidad_impares = 0
par_mayor = 0
suma_positivos = 0
producto_negativo = 1
menor_numero = 0
es_primer_par = True


for i in range(0,5):

    numero = int(input("Ingrese un numero(1-max): "))
    while numero < 0:
        numero = int(input("Error.Ingrese un numero (1-max)"))
    
    if numero % 2 == 0:
        cantidad_pares += 1
        if es_primer_par = True or numero > mayor_numero_par:
            mayor_numero_par = numero
            es_primer_par = false

    else:
        cantidad_impares += 1
    
    
    if menor_numero > numero:
        menor_numero = numero

    if numero > 0:
        suma_positivos += numero
    else:
        producto_negativo *= numero




print("La cantidad de pares es: ", cantidad_pares,"La cantidad de impares es: ", cantidad_impares)
print("El menor numero ingresado fue: ", menor_numero)
print ("El par mayor es: ", par_mayor)
print("La suma de los positivos es: ",suma_positivos)
print("El producto de los negativos es: ",producto_negativo)

 """


""" Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil distinto a "Soltero", mostrar el siguiente mensaje:
Es muy pequeño para NO ser soltero.
 """

""" edad = int(input("Ingrese su edad(0-120): "))
estado_civil = input("Ingrese su estado civil(soltero/casado/viudo): ")
while estado_civil != "soltero" and estado_civil != "casado" and estado_civil != "viudo":
    print("Error el dato ingresado es incorrecto.Vuelva a ingresar")
    estado_civil = input("Ingrese su estado civil(soltero/casado/viudo): ")
if estado_civil != "soltero" and edad < 18:
    print("Es muy pequeño para NO ser soltero")
 """

""" Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000 por cada estadía como base,
 se pide el ingreso de una estación del año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del Plata/Córdoba) 
 para vacacionar para poder calcular el precio final: -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un 
 descuento del 10% Mar del Plata tiene un descuento del 20% -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene 
 un aumento del 10% Mar del Plata tiene un aumento del 20% -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene
un aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el precio sin descuento.
 """

estadia = 15000
corte_control = "si"
while corte_control == "si":
    estacion = input("Ingrese en la estacion que desea viajar(invierno/verano/otoño/primavera): ")
    while estacion != "invierno" and estacion != "verano" and estacion != "otoño" and estacion != "primavera":
        estacion = input("Error.Ingrese en la estacion que desea viajar(invierno/verano/otoño/primavera): ")
    localidad = input("Ingrese la localidad a viajar(bariloche/cataratas/mar del plata/cordoba): ")
    while localidad != "bariloche" and localidad != "cataratas" and localidad != "mar del plata" and localidad != "cordoba":
        localidad = input("Error.Ingrese la localidad a viajar(bariloche/cataratas/mar del plata/cordoba): ")
    aumento = 0
    descuento = 0

    if estacion == "invierno":
        if localidad == "bariloche":
            aumento = 20
        if localidad == "cataratas" or localidad == "cordoba":
            descuento = 10
        else:
            descuento = 20
    elif estacion == "verano":
        if localidad == "bariloche":
            descuento = 20
        if localidad == "cataratas" or localidad == "cordoba":
            aumento = 10
        else:
            aumento = 20
    elif estacion == "otoño" or estacion == "primavera":
        if localidad == "bariloche" or localidad == "cataratas" or localidad == "mar del plata":
            aumento = 10

    precio_final = estadia + (estadia * aumento / 100) - (estadia * descuento / 100)

    print("El precio final de la estadía en",localidad, "durante",estacion," es: $", precio_final)

    corte_control = input("Desea calcular otra tarifa (si/no): ")
    while corte_control != "si" and corte_control != "no":
        corte_control = input("Error. Desea calcular otra tarifa (si/no): ")






    
