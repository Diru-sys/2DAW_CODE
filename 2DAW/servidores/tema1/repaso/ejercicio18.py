class Figura:
    def __init__(self):
        pass

    def area(self):
        return f"Las figuras no tienen area predifinida ni calculable."

    def __str__(self):
        return f"Las figuras no tienen forma predifinida."


class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def area(self):
        return f"El area de un circulo es PI por su radio: {self.radio * 3.1416}"

    def __str__(self):
        return f"Esta figura es un circulo."


class Cuadrado(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self):
        return f"El area de un cuadrado es lado al cuadrado: {self.altura*self.altura}"

    def  __str__(self):
        return f"Esta figura es un cuadrado de base: {self.base} y altura: {self.altura}"


class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__()
        self.base =  base
        self.altura = altura

    def area(self):
        return f"El area de un triangulo es base * altura / 2 -> {(self.base * self.altura)/2}"

    def __str__(self):
        return f"Esta figura es un triangulo de base: {self.base} y altura: {self.altura}"


def main():
    fig = Figura()
    cir = Circulo(4)
    cua = Cuadrado(4, 5)
    tri = Triangulo(2, 9)

    print(f"{fig}\n{fig.area()}")
    print()
    print(f"{cir}\n{cir.area()}")
    print()
    print(f"{cua}\n{cua.area()}")
    print()
    print(f"{tri}\n{tri.area()}")


if __name__ == "__main__":
    main()