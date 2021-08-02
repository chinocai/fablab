personal=[]

def present():
    ap= input("Ingrese su apellido: ").capitalize()
    personal.append(ap)
    menu()

def clave(texto):
    letrasA=2
    texto=str(texto).lower()
    for i in texto:
        if i == "a":
            letrasA-=1
    if letrasA == 0:
        return True
    else:
        return False

def busqueda():
    mirar = input("Apellido de quien esta buscando: ").capitalize()
    for i in personal:
        if i == mirar:
            print(i, "se encuentra presente!")
            break
    else:
        print(i,"NO se encuentra...")
    menu()

def asist():
    print("\n1. supervisor\n2. jefe de departamento\n3. gerente\n")
    asi=input("Verifique su cargo: ")
    if 0 < asi < 4:
        for i in asi:
            codigo = input("Ingrese su clave: ")
            if clave(codigo)==True:
                busqueda()
                break
        else:
            menu()
    else:
        asist()

def menu():
    print("""
    1. Dar Presente
    2. Ver Asistencia
    3. Salir""")
    op = input(" >>> ")
    if op == "1":
        present()
    elif op == "2":
        asist()
    elif op =="3":
        exit()
    else:
        menu()

print(" Sistema de gestión de personal ".center(80,"-"))
menu()