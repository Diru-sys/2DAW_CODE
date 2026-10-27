class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self._nota = nota

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nuevaNota):
        if nuevaNota < 0:
            raise ValueError("La nota no puede ser menor que 0.")
        else:
            self._nota = nuevaNota

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