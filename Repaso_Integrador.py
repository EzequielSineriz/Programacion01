""" Enunciado/s:
 Tabla de Posiciones de Torneo de Ping-Pong
 Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
 Los datos que se cargarán son:
 Nombre del jugador
 Edad (validar)
 Cantidad de puntos (validar-número entero positivo, hasta 60).
 Número de partidos ganados (validar-número entero positivo, hasta 35).
 Tipo de saque ("plano", "liftado", "cortado")
 Categoría ("elite", "experto", "avanzado")
 Se necesita saber
 TemaA:
 1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
 inclusive.
 2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
 3-Porcentaje de jugadores de categoría "experto".
 4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
 5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite” """

corte_control = "si"
min_edad = 101
cont_jugadores = 0
cont_punto_a = 0
cont_experto = 0
acum_edad_c = 0
cont_punto_c = 0
cont_punto_plano = 0
cont_punto_listado = 0
cont_punto_cortado = 0

while corte_control == "si":
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad (18-100): "))
    while edad < 18 and edad > 100:
        edad = int(input("Error.Ingrese su edad (18-100): "))
    cant_puntos = int(input("Ingrese la cantidad de puntos(0-60): "))
    while cant_puntos < 0 or cant_puntos > 60:
        cant_puntos = int(input("Error. Ingrese la cantidad de puntos(0-60): "))
    partidos_ganados = int(input("Ingrese los partidos ganados(0-35): "))
    while partidos_ganados < 0 and partidos_ganados > 35:
        partidos_ganados = int(input("Error.Ingrese los partidos ganados(0-35): "))
    tipo_saque = input("Ingrese el tipo de saque(plano/liftado/cortado): ")
    while tipo_saque != "plano" and tipo_saque != "listado" and tipo_saque != "cortado":
        tipo_saque = input("ERROR.Ingrese el tipo de saque(plano/liftado/cortado): ")
    categoria = input("Ingrese su categoria(elite/experto/avanzado): ")
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":
        categoria = input("Error.Ingrese su categoria(elite/experto/avanzado): ")
    
    
    cont_jugadores += 1

    if categoria == "elite":
        if tipo_saque == "plano":
            cont_punto_plano += 1
            if edad >= 19 and edad <= 25:
                cont_punto_a += 1
        elif tipo_saque == "cortado":
            cont_punto_cortado += 1
        elif tipo_saque == "listado":
            cont_punto_listado += 1    
    elif categoria == "experto":
        cont_experto += 1
    elif categoria == "avanzado":
        acum_edad_c += edad
        cont_punto_c += 1
    

    if cant_puntos > 50 and edad < min_edad:
        edad = min_edad
        nombre_punto_b = nombre
        categoria_punto_b = categoria
    
porcentaje_experto = cont_experto *100 /cont_jugadores

if cont_punto_plano > cont_punto_cortado and cont_punto_plano > cont_punto_listado:
    contador_mas_grande = "plano"
elif cont_punto_cortado > cont_punto_listado:
    contador_mas_grande = "cortado"
else:
    contador_mas_grande = "listado"

print("La cantidad de jugadores elite con tipo de saque plano,de edad entre 19 y 25 es:", cont_punto_a)
print("El jugador con menor edad con mas de 50 punto es:",nombre_punto_b,"de categoria:", categoria_punto_b)
if porcentaje_experto > 0:
    print("El porcentaje de jugadores de categorias experto es:", porcentaje_experto,"%")
else:
    print("El porcentaje de jugadores de categoria experto es: 0 % ")
print("El Promedio de edad de categoria avanzada es de", acum_edad_c/cont_punto_c)
print("El tipo de saque mas utilizado por la categoria elite es:",contador_mas_grande)






    




