#Creación de la clase alumno
class Alumno:
    def __init__(self, nombre, edad):
        """Constructor de la clase Alumno."""
        self.nombre = nombre
        self.edad = edad
        self.notas = []

    def __str__(self):
        """Método para mostrar la instancia de esta clase."""
        return f"Nombre del alumno: {self.nombre} | Edad: {self.edad} | Notas: {self.notas}"

    def añadirNota(self, nota):
        """Método para añadir una nueva nota a la lista de notas del alumno."""
        self.notas.append(nota)

    def media(self):
        """Calcular la media del alumno apartir de la lista de sus notas."""
        return sum(self.notas) / len(self.notas)

    def cambiarNombre(self,nombreNuevo):
        """Método para cambiar el nombre del alumno."""
        self.nombre = nombreNuevo

    def mayorEdad(self):
        """Comprobar que el alumno es mayor de 18 años de edad."""
        if self.edad >= 18:
            return f"Este alumno de nombre {self.nombre} es mayor de edad."
        else:
            return f"El alumno de nombre {self.nombre} es menor de edad."
    
    
#Crear instancia de la clase Alumno
alumno1 = Alumno("Carlos", 20)

#Añadir notas al objeto ana
alumno1.añadirNota(8)
alumno1.añadirNota(5)
alumno1.añadirNota(6)

#Calcular media
print(f"{alumno1.media():.2f}")

#Mostrar si es mayor de edad
print(alumno1.mayorEdad())

#Cambiar el nombre del alumno
print("Cambiamos el nombre del alumno de Carlos -> Ana Luna")
alumno1.cambiarNombre("Ana Luna")

#Objeto ana
print(alumno1)