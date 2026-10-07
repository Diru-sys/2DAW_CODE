#GESTOR DE TAREAS
"""Para cada tarea va a tener:
- titulo
- tiempo en horas
- realizada
-> Cada tarea es un diccionario que tiene una de estas variables.
-> Se debe tener varias funciones: LIstar, Añadir, Buscar, Borrar, Editar
"""
#----------------------------------------------------------------------------------------------------------#
tareas = []


def listarTareas(tareas):
    """Lista todas las tareas existentes"""
    if not tareas:
        print("No existen tareas registradas.")
    else:
        print("Listado de tareas")
        print(tareas)


def añadirTarea(tareas):
    """Añade una nueva tarea a mi lista de diccionarios de tareas"""
    titulo = str(input("Introduce el titulo de la tarea: "))
    tiempo = int(input(f"Introduce el tiempo para la tarea {titulo} en horas: "))
    realizada = str(input(f"¿Está la tarea realizada? (Si/No): ")).lower().strip()
    if realizada == "si":
        realizada = True
    elif realizada == "no":
        realizada = False
    tareaEscrita = {
        "titulo": titulo,
        "tiempo": tiempo,
        "realizada": realizada
    }
    tareas.append(tareaEscrita)
    print("Tarea añadida correctamente.")


def buscarTarea(tareas, titulo):
    """Busca una tarea en mi lista de diccionarios de tareas"""
    for tarea in tareas:
        if tarea["titulo"].lower() == titulo.lower():
            return tarea
    return None


def buscarMostrarTarea(tareas):
    """Buscar y mostrar la tarea"""
    titulo = input("Titulo de la tarea a buscar: ").strip()
    tarea = buscarTarea(tareas, titulo)

    if tarea is None:
        print(f"Tarea no encontrada.")
    else:
        print(
            f"Tarea encontrada.\n"
            f"Titulo: {tarea['titulo']}\n"
            f"Tiempo: {tarea['tiempo']} horas\n"
            f"Realizada: {tarea['realizada']}"
        )


def borrarTarea(tareas):
    """"Borra una tarea"""
    titulo = input("Titulo de la tarea a borrar: ").strip()
    tarea = buscarTarea(tareas, titulo)

    if tarea is None:
        print(f"Tarea no encontrado o no es posible de borrar.")
    else:
        tareas.remove(tarea)
        print(f"Tarea borrada correctamente.")


def editarTarea(tareas):
    """Edita una tarea ya existente"""
    titulo = input("Titulo de la tarea que quieres editar: ")
    tarea = buscarTarea(tareas, titulo)

    if tarea is None:
        print(f"Tarea no encontrada con este titulo.")
    else:
        while True:
            opc = int(input("¿Que quieres editar?\n" \
            "1.- Titulo de la tarea\n" \
            "2.- Tiempo realizado de la tarea en horas\n" \
            "3.- Tarea realizada (Si/No)\n" \
            "0.- Terminar de editar\n"))

            match (opc):
                case 1:
                    tarea["titulo"] = str(input("Titulo nuevo: "))
                    print(f"Titulo modificado")

                case 2:
                    tarea["tiempo"] = str(input("Tiempo nuevo: "))
                    print(f"Tiempo modificado")

                case 3:
                    estado = str(input("Estado de la tarea nuevo (Si/No): ")).strip().lower()
                    if estado == "si":
                        tarea["realizada"] = True
                    elif estado == "no":
                        tarea["realizada"] = False
                    print(f"Estado de la tarea actualizado")

                case 0:
                    print("Edición de la tarea terminada.")
                    break

                case _:
                    print("Opción incorrecta.")


def marcarTarea(tareas):
    titulo = str(input(f"Titulo de la tarea que quieres marcar como completada: "))
    tarea = buscarTarea(tareas, titulo)

    if tarea is None:
        print(f"Tarea no encontrada con este titulo.")
    else:
        tarea["realizada"] = True
        print(f"Tarea marcada como completa correctamente.")


def contiene(tareas):
    texto = str(input(f"Texto que quieres buscar en los titulos de las tareas: "))
    contenedores = [tarea for tarea in tareas if texto in tarea["titulo"]]
    print(f"Tareas que contienen este texto guardadas correctamente dentro de contenedores.")


def main():
    while True:
        opc = int(input(
        "\n====================\n"
        "  GESTOR DE TAREAS  \n"
        "====================\n"
        "1. Listar todas las tareas\n"
        "2. Añadir una tarea\n"
        "3. Buscar una tarea\n"
        "4. Borrar una tarea\n"
        "5. Editar una tarea\n"
        "6. Marcar tarea como realizada\n"
        "7. Filtrar tareas por coincidencia de texto\n"
        "0. Salir\n"
        ))
        match (opc):
            case 0:
                print("\nPrograma finalizado.")
                break

            case 1:
                listarTareas(tareas)

            case 2:
                añadirTarea(tareas)

            case 3:
                buscarMostrarTarea(tareas)

            case 4:
                borrarTarea(tareas)

            case 5:
                editarTarea(tareas)

            case 6:
                marcarTarea(tareas)

            case 7:
                contiene(tareas)

            case _:
                print("Opción invalida, vuelve a intentar de nuevo.")


if __name__ == "__main__":
    main()