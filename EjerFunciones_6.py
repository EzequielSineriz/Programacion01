""" Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor
solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
por pantalla. Atención: pueden reutilizarse funciones ya creadas.
 """
import Funciones

numero1 = Funciones.pedir_numero_en_rango(10, 100)
resultado_con_descuento = Funciones.realizar_descuentos(numero1)

print("El valor con descuento aplicado es: ", resultado_con_descuento)
