
print ("Supermercado La Ilusión")

nombre=input ("Bienvenido, Ingresá tu nombre: ")
verduleria=float(input("Ingrese el gasto en verduleria: "))
carniceria=float(input("Ingrese el gasto en carniceria: "))
almacen=float(input("Ingrese el gasto en almacen: "))

total=verduleria+carniceria+almacen
print(nombre + "su gasto total fue de " + str(total))

tarjeta=input ("Por favor, Ingrese su tarjeta: ")
print("Usted tiene un 10% de descuento por su compra con tarjeta de credito")
costofinal= total*0.9
print ("El costo final fue de ", costofinal)

print(nombre + " Gracias por su compra, hasta luego...vuelvas prontos")

'''
Realizar un programa informático en Python que:
1) De un mensaje de bienvenida al usuario que diga "Supermercado La Ilusión"
2) Le pida al usuario su nombre.
3) Le pida al usuario el monto que gastó en carnicería.
4) Le pida al usuario su gasto de verdulería.
5) Por último le pida su gasto en almacén.
6) Le informe al usuario, concatenando su nombre, el costo total de su compra.
7) Le pida al usuario el número de tarjeta de crédito.
8) Luego de ingresada la tarjeta, le informe que posee un 10% de descuento con dicho medio de pago.
9) Le indique costo final aplicando el descuento.
10) Le dé al usuario un mensaje de agradecimiento y despedida.
'''
