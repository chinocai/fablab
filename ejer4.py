
def op_uno():  # Funcion de comprar electrodomésticos
    print("""
    1. Heladera de $60000
    2. Lavarropas de $45000
    3. Cocina de $25000    """)  # Igual que los comentarios multilineas, si en un print
    # se le pone """ al inicio y al final permite escribir en varias lineas.
    op = int(input(" Que desea comprar: "))
    # Guardo en OP el numero que le paso, si el numero es menor a 1 o mayor a 3, me tira
    # mensaje de error y me manda al principio de la funcion. En caso de elegir 1, 2 o 3
    # guarda en ASD el monto a pagar por el item elegido...
    if op < 1 or op > 3:
        input("Dato no reconocido, presione ENTER para regresar.")
        asd = op_uno()
    else:
        if op == 1:
            asd = 60000
        elif op == 2:
            asd = 45000
        else:
            asd = 25000
    # Retornamos la variable ASD con el monto que se elegio...
    return asd


def op_dos():  # Funcion de comprar TV/Audio
    print("""
    1. Minicomponente de $30000
    2. Led de $45000
    3. Smart TV de $125000    """)  # Igual que los comentarios multilineas, si en un print
    # se le pone """ al inicio y al final permite escribir en varias lineas.
    op = int(input(" Que desea comprar: "))
    # Guardo en OP el numero que le paso, si el numero es menor a 1 o mayor a 3, me tira
    # mensaje de error y me manda al principio de la funcion. En caso de elegir 1, 2 o 3
    # guarda en ASD el monto a pagar por el item elegido...
    if op < 1 or op > 3:
        input("Dato no reconocido, presione ENTER para regresar.")
        asd = op_dos()
    else:
        if op == 1:
            asd = 30000
        elif op == 2:
            asd = 45000
        else:
            asd = 125000
    # Retornamos la variable ASD con el monto que se elegio...
    return asd


def tarjeta():  # Funcion de la carga de tarjeta de credito
    num = input(" Número de tarjeta de crédito: ")
    # Cargo en NUM el str de la tarjeta de credito, el cual despues con la funcion len verifico
    # la cantidad de digitos que tiene, si es distinto a 12, le indico que no tiene 12 y vuelvo
    # a llamar a la funcion. Cuando me de una tarjeta de 12 digitos, se llama a return para que
    # devuelva ese str con el numero de la tarjeta...
    if len(num) != 12:
        print("La tarjeta no tiene 12 numeros, ingreselo de nuevo.")
        tarjeta()
    else:
        return num


def venta_Final(compra):  # Fucion de el final de la venta...
    # Llamo la funcion tarjeta y guardo el valor retornado de ella en tarjeta_numero
    tarjeta_numero = tarjeta()
    # Pregunto si tiene codigo promocional, poniendo lower() al final hago que todo lo
    # puesto se transforme automaticamente a minusculas...
    cod = input(" Tiene un código promocional? (si/no) ").lower()
    # Si COD es distinto a "si", le informo el monto que tiene que pagar y su num de
    # tarjeta. En caso de ser "si", nos pregunta el codigo y si es "1234", nos avisa de
    # que tenemos un descuento de $5000...  hago la cuenta dentro de COSTO, descontando
    # 5000 a la compra y paso el mensaje de lo que costo todo y de su tarjeta.
    if cod != "si":
        # Esta es otra manera de "condenar" informacion a un print, si apenas ponemos una
        # f despues del ( indicamos que el texto va a tener un formato. Eso significa que
        # escribimos lo que queremos, pero cuando queremos hacer referencia a una variable
        # ponemos la misma entre {}
        print(
            f" Su compra de ${compra} será debitado de su tarjeta {tarjeta_numero}")
    else:
        cod = input(" Ingrese su codigo: ")
        if cod == "1234":
            print(" Tiene un descuento de $5000")
            costo = compra-5000
            print(
                f" Su compra de ${costo} será debitado de su tarjeta {tarjeta_numero}")
    input("Gracias por su compra")
    # Con este ultimo input damos un mensaje de despedida y a continuacion salimos del programa.
    exit()


def menu():  # Funcion del menu...
    # Defino 2 variables con un valor a 0, que luego usare adelante o no...
    electro = 0
    autv = 0
    # Imprimo un semi titrular de 30 espacios vacios, en el medio del mismo pongo MENU
    print(" MENU ".center(30, " "))
    print("""
    1. Comprar electrodomésticos
    2. Comprar Audio/Tv
    3. Ambas
    """)
    opcion = int(input(" Que opcion quiere elegir: "))
    # Pido una opcion a elegir, si es menor a 1 o mayor a 3, le indico el error y llamo
    # denuevo a menu. En caso de elegir 1, llamamos a op_uno. En caso de elegir 2, llamamos
    # a op_dos. En caso 3, llamamos a ambas...
    if opcion < 1 or opcion > 3:
        input("Dato no reconocido, presione ENTER para regresar al menu.")
        menu()
    else:
        if opcion == 1:
            electro = op_uno()
        elif opcion == 2:
            autv = op_dos()
        else:
            electro = op_uno()
            autv = op_dos()
    # Sea lo que sea que elegimos grardamos los valores retornados en variables que definimos
    # al principio. En MONTO sumamos ambas variables, en caso de la opcion 1 o 2, iba a dar error
    # si sumamos a una variable desconocida si no las agregabamos al principio...
    monto = electro + autv
    # Indicamos el monto a pagar
    print(" Usted ha comprado un total de $" + str(monto))
    # Llamamos a la funcion venta_Final y le pasamos el parametro con lo que se gasto en la compra
    venta_Final(monto)


print(" Garbarino Online ".center(60, "-"))
# Iniciamos el programa poniendo un titular de 60 caracteres de ancho de "-" y en el centro el titulo
# Y automaticamente llamamos a la funcion menu
menu()

"""
Desarrollas un programa en python que:
1. Imprima el mensaje "Garbarino Online".
2. Le pida al usuario que seleccione entre las operaciones de comprar electrodomésticos, comprar Audio/Tv o ambas.
3. Si selecciona la opción electrodomésticos deberá pedirle que elija entre una heladera de $60000, un lavarropas de $45000 o una cocina de $25000.
4. Si la elección del usuario no corresponde a alguna de estas opciones, deberá pedirle que lo ingrese nuevamente hasta que lo haga correctamente.
5. Si selecciona la opción TV/Audio deberá pedirle que elija entre un minicomponente de $30000, un led de $45000 o un smart tv de $125000.
6. Si la elección del usuario no corresponde a alguna de estas opciones, deberá pedirle que lo ingrese nuevamente hasta que lo haga correctamente.
7. En caso que seleccione ambas, darle la posibilidad que selecciones entre todas las opciones, una de electrodomésticos  y una de TV/Audio.
8. Al finalizar la selección por parte del usuario, mostrarle el monto final de su compra.
9. Pedirle que ingrese un número de tarjeta de crédito.
10. Si la tarjera ingresada no tiene 12 dígitos, pedirle que la ingrese nuevamente. Repetir esta acción hasta que el usuario lo haga correctamente.
11. Preguntarle al usuario si tiene un código promocional. Es caso negativo, informarle que el total de su compra será debitado de su tarjeta.
12. En caso que posea un código, pedirle que lo ingrese. Si el mismo es igual a "1234" informarle que tiene un descuento de $5000, calcular el costo final e indicarle que el mismo será debitado de su tarjeta.
13. Si el código es incorrecto, informárselo y no aplicar ningún descuento. Informar el costo final e indicarle que el mismo será debitado de su tarjeta.
14. Imprimir el mensaje "Gracias por su compra" y cerrar la ejecución del programa.
"""