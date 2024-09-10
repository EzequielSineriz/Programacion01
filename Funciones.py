def pedir_numero_en_rango(desde, hasta):
    numero = int(input("Ingrese un número entre " + str(desde) + " y " + str(hasta) + ": "))
    while numero < desde or numero > hasta:
        print("El número ingresado no está en el rango " + str(desde) + "-" + str(hasta) + ".")
        numero = int(input("Ingrese un número entre " + str(desde) + " y " + str(hasta) + ": "))
    return numero

def realizar_descuentos(parametro1:int)-> int:
    descuento = parametro1 * 0.95
    return descuento

def realizar_operacion(numero1, numero2, operacion)->int:
    if operacion == 's':
        return numero1 + numero2
    elif operacion == 'r':
        return numero1 - numero2