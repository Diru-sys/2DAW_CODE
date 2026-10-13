#Main del proyecto final de Python - Carlos Sánchez Damas
from funcionesBiblio import *

def main():
    print(f"=============================")
    print(f"    GESTIÓN DE BIBLIOTECA    ")
    print(f"=============================\n")

    while True:
        menu()
        opc = pedirOpc("")
        if opc is None:
            continue
        match opc:
            case 1:
                print()
            case 2:
                print()
            case 3:
                print()
            case 4:
                print()
            case 5:
                print()
            case 6:
                print()
            case 7:
                print()
            case 8:
                print()
            case 9:
                print()
            case 0:
                print()
                break
            case _:
                print(f"Error en la selección de opciones, intentalo de nuevo.")


if __name__ == "__main__":
    main()