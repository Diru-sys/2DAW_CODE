class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"Nombre del alumno {self.nombre} - Nota: {self.nota}"


def main():
    a1 = Alumno("Carlos", 9)
    a2 = Alumno("Lucía", 7)
    a3 = Alumno("José", 4)

    lista = (a1, a2, a3)
    print(f"Nombre de los alumnos:")
    for alumno in lista:
        print(alumno)

if __name__ == "__main__":
    main()    