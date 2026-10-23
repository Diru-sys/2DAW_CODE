diccionario = {
    "casa": "house",
    "coche": "car",
    "libro": "book",
    "mesa": "table"
}

def traducir(diccionario):
    palabra = input("Introduce una palabra: ").lower()

    if palabra in diccionario:
        print(f"Traducción: {diccionario[palabra]}")
    else:
        print(f"La palabra no existe en el diccionario.")

def añadirTraduccion(diccionario):
    palabra = input("Introduce una palabra nueva en español: ").lower()



def main():
    while True:
        print()
        print("1. Traducir una palabra")
        print("2. Añadir nueva traducción")
        print("3. Modificar traducción existente")
        print("4. Eliminar una palabra")
        print("5. Mostrar todas las palabras ordenadas alfabéticamente")
        print("6. Traducir una frase")
        print("0. Salir")
        opc = int(input("Opción: "))
        match opc:
            case 1:
                traducir(diccionario)
            case 2:
                añadirTraduccion(diccionario)
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 0:
                print(f"Saliendo...")
            case _:
                print(f"Opción incorrecta o no existe.")

if __name__ == "__main__":
    main()