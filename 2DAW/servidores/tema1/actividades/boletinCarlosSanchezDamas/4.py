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

    if palabra in diccionario:
        print(f"La palabra ya está en el diccionario.")
    else:
        traduccion = input("Introduce la traducción de esta palabra: ").lower()
        diccionario[palabra] = traduccion
        print(f"Traducción añadida correctamente.")

def modificar(diccionario):
    palabra = input("Introduce una palabra del diccionario: ").lower()

    if palabra not in diccionario:
        print(f"Esta palabra no está en el diccionario.")
    else:
        traduccion = input("Introduce la nueva traducción de la palabra: ").lower()
        diccionario[palabra] = traduccion
        print(f"Traducción modificada correctamente.")

def eliminar(diccionario):
    palabra = input("Introduce una palabra del diccionario: ").lower()
    if palabra in diccionario:
        del diccionario[palabra]
        print(f"Palabra eliminada correctamente.")
    else:
        print(f"Esta palabra no está en el diccionario.")

def ordenadas(diccionario):
    palabrasOrdenadas = sorted(diccionario)

    for palabra in palabrasOrdenadas:
        traduccion = diccionario[palabra]
        print(f"{palabra} : {traduccion}")

def frase(diccionario):
    frase = input("Introduce una frase: ").lower().strip()
    fraseSeparada = frase.split()
    fraseTraducida = []
    for palabra in fraseSeparada:
        if palabra in diccionario:
            fraseTraducida.append(diccionario[palabra])
        else:
            fraseTraducida.append(palabra)
    print(f"Frase traducida:{fraseTraducida}")

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
                modificar(diccionario)
            case 4:
                eliminar(diccionario)
            case 5:
                ordenadas(diccionario)
            case 6:
                frase(diccionario)
            case 0:
                print(f"Saliendo...")
                break
            case _:
                print(f"Opción incorrecta o no existe.")

if __name__ == "__main__":
    main()