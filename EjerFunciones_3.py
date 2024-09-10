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