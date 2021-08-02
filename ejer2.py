print ("Sistema de registros deportivos")

genero = input ("Ingresá tu genero: H> hombre / M > mujer ").lower

controlgenero = genero == "h"
print("Genero hombre"), controlgenero

edad =int(input("Ingresá tu edad: >> "))
controledad = edad >=18
print("mayor de edad"), controledad

altura =float(input("ingrese su altura"))

controlaltura = altura >=1.8
print("alto"), controlaltura

print("Asignación de deporte")

hockey= controlgenero == True
print("puede jugar al hockey: ", hockey)

volley = controlgenero == True or controlgenero == False and controlaltura == True
print("puede jugar al volley: ", volley)

rugby= controledad == True and controledad <=55
print("puede jugar al rugby: ", rugby)

print("Gracias por usar nuestro sistema")
exit()

'''
Realizar un programa en Python que:
1. Le de un mensaje al usuario que indique "Sistema de registros deportivos")
2. Le pida al usuario que indique su género.
3. Si es masculino, que imprima un mensaje: "Hombre: Verdadero", caso contrario que indique falso.
4. Que le pida que ingrese su edad.
5. Si es mayor de edad, que indique un mensaje: "Mayor: Verdadero", caso contrario que indique falso.
6. Le pida la altura (admitiendo decimales)
7. Si la altura ingresada es mayor de 1,8, que indique: "Alto: Verdadero", caso contrario falso.
8. Que imprima un mensaje que diga "Asignación de deporte".
9. Que le diga Puede jugar Hochey: Verdadero, solo si es varón, caso contrario que indique falso.
10. Que indique: "Puede jugar Volley: Verdadero" solo si es hombre o si es mujer alta. Caso contrario falso.
11. Que le informe "Puede jugar Rugby: Verdadero si es mayor de 18 y menor de 55 años.
12. Que al finalizar le de un mensaje de despedida y cierre la ejecución del programa.
'''
