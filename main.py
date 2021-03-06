from logic import generar_y_mostrar_vector


def menu_de_opciones():
    opcion = None
    vector = []
    matriz = []
    menu = """
-----------------------------------------------------
Menú de opciones 
-----------------------------------------------------
1 - Generar y Mostrar Vector
2 - Mostrar N canciones del idioma I
3 - Cantidad de canciones según género e idioma
4 - Cantidad de canciones del género G
5 - Buscar canción por título
6 - Generar archivo de música según idioma
7 - Cargar archivo de música según idioma
8 - Finalizar programa"""
    while opcion != "8":
        print(menu)
        opcion = input('Ingrese opción: ')
        if opcion == "1":
            generar_y_mostrar_vector(vector)
            input("...")
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