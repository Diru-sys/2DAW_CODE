alumnos = [
    {
        "nombre": "Ana",
        "notas": [7, 8, 9],
    },
    {
        "nombre": "Luis",
        "notas": [5, 6, 7],
    },
]

#Para cada alumno, la nota media
def media():
    for alumno in alumnos:
        notas = alumno["notas"]
        media = sum(notas) / len(notas)
        alumnoNombre = alumno["nombre"]
        print(f"La media del alumno {alumnoNombre} es de : {media}")

#El nombre de la nota mas alta del primer alumno
def alta():
    notaMaxima = 0
    mejorAlumno = None

    for nombre in alumnos:
        notaActual = max(nombre["notas"])
        if notaActual > notaMaxima:
            notaMaxima = notaActual
            mejorAlumno = nombre["nombre"]

    print(f"La nota máxima de todos los alumnos es: {notaMaxima} y pertenece a {mejorAlumno}")