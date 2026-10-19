# Control de ocupación de un aparcamiento
capacidad = 20
vehiculos = 0
max = 0
entradaCorrecta = 0
salidaCorrecta = 0
movimientos = [
    "entrada", "entrada", "entrada", "salida",
    "entrada", "entrada", "salida", "salida",
    "entrada", "entrada", "entrada", "entrada"
]

for movimiento in movimientos:
    if movimiento == "entrada" and vehiculos < capacidad:
        max = max + 1
        entradaCorrecta = entradaCorrecta + 1
        vehiculos = vehiculos + 1

    if movimiento == "salida" and vehiculos < capacidad and vehiculos is not 0:
        salidaCorrecta = salidaCorrecta + 1
        vehiculos = vehiculos - 1

    print(f"Coches dentro: {vehiculos} | Aparcamientos libres: {capacidad-vehiculos}")

print(f"Máximo de vehiculos dentro simultáneos: {max}")
print(f"Entradas validadas correctamente: {entradaCorrecta}")
print(f"Salidas validadas correctamente: {salidaCorrecta}")

porcentajeOcupacion = (vehiculos * 100) / 20
print(f"Porcentaje de ocupación final del aparacamiento: {porcentajeOcupacion}")