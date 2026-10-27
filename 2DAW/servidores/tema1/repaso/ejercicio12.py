class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base * self.altura)


def main():
    r1 = Rectangulo(3,4)
    r2 = Rectangulo(9,2)

    print(f"Area del rectángulo 1: {r1.area():.2f}")
    print(f"Area del rectángulo 2: {r2.area():.2f}")
    print(f"Perímetro del rectángulo 1: {r1.perimetro():.2f}")
    print(f"Perímetro del rectángulo 2: {r2.perimetro():.2f}")


if __name__ == "__main__":
    main()