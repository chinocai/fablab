print ("bienvenidos a Automotores Carlitos")

nombre=input ("Ingresá tu nombre: ")

monto=int(input("Por favor " + nombre + " ingrese el monto disponible para la compra."))

if (monto < 1000000):
    print ("no se poseen autos de ese rango de precios, debera reingresar el monto nuevamente.")
    monto=int(input("reingrese el monto."))

if (monto < 1000000):
    print ("no se poseen autos de ese rango de precios, hasta la otra")
    exit()

marca=input ("Ingrese la marca del auto que está buscando: ")

if (marca != "Ford" and marca != "Chevrolet" and marca != "Fiat"):
    print ("son las únicas marcas disponibles, reingresar la marca")

    marca=input("reingrese la marca.")

if (marca != "Ford" and marca != "Chevrolet" and marca != "Fiat"):
    print ("son las únicas marcas disponibles, hasta la otra")
    exit()

puerta=int(input("Ingrese la cantidad de puertas que desea: "))

if (puerta <3 or puerta >5):
    print ("cantidad no disponible, reingresar la cantidad de puertas ")

    puerta=int(input("reingrese la cantidad de puertas "))

if (puerta <3 or puerta >5):
    print ("son las únicas puertas disponibles, hasta la otra")
    exit()    

if marca == "Ford" and monto >= 1500000:
    print("puede comprar el modelo Ka.")

elif marca == "Fiat" and (puerta==3 or puerta==5):
    print("tiene el modelo Punto.")

elif marca == "Chevrolet" and puerta==5 and monto>2000000:
    print("puede acceder al modelo zafira.")

else:
    print("no se poseen autos con esas características")

print ("Gracias vuelvas prontos")
exit()

'''
Realizar un programa en Python que:
1. Le imprima un mensaje de bienvenida que diga "Automotores Carlitos "
2. Le pida al usuario su nombre.
3. Le pida al usuario, concatenando su nombre, el monto disponible para la compra.
4. Si el monto es menor a $1000000, indicarle que no se poseen autos de ese rango de precios y pedirle que reingrese el monto.
5. Si al reingresarlo sigue colocando un monto menor, darle un mensaje de despedida y cerrar la ejecución del programa.
6. Si ingreso un monto correcto, pedirle que ingrese la marca del auto que está buscando.
7. Si no ingresa "Ford, Chevrolet o Fiat", indicarle que esos son las únicas marcas disponibles y pedirle que reingrese la marca. Cerrar la ejecución si no lo hace.
8. Por último, pedirle que ingrese la cantidad de puertas que desea. Si el usuario no coloca un valor entre 3 y 5, decirle que no existen autos con esa cantidad de puertas. Permitirle reingresar el dato y si lo hace incorrectamente, cerrar la ejecución del programa.
9. Si el usuario ingreso un Ford con un valor menor a 1500000 informarle que puede comprar el modelo Ka.
10. Si ingresó Fiat con 3 o 5 puertas indicarle que tiene el modelo Punto.
11. Si el usuario ingreso la marca Chevrolet, con 5 puertas y un valor superior a los 2000000, indicarle que puede acceder al modelo Zafira.
12. En cualquier otra opción ingresada, indicarle que no se poseen autos con esas características.
13. Dar un mensaje de despedida y cerrar la ejecución del programa.
'''
