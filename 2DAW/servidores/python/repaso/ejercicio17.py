class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return f"<Sonido de animal>"

    def __str__(self):
        return f"Nombre del animal: {self.nombre}"


class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        return f"Guau guau!"


class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        return f"Miau miau..."


class Vaca(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hablar(self):
        return f"Muuu!"


def main():
    a1 = Animal("Ornitorrinco")
    p1 = Perro("Sony")
    g1 = Gato("Wiskas")
    v1 = Vaca("Lechera")

    while True:
        print()
        print(f"1. Animal")
        print(f"2. Perro")
        print(f"3. Gato")
        print(f"4. Vaca")
        print(f"0. Salir")
        opc = int(input("Opción: "))

        match opc:
            case 1:
                print(a1)
                print(a1.hablar())
            case 2:
                print(p1)
                print(p1.hablar())
            case 3:
                print(g1)
                print(g1.hablar())
            case 4:
                print(v1)
                print(v1.hablar())
            case 0:
                print(f"Saliendo..")
                break
            case _:
                print(f"Opción invalida seleccionada.")


if __name__ == "__main__":
    main()