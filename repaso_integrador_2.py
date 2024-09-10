"""  UTN Technologies, una reconocida software factory se encuentra en la búsqueda
 de ideas para su próximo desarrollo en Python, que promete revolucionar el
 mercado.
 Las posibles aplicaciones son las siguientes:
 ● Inteligencia artificial (IA),
 ● Realidad virtual/aumentada (RV/RA),
 ● Internet de las cosas (IOT)
 Para ello, la empresa realiza entre sus empleados una encuesta, con el
 propósito de conocer ciertas métricas.
 A) Los datos a ingresar por cada empleado encuestado son:
 ● nombre del empleado
 ● edad(no menor a 18)
 ● género (Masculino- Femenino- Otro)
 ● tecnologia (IA, RV/RA, IOT)
 B) Cargar por terminal 10 encuestas.
 C) Determinar:
 1. Cantidad de empleados de género masculino que votaron por IOT o IA,
 cuya edad esté entre 25 y 50 años inclusive.
 2. Porcentaje de empleados que no votaron por IA, siempre y cuando su
 género no sea Femenino o su edad se encuentre entre los 33 y 40.
 3. Nombre y tecnología que votó, de los empleados de género masculino con
 mayor edad de ese género """

masc_iot_ia = 0
cont_punto_b = 0
mayor_edad_c = 17
total_no_ia = 0

for i in range(0,10):
    empleado = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese su edad(18-80): "))
    while edad < 18 or edad > 80:
        edad = int(input("Error, edad invalida.Ingrese su edad(18-80): "))
    genero = input("Ingrese su genero(Masculino- Femenino- Otro): ").lower()
    while genero != "masculino" and genero != "femenino"  and genero != "otro":
        genero = input("Error, genero invalido.Ingrese su genero(Masculino- Femenino- Otro): ").lower()
    tecnologia = input("Ingrese la tecnologia (IA, RV/RA, IOT): ").lower()
    while tecnologia != "ia" and tecnologia != "rv/ra" and tecnologia != "iot":
        tecnologia = input("Error, Ingrese una opcion valida(IA, RV/RA, IOT): ").lower()
    
    if genero == "masculino":
        if tecnologia == "iot" or tecnologia == "ia" and edad >= 25 and edad <= 50:
            masc_iot_ia += 1
        if edad > mayor_edad_c:
            mayor_edad_c = edad
            nombre_mayor_c = empleado
            tecnologia_punto_c = tecnologia

    if tecnologia != "ia":
        total_no_ia += 1
        if genero != "femenino" or (edad >= 33 and edad <= 40):
            cont_punto_b += 1

porcentaje_punto_b = (cont_punto_b / total_no_ia) * 100

print("La cantidad de empleados de genero masculino que votaron por IOT O IA, de edad 33 y 40 es:",masc_iot_ia)
if porcentaje_punto_b > 0 :
    print("Porcentaje de empleados que no votaron por IA, y cumplen con la condición del punto B:", porcentaje_punto_b)
else:
    print("No hubo porcentaje de empleados que no votaron por IA, Y que cumplen con la condicion del punto B")
print("El empleado de género masculino con mayor edad es,",nombre_mayor_c,"que voto por la tecnologia de", tecnologia_punto_c)




