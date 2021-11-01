def menu_de_opciones():
    opcion = None
    menu = """
-----------------------------------------------------
Menú de opciones 
-----------------------------------------------------
1 - Opcion 1
2 - Opcion 2
3 - Opcion 3
4 - Opcion 4
5 - Opcion 5
6 - Opcion 6
7 - Opcion 7
8 - Finalizar programa"""
    while opcion != "8":
        print(menu)
        opcion = input('Ingrese opción: ')
        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            pass
        elif opcion == "8":
            confirmacion = input("Seleccionó finalizar programa. ¿Está seguro que desea salir? (s/n): ")
            if confirmacion == "s" or confirmacion == "S":
                print("Gracias por utilizar este programa. Hasta pronto.")
            else:
                print("Regresando al menu principal...")
                continue
        else:
            print("La opción ingresada no es válida")


if __name__ == "__main__":
    menu_de_opciones()