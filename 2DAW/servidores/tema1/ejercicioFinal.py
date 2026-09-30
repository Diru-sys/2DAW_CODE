# ACTIVIDAD FINAL
def mostrar_menu():
    """Muestra el menú principal."""
    print("\n--- MENÚ ---")
    print("1. Añadir alumno")
    print("2. Eliminar alumno")
    print("3. Buscar alumno")
    print("4. Añadir nota")
    print("5. Mostrar alumnado")
    print("6. Calcular media de un alumno")
    print("7. Calcular media general")
    print("8. Mostrar mejor alumno")
    print("9. Modificar nombre de un alumno")
    print("0. Salir")


def calcular_media(alumno):
    """Devuelve la media de las notas de un alumno (debe tener al menos una nota)."""
    return sum(alumno["notas"]) / len(alumno["notas"])


def mostrar_mejor_alumno(alumnado):
    """Muestra el alumno con la media más alta entre los que tienen notas."""
    mejor = None
    mejor_media = -1

    for alumno in alumnado:
        if alumno["notas"]:
            media = calcular_media(alumno)
            if media > mejor_media:
                mejor = alumno
                mejor_media = media

    if mejor is None:
        print("No hay alumnos con notas registradas.")
    else:
        print(f"El mejor alumno es {mejor['nombre']} con una media de {mejor_media:.2f}.")


def modificar_nombre_alumno(alumnado):
    """Cambia el nombre de un alumno existente."""
    nombre = input("Introduce el nombre del alumno que quieras modificar: ").strip()
    alumno = buscar_alumno(alumnado, nombre)
    if not alumno:
        print("El alumno no existe.")
        return

    nuevo_nombre = input("Introduce el nuevo nombre: ").strip()
    if not nuevo_nombre:
        print("El nombre no puede estar vacío.")
        return

    existente = buscar_alumno(alumnado, nuevo_nombre)
    if existente and existente is not alumno:
        print("Ya existe un alumno con ese nombre.")
        return

    alumno["nombre"] = nuevo_nombre
    print(f"Nombre cambiado de '{nombre}' a '{nuevo_nombre}'.")


def pedir_opcion():
    """Pide una opción al usuario. Devuelve None si no es un número válido."""
    texto = input("Selecciona una opción: ").strip()
    if texto.isdecimal():
        return int(texto)
    print("Por favor, introduce un número válido.")
    return None


def es_numero(texto):
    """Comprueba si un texto representa un número (entero o decimal con punto)."""
    if texto.startswith("-"):
        texto = texto[1:]
    return texto.replace(".", "", 1).isdecimal()


def buscar_alumno(alumnado, nombre):
    """Devuelve el alumno cuyo nombre coincide (sin distinguir mayúsculas) o None."""
    for alumno in alumnado:
        if alumno["nombre"].lower() == nombre.lower():
            return alumno
    return None


def anadir_alumno(alumnado):
    nombre = input("Introduce el nombre del alumno: ").strip()
    if buscar_alumno(alumnado, nombre):
        print("El alumno ya existe en el sistema.")
    else:
        alumnado.append({"nombre": nombre, "notas": []})
        print(f"Alumno '{nombre}' añadido correctamente.")


def eliminar_alumno(alumnado):
    nombre = input("Introduce el nombre del alumno que quieras eliminar: ").strip()
    alumno = buscar_alumno(alumnado, nombre)
    if alumno:
        alumnado.remove(alumno)
        print(f"Alumno '{nombre}' eliminado correctamente.")
    else:
        print("El alumno que buscas no existe.")


def buscar_y_mostrar_alumno(alumnado):
    nombre = input("Introduce el nombre del alumno que quieras buscar: ").strip()
    alumno = buscar_alumno(alumnado, nombre)
    if alumno:
        print(f"\nAlumno encontrado: {alumno['nombre']}")
        print(f"Notas: {alumno['notas']}")
    else:
        print("El alumno que buscas no existe.")


def anadir_nota(alumnado):
    nombre = input("Introduce el nombre del alumno al que añadir la nota: ").strip()
    alumno = buscar_alumno(alumnado, nombre)
    if not alumno:
        print("El alumno no existe.")
        return

    texto = input("Introduce la nota (0 - 10): ").strip()
    if not es_numero(texto):
        print("Error: Debes introducir un número.")
        return

    nota = float(texto)
    if 0 <= nota <= 10:
        alumno["notas"].append(nota)
        print(f"Nota {nota} añadida a {alumno['nombre']}.")
    else:
        print("La nota debe estar entre 0 y 10.")


def mostrar_alumnado(alumnado):
    if not alumnado:
        print("No hay alumnos registrados.")
        return

    print("\n--- LISTA DE ALUMNOS ---")
    for alumno in alumnado:
        notas_str = ", ".join(map(str, alumno["notas"])) if alumno["notas"] else "Sin notas"
        print(f"- {alumno['nombre']}: [{notas_str}]")


def calcular_media_alumno(alumnado):
    nombre = input("Introduce el nombre del alumno para calcular su media: ").strip()
    alumno = buscar_alumno(alumnado, nombre)
    if not alumno:
        print("El alumno no existe.")
    elif alumno["notas"]:
        media = sum(alumno["notas"]) / len(alumno["notas"])
        print(f"La media de {alumno['nombre']} es: {media:.2f}")
    else:
        print(f"{alumno['nombre']} no tiene notas registradas.")


def calcular_media_general(alumnado):
    todas_las_notas = [nota for alumno in alumnado for nota in alumno["notas"]]
    if todas_las_notas:
        media_general = sum(todas_las_notas) / len(todas_las_notas)
        print(f"La media general de todo el alumnado es: {media_general:.2f}")
    else:
        print("No hay notas registradas en ningún alumno para calcular la media general.")


def main():
    print(" ==== GESTIÓN DEL ALUMNADO === ")
    alumnado = [
        {
            "nombre": "Ana",
            "notas": [7.0, 8.0]
        }
    ]

    while True:
        mostrar_menu()
        opc = pedir_opcion()
        if opc is None:
            continue

        match opc:
            case 1:
                anadir_alumno(alumnado)
            case 2:
                eliminar_alumno(alumnado)
            case 3:
                buscar_y_mostrar_alumno(alumnado)
            case 4:
                anadir_nota(alumnado)
            case 5:
                mostrar_alumnado(alumnado)
            case 6:
                calcular_media_alumno(alumnado)
            case 7:
                calcular_media_general(alumnado)
            case 8:
                mostrar_mejor_alumno(alumnado)
            case 9:
                modificar_nombre_alumno(alumnado)
            case 0:
                print("¡Hasta luego!")
                break
            case _:
                print("Error en la selección de opciones, intenta de nuevo.")


if __name__ == "__main__":
    main()