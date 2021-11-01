import random
"""
Los títulos de las canciones fueron extraidos de grándes éxitos de:
Luis Miguel, Morrisey, Carla Bruni, Milton Nascimento, Eros Ramazzoti, Sigur Ros, Ramstein, Percival,
"""


titulos = [
    "Ahora Te Puedes Marchar", "Cuando Calienta El Sol", "Fria Como El Viento",
    "Un Hombre Busca Una Mujer", "La Incondicional", "Entrégate", "Tengo Todo Excepto A Ti",
    "Será Que No Me Amas", "Inolvidable", "No Sé Tú", "América, América", "Hasta Que Me Olvides",
    "Suave", "El Día Que Me Quieras", "Somos Novios", "La media vuelta",

    "The Last of the Famous International Playboys", "You're Gonna Need Someone on Your Side",
    "The More You Ignore Me, the Closer I Get", "Glamorous Glue", "Girl Least Likely To", "Suedehead",
    "Tomorrow", "Boxers", "My Love Life", "Break Up the Family", "I've Changed My Plea to Guilty",
    "Such a Little Thing Makes Such a Big Difference", "Ouija Board, Ouija Board", "Interesting Drug",
    "November Spawned a Monster", "Everyday Is Like Sunday", "Interlude", "Moonriver",

    "Quelqu'un m'a dit", "Raphaël", "Tout le monde", "La noyée", "Le toi du moi", "Le ciel dans une chambre",
    "J'en connais", "Le plus beau du quartier", "Chanson triste", "L'excessive", "L'amour", "La dernière minute",

    "Maria Maria", "Cozinha", "Pilar (do Pila)", "Trabalhos (Essa Voz)", "Lilia", "A Chamada", "Era Rei E Sou Escravo",
    "Os Escravos De Jo", "Tema Dos Deuses", "Santos Catolicos x Candomble", "Pai Grande", "Seducao", "Francisco",
    "Maria Solidaria", "De Repente Maria Sumiu", "Eu Sou Uma Preta Velha Aqui Sentada", "Boca A Boca",

    "Terra promessa", "Una storia importante", "Adesso tu", "Ma che bello questo amore", "Musica è",
    "Occhi di speranza", "Più bella cosa", "Memorie", "Cose della vita", "L'aurora", "Ancora un minuto di sole",
    "Quasi amore", "Se bastasse una canzone", "Un'altra te", "Favola", "Quanto amore sei",

    "Hoppípolla", "Inní mér syngur vitleysingur", "Sæglópur", "Gobbledigook", "Í Gær", "Fljótavík",
    "Hafsól", "Heysátan", "Ti Ki", "Glósóli", "Takk...", "Mílanó", "Andvari", "Svefn-g-englar", "Starálfur",

    "Engel", "Links 2-3-4", "Keine Lust", "Mein Teil", "Du hast", "Du riechst so gut", "Ich will", "Mein Herz brennt",
    "Mutter", "Pussy", "Rosenrot", "Haifisch", "Amerika", "Sonne", "Ohne dich", "Mein Land",

    "Marysia", "Rodzanice", "Pocałunek", "Alhambra", "Lazare", "Buba", "Gdy Rozum Śpi", "Aziareczka",
    "Pani Pana", "Miesiac", "Sargon", "Sokol mi leta vysoko", "Rosa", "Wóda Zryje Banie",
    ]  # Rellenar con muuuuchos titulos random :)


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