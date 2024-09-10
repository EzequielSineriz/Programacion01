def pedir_numero_en_rango(desde, hasta):
    numero = int(input("Ingrese un número entre " + str(desde) + " y " + str(hasta) + ": "))
    while numero < desde or numero > hasta:
        print("El número ingresado no está en el rango " + str(desde) + "-" + str(hasta) + ".")
        numero = int(input("Ingrese un número entre " + str(desde) + " y " + str(hasta) + ": "))
    return numero

# Llamada a la función de prueba
numero_en_rango = pedir_numero_en_rango(1, 10)
print("El número ingresado dentro del rango es: " + str(numero_en_rango))
