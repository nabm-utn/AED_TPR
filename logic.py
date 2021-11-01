from musica import Musica

# opción 1
"""
A partir del archivo de texto musica.csv (creado con el módulo separado que se indicó), 
generar un vector de registros, de tal manera que vaya quedando ordenado por título, 
con todos los temas musicales. Mostrar el vector a razón de una línea por tema 
mostrando el género y el idioma en lugar de sus códigos).
"""

def busqueda_binaria_indice_por_titulo(vector, titulo):
    """
    Encuentra mediante búsqueda binaria la posición de inserción
    de una nueva música en un arreglo, de acuerdo a su título.
    """
    min = 0
    max = len(vector) - 1
    while min <= max:
        mid = min + (max - min) // 2
        if vector[mid].titulo > titulo:
            max = mid - 1
        else:
            min = mid + 1
    return min


def insertar_cancion(vector, musica):
    indice = busqueda_binaria_indice_por_titulo(vector, musica.titulo)
    vector[indice:indice] = [musica]


def cargar_vector(vector):
    filename = "musica.csv"
    file = open(filename, "rt", encoding="utf8")
    data = file.readlines()
    file.close()
    for line in data[1:]:
        titulo, genero, idioma = line.strip().split("; ")
        musica = Musica(titulo, genero, idioma)
        insertar_cancion(vector, musica)


def mostrar_vector(vector):
    print("{:^50} ({:^11} - {:^9})".format("Título", "Género", "Idioma"))
    for musica in vector:
        print(musica)


def generar_y_mostrar_vector(vector):
    if len(vector) == 0:
        cargar_vector(vector)
    mostrar_vector(vector)


