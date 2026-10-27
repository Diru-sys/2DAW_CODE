peliculas = [
    {
        "titulo": "Matrix",
        "anio": 1999,
        "genero": "Ciencia ficción",
        "puntuacion": 8.7
    },
    {
        "titulo": "Gladiator",
        "anio": 2000,
        "genero": "Drama",
        "puntuacion": 8.5
    }
]


def añadir_pelicula(peliculas):
    titulo = input("Título: ")

    for pelicula in peliculas:
        if pelicula["titulo"].lower() == titulo.lower():
            print(f"La película ya existe.")
            return

    año = int(input("Año: "))
    genero = input("Género: ")
    puntuacion = float(input("Puntuación: "))

    pelicula = {
        "titulo": titulo,
        "anio": año,
        "genero": genero,
        "puntuacion": puntuacion
    }

    peliculas.append(pelicula)
    print(f"Película añadida.")

def buscar_pelicula(peliculas, titulo):
    for pelicula in peliculas:
        if pelicula["titulo"].lower() == titulo.lower():
            return pelicula
    return None

def mostrar_peliculas(peliculas):
    for pelicula in peliculas:
        print(pelicula)

def mostrar_genero(peliculas):
    genero = input("Introduce el género: ").lower()

    for pelicula in peliculas:
        if pelicula["genero"].lower() == genero:
            print(pelicula)

def mostrar_posteriores(peliculas):
    año = int(input("Introduce un año: "))

    for pelicula in peliculas:
        if pelicula["anio"] > año:
            print(pelicula)

def puntuacion_media(peliculas):
    if len(peliculas) == 0:
        print(f"No hay películas.")
        return

    total = 0

    for pelicula in peliculas:
        total += pelicula["puntuacion"]

    print(f"Puntuación media:", total / len(peliculas))

def mejor_pelicula(peliculas):
    if len(peliculas) == 0:
        print(f"No hay películas.")
        return

    mejor = peliculas[0]

    for pelicula in peliculas:
        if pelicula["puntuacion"] > mejor["puntuacion"]:
            mejor = pelicula
    print(f"Mejor película:", mejor)

def eliminar_pelicula(peliculas):
    titulo = input("Título de la película que quieres eliminar: ")
    pelicula = buscar_pelicula(peliculas, titulo)

    if pelicula is not None:
        peliculas.remove(pelicula)
        print(f"Película eliminada.")
    else:
        print(f"Película no encontrada.")

def main():
    while True:
        print()
        print("\n1. Añadir película")
        print("2. Buscar película")
        print("3. Mostrar todas")
        print("4. Mostrar por género")
        print("5. Mostrar posteriores a un año")
        print("6. Calcular puntuación media")
        print("7. Mostrar mejor película")
        print("8. Eliminar película")
        print("9. Salir")
        opc = int(input("Opción: "))

        match opc:
            case 1:
                añadir_pelicula(peliculas)
            case 2:
                titulo = input("Título: ")
                pelicula = buscar_pelicula(peliculas, titulo)

                if pelicula is not None:
                    print(pelicula)
                else:
                    print(f"Película no encontrada.")
            case 3:
                mostrar_peliculas(peliculas)
            case 4:
                mostrar_genero(peliculas)
            case 5:
                mostrar_posteriores(peliculas)
            case 6:
                puntuacion_media(peliculas)
            case 7:
                mejor_pelicula(peliculas)
            case 8:
                eliminar_pelicula(peliculas)
            case 9:
                print(f"Saliendo..")
                break
            case _:
                print("Opción incorrecta.")


if __name__ == "__main__":
    main()
