import json
from pathlib import Path

RUTA = "./datos.txt"
def guardarLog(datosAGuardar):
    with open(RUTA, "a", encoding="utf-8") as fichero:
        fichero.write(datosAGuardar)

def pedirNumero(mensaje):
    """Este metodo valida si la información introducida es un número junto con un mensaje."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(f"Debes introducir un número entero.")


def mostrar_menu():
    """Este metodo muestra el menú principal."""
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
    print("10. Calcular media curso")
    print("11. Ordenar alumnado")
    print("0. Salir")


def ordenar_alumnado(alumnado):
    """Este metodo ordena el alumnado por nombre o nota."""
    opc = pedirNumero(f"Quieres ordenar el alumnado por nombre o por nota? (1 para nombre y 2 para nota)?")

    if opc == 1:
        alumnado.sort(key=lambda alumno: alumno["nombre"].lower())
        print("Ordenado por nombre correctamente.")
        guardarLog(f"\nOrdenador por nombre correctamente")
    elif opc == 2:
        alumnado.sort(key=lambda alumno: calcular_media(alumno), reverse=True)
        print("Ordenado por nota correctamente.")
        guardarLog(f"\nOrdenado por nota correctamente")


def calcular_media(alumno):
    """Devuelve la media de las notas de un alumno (debe tener al menos una nota)."""
    return sum(alumno["notas"]) / len(alumno["notas"])


def calcular_media_de_los_cursos(alumnado):
    """Este metodo da la media ordenada por los cursos existentes."""
    cursos = []
    for alumno in alumnado:
        if alumno["curso"] not in cursos:
            cursos.append(alumno["curso"])
    
    for curso in cursos:
        medias = []
        for alumno in alumnado:
            if alumno["curso"] == curso:
                medias.append(calcular_media(alumno))
        print(f"Curso - {curso} - Media: {sum(medias) / len(medias)}")
        guardarLog(f"\nCurso - {curso} - Media: {sum(medias) / len(medias)}")


def mostrar_mejor_alumno(alumnado):
    """Muestra el alumno con la media más alta entre los que tienen notas."""
    alumno = max(alumnado, key=lambda alumno: calcular_media(alumno))

    print(f"El alumno con la media más alta de todos es: {alumno["nombre"]} y su nota media es: {calcular_media(alumno)}")
    guardarLog(f"\nEl alumno con la media más alta de todos es: {alumno["nombre"]} y su nota media es: {calcular_media(alumno)}")

def modificar_nombre_alumno(alumnado):
    """Cambia el nombre de un alumno existente."""
    nombre = input("Introduce el nombre del alumno que quieras modificar: ").strip()
    alumno = buscar_alumno(alumnado, nombre)
    if not alumno:
        print("El alumno no existe.")
        guardarLog(f"\nEl alumno no existe.")
        return

    nuevo_nombre = input("Introduce el nuevo nombre: ").strip()
    if not nuevo_nombre:
        print("El nombre no puede estar vacío.")
        guardarLog(f"\nEl nombre no puede estar vacío.")
        return

    existente = buscar_alumno(alumnado, nuevo_nombre)
    if existente and existente is not alumno:
        print("Ya existe un alumno con ese nombre.")
        guardarLog(f"\nYa existe un alumno con ese nombre.")
        return

    alumno["nombre"] = nuevo_nombre
    print(f"Nombre cambiado de '{nombre}' a '{nuevo_nombre}'.")
    guardarLog(f"\nNombre cambiado de '{nombre}' a '{nuevo_nombre}'.")


def buscar_alumno(alumnado, nombre):
    """Devuelve el alumno cuyo nombre coincide (sin distinguir mayúsculas) o None."""
    for alumno in alumnado:
        if alumno["nombre"].lower() == nombre.lower():
            return alumno
    return None


def anadir_alumno(alumnado):
    """Este metodo añade un nuevo alumno al alumnado."""
    nombre = input("Introduce el nombre del alumno: ").strip()
    if buscar_alumno(alumnado, nombre):
        print("El alumno ya existe en el sistema.")
        guardarLog(f"\nEl alumno ya existe en el sistema.")
    else:
        curso = input(f"Introduce el curso de {nombre}: ").strip()
        alumnado.append({"nombre": nombre, "notas": [], "curso": curso})
        print(f"Nombre '{nombre}' y curso '{curso}' añadido correctamente.")
        guardarLog(f"\nNombre '{nombre}' y curso '{curso}' añadido correctamente.")


def eliminar_alumno(alumnado):
    """Este metodo busca un alumno y si existe lo borra."""
    nombre = input("Introduce el nombre del alumno que quieras eliminar: ").strip()
    alumno = buscar_alumno(alumnado, nombre)
    if alumno:
        alumnado.remove(alumno)
        print(f"Alumno '{nombre}' eliminado correctamente.")
        guardarLog(f"\nAlumno'{nombre}' eliminado correctamente.")
    else:
        print("El alumno que buscas no existe.")
        guardarLog(f"\nEl alumno que buscas no existe.")


def buscar_y_mostrar_alumno(alumnado):
    """Este metodo busca el nombre de un alumno por texto y te dice si existe o no, junto con sus notas y cursos."""
    nombre = input("Introduce el nombre del alumno que quieras buscar: ").strip()
    alumno = buscar_alumno(alumnado, nombre)
    if alumno:
        print(f"\nAlumno encontrado: {alumno['nombre']}")
        print(f"Notas: {alumno['notas']}")
        print(f"Curso: {alumno['curso']}")
        guardarLog(f"\nAlumno encontrado: {alumno['nombre']}")
        guardarLog(f"\nNotas: {alumno['notas']}")
        guardarLog(f"\nCurso: {alumno['curso']}")
    else:
        print("El alumno que buscas no existe.")
        guardarLog(f"\nEl alumno que buscas no existe.")


def anadir_nota(alumnado):
    """Este metodo pide el nombre de un alumno para añadirle una nota a su lista de notas."""
    nombre = input("Introduce el nombre del alumno al que añadir la nota: ").strip()
    alumno = buscar_alumno(alumnado, nombre)
    if not alumno:
        print("El alumno no existe.")
        guardarLog(f"\nEl alumno no existe.")
        return

    nota = pedirNumero(f"Introduce la nota (0 - 10): ")
    if 0 <= nota <= 10:
        alumno["notas"].append(nota)
        print(f"Nota {nota} añadida a {alumno['nombre']}.")
        guardarLog(f"\nNota {nota} añadida a {alumno['nombre']}.")
    else:
        print("La nota debe estar entro 0 y 10.")
        guardarLog(f"\nLa nota debe estar entre 0 y 10.")


def mostrar_alumnado(alumnado):
    """Este metodo muestra todo el alumnado existente."""
    if not alumnado:
        print("No hay alumnos registrados.")
        guardarLog(f"\nNo hay alumnos registrados")
        return

    print("\n--- LISTA DE ALUMNOS ---")
    guardarLog(f"\n--- LISTA DE ALUMNOS ---")
    for alumno in alumnado:
        notas_str = ", ".join(map(str, alumno["notas"])) if alumno["notas"] else "Sin notas"
        print(f"- {alumno['nombre']}: [{notas_str}] - {alumno['curso']}")
        guardarLog(f"\n- {alumno['nombre']}: [{notas_str}] - {alumno['curso']}")


def calcular_media_alumno(alumnado):
    """Este metodo pide el nombre de un alumno para calcular su media de notas."""
    nombre = input("Introduce el nombre del alumno para calcular su media: ").strip()
    alumno = buscar_alumno(alumnado, nombre)
    if not alumno:
        print("El alumno no existe.")
        guardarLog(f"\nEl alumno no existe.")
    elif alumno["notas"]:
        media = sum(alumno["notas"]) / len(alumno["notas"])
        print(f"La media de {alumno['nombre']} es: {media:.2f}")
        guardarLog(f"\nLa media de {alumno['nombre']} es: {media:.2f}")
    else:
        print(f"{alumno['nombre']} no tiene notas registradas.")
        guardarLog(f"\n{alumno['nombre']} no tiene notas registradas.")


def calcular_media_general(alumnado):
    """Este metodo calcula la media general de todo el alumnado."""
    todas_las_notas = [nota for alumno in alumnado for nota in alumno["notas"]]
    if todas_las_notas:
        media_general = sum(todas_las_notas) / len(todas_las_notas)
        print(f"La media general de todo el alumnado es: {media_general:.2f}")
        guardarLog(f"\nLa media general de todo el alumnado es: {media_general:.2f}")
    else:
        print("No hay notas registradas en ningún alumno para calcular la media general.")
        guardarLog(f"\nNo hay notas registradas en ningún alumno para calcular la media general.")