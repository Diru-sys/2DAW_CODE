"""
Crea una lista con 6 alumnos, cada uno {"nombre", "curso", "nota"}.

Recorre la lista con un for y muestra nombre - nota - Aprobado/Suspenso (usa un if).
Muestra solo los alumnos del curso "1A".
Calcula la nota media de cada curso.
Muestra el mejor alumno con max y una lambda.
"""

alumnos = [
    {"nombre": "Carlos", "curso": "1A", "nota": 8},
    {"nombre": "Lucía", "curso": "1A", "nota": 6},
    {"nombre": "Mario", "curso": "1A", "nota": 4},
    {"nombre": "Ana", "curso": "2A", "nota": 9},
    {"nombre": "Pedro", "curso": "2A", "nota": 3},
    {"nombre": "Laura", "curso": "2A", "nota": 7}
]

for alumno in alumnos:
    if alumno["nota"] >= 5:
        print(f"Nombre: {alumno["nombre"]} | Nota: {alumno["nota"]} | Aprobado")
    else:
        print(f"Nombre: {alumno["nombre"]} | Nota: {alumno["nota"]} | Suspenso")

print() #-------------------

for alumno in alumnos:
    if alumno["curso"] == "1A":
        print(alumno)

print() #-------------------

sumatorioNotas1A = 0
contadorNotas1A = 0
sumatorioNotas2A = 0
contadorNotas2A = 0

for alumno in alumnos:
    if alumno["curso"] == "1A":
        contadorNotas1A = contadorNotas1A + 1
        sumatorioNotas1A = sumatorioNotas1A + alumno["nota"]
    elif alumno["curso"] == "2A":
            contadorNotas2A = contadorNotas2A + 1
            sumatorioNotas2A = sumatorioNotas2A + alumno["nota"]
print(f"Media del curso 1A: {sumatorioNotas1A / contadorNotas1A:.2f}")
print(f"Media del curso 2A: {sumatorioNotas2A / contadorNotas2A:.2f}")

print() #-------------------

mejorAlumno = max(alumnos, key=lambda alumno: alumno["nota"])
print(f"Nombre del mejor alumno: {mejorAlumno["nombre"]} | Curso: {mejorAlumno["curso"]} | Nota: {mejorAlumno["nota"]}")
