class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre de la persona: {self.nombre} - Edad: {self.edad}"


class Alumno(Persona):
    def __init__(self, nombre, edad, nota):
        super().__init__(nombre, edad)
        self.nota = nota

    def __str__(self):
        return f"Nombre de la persona: {self.nombre} - Edad: {self.edad} - Nota: {self.nota}"


class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def __str__(self):
        return f"Nombre de la persona: {self.nombre} - Edad: {self.edad} - Asignatura impartida: {self.asignatura}"


def main():
    p1 = Persona("Manolo", 45)
    a1 = Alumno("Carlos", 20, 9)
    pro1 = Profesor("Joaquín", 39, "Matemáticas")
    print(f"Prints: ")
    print(p1)
    print(a1)
    print(pro1)


if __name__ == "__main__":
    main()