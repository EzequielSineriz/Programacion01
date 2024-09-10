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
 
