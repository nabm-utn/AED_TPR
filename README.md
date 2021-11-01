# AED_TPR

Se solicita un pequeño sistema para administrar listas de música personalizadas. Su primera tarea es crear, mediante un módulo separado, un archivo de texto “musica.csv” con los datos de los temas musicales generados en forma aleatoria. Por cada tema en el archivo de texto, debe haber una línea con los datos siguientes:

    Título o nombre.
    Género: 0-Balada, 1-Pop, 2-Rock, 3-Folclore, 4-Electrónica, 5-Otros.
    Idioma Original: 0-Español, 1: Inglés, 2: Francés, 3: Portugués, 4:Otros.

Su segunda tarea es desarrollar un programa que incluya la definición del tipo registro Tema (con un campo por cada dato contenido en el archivo de texto para un tema), y tal que el programa esté controlado por menú de opciones que permita:

    1 A partir del archivo de texto musica.csv (creado con el módulo separado que se indicó), generar un vector de registros, de tal manera que vaya quedando ordenado por título, con todos los temas musicales. Mostrar el vector a razón de una línea por tema mostrando el género y el idioma en lugar de sus códigos).
    2 A partir del vector generar una lista (otro vector) de n temas (n se ingresa por teclado) que sean del idioma i (i se ingresa por teclado). Si no hubiera suficientes temas del idioma ingresado, generar la lista con los que haya e informar con un mensaje. Mostrar la lista generada.
    3 A partir del vector original determinar la cantidad de temas por género y por idioma. Para eso se debe utilizar una matriz de conteo. Mostrar las cantidades sólo cuando sean mayores a 0. Se debe mostrar el nombre del idioma y del género y no sus códigos.
    4 A partir de la matriz generada en el item 3, determinar la cantidad de temas musicales para el género g, siendo g un valor ingresado por teclado.
    5 Buscar en el vector original un tema musical con el título x (x se ingresa por teclado). Si existe, mostrar sus datos. Si no, informar con un mensaje. Si hubiera más de una cortar con el primero.
    6 Ingresar por teclado un idioma i. Generar un archivo binario cuyo nombre tenga la forma “MusicaIdiomax.dat” (reemplazando x por el número del idioma seleccionado) conteniendo todos los temas de ese idioma.
    7 A partir de un idioma i ingresado por teclado, verificar si existe el archivo “MusicaIdiomaX.dat”. Si no existe, generarlo. Mostrar el contenido del archivo.

Se debe validar en toda situación posible.
