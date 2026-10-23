def main():
    accesos = 0
    usuarios = {}

    with open("accesos.txt", "r", encoding="utf-8") as fichero:
        for linea in fichero:
            datos = linea.strip().split(";")

            if len(datos) == 2:
                nombre = datos[0]
                hora = datos[1]

                accesos += 1

                if nombre in usuarios:
                    usuarios[nombre] += 1
                else:
                    usuarios[nombre] = 1

    print(f"Total de accesos: {accesos}")
    print(f"Usuarios diferentes: {len(usuarios)}")

    for nombre in usuarios:
        print(f"{nombre} : {usuarios[nombre]} - {accesos}")

    if usuarios:
        mayor = max(usuarios, key=usuarios.get)
        print(f"Usuario con más accesos: {mayor}")

    with open("resumen.txt", "w", encoding="utf-8") as fichero:
        fichero.write("RESUMEN DE ACCESOS\n")
        fichero.write("------------------\n\n")
        fichero.write(f"Total de accesos: {accesos}\n")
        fichero.write(f"Usuarios diferentes: {len(usuarios)}\n\n")

        for nombre in usuarios:
            fichero.write(f"{nombre}: {usuarios[nombre]} accesos\n")

        if len(usuarios) > 0:
            fichero.write(f"\nUsuario con más accesos: {mayor}\n")

    print(f"Resumen guardado en resumen.txt")


if __name__ == "__main__":
    main()