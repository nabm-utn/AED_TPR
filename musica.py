class Musica:
    def __init__(self, titulo, genero, idioma):
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma

    def __str__(self):
        return "{}  ({}/{})".format(self.titulo, self.genero, self.idioma)
