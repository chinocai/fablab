#FabLab MVL - Curso de introduccion a Python
#Ejercicio 5 - Colecciones
#por Gonzalo Otano

#Listas
list_infantiles = [ 'Blancanieves' ,'Los Tres Chanchitos' ,'Cenicienta' ]  

list_novelas = [ 'Don Quijote' ,'La Novicia Rebelde' ]

list_policiales = [ 'Sherlock Holmes' ,'Muerte en el Nilo' ]

#Funciones
def elegir_opcion():
    
    print('''
    ========== Bienvenido al Sistema Online de Gestion de la Biblioteca Nacional ==========
    
    1. Ver libros disponibles
    2. Ver stock de libros disponibles
    3. Agregar un libro
    4. Eliminar un libro
    5. Salir del sistema
    ''')
    
    op = input("Ingrese una opcion: ")
    
    return op

def ver_libros():
    while True: 
        
        print('''
        === Consulta por Genero ===
        
        Generos disponibles:

        1. Infantiles
        2. Novelas
        3. Policiales
        0. Todos

        *. Menu anterior
        ''')
        
        cat = str(input('Ingrese el numero correspondiente al genero que desea consultar: '))
        
        if not (cat == '1' or cat == '2' or cat == '3' or cat == '0' or cat == '*'):
            print('')
            print('''Usted ha ingresado una opcion incorrecta
            ''')
            input('Presione Enter para continuar ')

        elif cat == '1':
            print('''
            Mostrando todos los titulos en: Infantiles''')
            list_infantiles.sort()
            print(list_infantiles)
            print('')
            input('Presione Enter para continuar ')

        elif cat == '2':
            print('''
            Mostrando todos los titulos en: Novelas''')
            list_novelas.sort()
            print(list_novelas)
            print('')
            input('Presione Enter para continuar ')
        
        elif cat == '3':
            print('''
            Mostrando todos los titulos en: Policiales''')
            list_policiales.sort()
            print(list_policiales)
            print('')
            input('Presione Enter para continuar ')
        
        elif cat == '0':
            print('''
            Mostrando todos los titulos en: Infantiles''')
            list_infantiles.sort()
            print(list_infantiles)
            print('''
            Mostrando todos los titulos en: Novelas''')
            list_novelas.sort()
            print(list_novelas)
            print('''
            Mostrando todos los titulos en: Policiales''')
            list_policiales.sort()
            print(list_policiales)
            print('')
            input('Presione Enter para continuar ')

        elif cat == '*':
            break

        continue

def ver_stock():
    while True:
        
        db = list_infantiles + list_novelas + list_policiales
        db2 = []
        for i in db:
            db2.append(i.lower())

        print('''
        === Consulta de stock ===
        ''')
        
        title = input('''Ingrese el titulo del libro del cual desea consultar el stock (* -> Menu anterior): ''')
        
        if title == '*':
            break

        elif title not in db2:
            print('''El titulo no se encuentra disponible.
            ''')
            input('Presione Enter para continuar')
        
        else:
            stock = db2.count(title)
            print('')
            print(title,'Stock disponible:',stock)
            print('')
            input('Presione Enter para continuar')

        continue
             
def agregar_libros():
    while True:
        print('''
        === Agregar nuevo libro ===
    
        Agregar por genero existente:
    
        1. Infantiles
        2. Novelas
        3. Policiales

        *. Menu Anterior
        ''')
        
        cat = input('Ingrese a que genero corresponde el libro que desea agregar: ')
        
        if not ( cat == '1' or cat == '2' or cat == '3' or cat == '*'):
            print('''
            Genero no disponible
            ''')
            input('Presione Enter para continuar')
        
        elif cat == '*':
            break

        else:
            title = input('Ingrese el titulo del libro: ')
            
            if cat == '1':
                list_infantiles.append(title)
                print('''
                Titulo agregado con exito!
                ''')
                input('Presione Enter para continuar')           
            
            elif cat == '2':
                list_novelas.append(title)
                print('''
                Titulo agregado con exito!
                ''')
                input('Presione Enter para continuar')

            elif cat == '3':
                list_policiales.append(title)
                print('''
                Titulo agregado con exito!
                ''')
                input('Presione Enter para continuar')

        continue        

def eliminar_libros():
    while True:
        
        db = list_infantiles + list_novelas + list_policiales

        print('''
        === Eliminar libro ===

        1. Ver titulos disponibles
        2. Ingresar titulo a eliminar
        
        *. Menu anterior
        ''')

        op_del = input('Ingrese una opcion: ')
        
        if not (op_del == '1' or op_del == '2' or op_del == '*'):
            print('')
            print('''Usted ha ingresado una opcion incorrecta
            ''')
            input('Presione Enter para continuar ')
        
        elif op_del == '*':
            break

        elif op_del == '1':
            ver_libros()
        
        elif op_del == '2':
            while True:
                print('')

                title = input('Ingrese el titulo del libro que desea eliminar (* -> Menu Anterior): ')

                if title not in db and title != '*':
                    print('''
                    No se ha encontrado el titulo
                    ''')
                    input('Presione Enter para continuar')

                elif title == '*':
                    break

                else:
                    if title in list_infantiles:
                        list_infantiles.remove(title)

                    elif title in list_novelas:
                        list_novelas.remove(title)

                    elif title in list_policiales:
                        list_policiales.remove(title)
                    
                    print('''
                    Titulo eliminado con exito!
                    ''')

                continue   

        continue

#Programa

while True:

    op = elegir_opcion()

    if op == '1':
        ver_libros()
    
    elif op == '2':
        ver_stock()
    
    elif op == '3':
        agregar_libros()
    
    elif op == '4':
        eliminar_libros()
    
    elif op == '5':
        print(''' 
        Gracias por utilizar el Sistema Online de Gestion de la Biblioteca Nacional''')
        break
    
    else:
        print('''
        Usted ingreso una opcion incorrecta
        ''')
        input('Presione Enter para continuar')
    
    continue

exit()