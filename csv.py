import random

titulos = []  # Rellenar con muuuuchos titulos random :)


def titulo_random():
    return random.choice(titulos)


def genero_random():
    return random.randint(0, 5)


def idioma_random():
    return random.randint(0, 4)


def generar_csv(n=100):
    filename = "musica.csv"
    file = open(filename, "w")
    file.write("Título, Género, Idioma\n")
    for i in range(n):
        titulo = titulo_random()
        genero = genero_random()
        idioma = idioma_random()
        file.write("{}, {}, {}\n".format(titulo, genero, idioma))