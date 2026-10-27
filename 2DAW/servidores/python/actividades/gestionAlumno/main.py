from gestorAlumno import *

def main():
    print(" ==== GESTIÓN DEL ALUMNADO === ")
    guardarLog(f"\n ==== GESTIÓN DEL ALUMNADO === ")
    alumnado = [
        {
            "nombre": "Ana",
            "notas": [7.0, 8.0],
            "curso": "1º DAW"
        },
        {
            "nombre": "Pepe",
            "notas": [5.0, 10.0],
            "curso": "2º DAW"
        },
        {
            "nombre": "Carlos",
            "notas": [2.0, 6.0],
            "curso": "2º DAW"
        },
        {
            "nombre": "Javier",
            "notas": [7.0, 7.0],
            "curso": "1º DAW"
        },
    ]
    while True:
            mostrar_menu()
            opc = pedirNumero("")
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
                case 10:
                    calcular_media_de_los_cursos(alumnado)
                case 11:
                    ordenar_alumnado(alumnado)
                case 0:
                    print("¡Hasta luego!")
                    guardarLog(f"\nFinalización del programa.")
                    break
                case _:
                    print("Error en la selección de opciones, intenta de nuevo.")
                    guardarLog(f"\nError en la selección de opciones, intenta de nuevo.")


if __name__ == "__main__":
    main()