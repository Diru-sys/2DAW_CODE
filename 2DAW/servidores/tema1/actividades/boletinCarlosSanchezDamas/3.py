#Gestión de puntuaciones de un videojuego
puntuaciones = {
    "Mario": 1250,
    "Lucía": 890,
    "Carlos": 1420,
    "Ana": 1100
}


def añadirJugador(puntuaciones):
    nombre = input("Introduce el nombre de un jugador: ").strip()
    puntuacion = int(input("Introduce una puntuación para este jugador: "))
    if puntuacion < 0:
        raise ValueError("La puntuación no puede ser menor que 0.")
    puntuaciones[nombre] = puntuacion
    return f"Jugador y puntuación nueva añadida correctamente."


def modificarPuntuacion(puntuaciones):
    nombreModificar = input("Introduce el nombre de quién quieres cambiar la puntuación: ").strip()
    puntuacionNueva = int(input("Introduce una nueva puntuación: "))
    if puntuacionNueva < 0:
        raise ValueError("La nueva puntuación no puede ser menor que 0.")

    for nombre in puntuaciones:
        if nombreModificar.lower() == nombre.lower():
            puntuaciones[nombre] = puntuacionNueva
            return f"Puntuación del jugador {nombreModificar} actualizada."
    return f"Jugador no encontrado correctamente."


def eliminarJugador(puntuaciones):
    nombreJugador = input("Introduce el nombre del jugador que quieras borrar: ").strip()
    for nombre in puntuaciones:
        if nombreJugador.lower() == nombre.lower():
            del puntuaciones[nombreJugador]


def consultarJugador(puntuaciones):
    nombreJugador = input("Introduce el nombre del jugador que quieras consultar: ").strip()
    if not nombreJugador:
        raise ValueError("El nombre del jugador no puede estar vacio.")
    
    for nombre in puntuaciones:
        if nombreJugador.lower() == nombre.lower():
            print(f"Nombre del jugador: {nombre} - Puntuación: {puntuaciones[nombre]}")
            return
    print(f"No se encontró al jugador {nombreJugador}")


def main():
    print(f" ==== MENÚ ==== ")
    while True:
        print("1. Añadir jugador")
        print("2. Modificar puntuación")
        print("3. Eliminar jugador")
        print("4. Consultar jugador")
        print("5. Mostrar mejor jugador")
        print("6. Mostrar jugadores que superan una puntuación")
        print("7. Mostrar puntuación media")
        print("8. Salir")
        opc = int(input("Opción: "))
        match opc:
            case 1:
                añadirJugador(puntuaciones)
            case 2:
                modificarPuntuacion(puntuaciones)
            case 3:
                eliminarJugador(puntuaciones)
            case 4:
                consultarJugador(puntuaciones)
            case 5:
                print()
            case 6:
                print()
            case 7:
                print()
            case 8:
                print("HASTA PRONTO.")
                exit


if __name__ == "__main__":
    main()
