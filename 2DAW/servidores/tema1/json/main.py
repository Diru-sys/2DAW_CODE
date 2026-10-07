import json
RUTA = "alumno.json"

alumno = {
    "nombre": "Ana",
    "edad": 18,
    "notas": [7, 8, 9],
}

alumnos = [
    {
    "nombre": "Ana",
    "edad": 18,
    "notas": [7, 8, 9],
    },
    {
    "nombre": "Carlos",
    "edad": 20,
    "notas": [7, 8, 10],
    }
]

with open(RUTA, "w", encoding="utf-8") as fichero:
    json.dump(alumno, fichero, ensure_ascii=False)

with open(RUTA, "w", encoding="utf-8") as fichero:
    json.dump(alumnos, fichero, ensure_ascii=False, indent=4)