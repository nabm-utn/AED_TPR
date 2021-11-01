class Musica:
    _generos = ["Balada", "Pop", "Rock", "Folclore", "Electrónica", "Otros"]
    _idiomas = ["Español", "Inglés", "Francés", "Portugués", "Otros"]

    def __init__(self, titulo, genero, idioma):
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma

    def __str__(self):
        return "{}  ({} - {})".format(self.titulo, self._generos[self.genero], self._idiomas[self.idioma])
