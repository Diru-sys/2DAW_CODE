# Control de ocupación de un aparcamiento
capacidad = 20
vehiculos = 0
maximo = 0
entradaCorrecta = 0
salidaCorrecta = 0
movimientos = [
    "entrada", "entrada", "entrada", "salida",
    "entrada", "entrada", "salida", "salida",
    "entrada", "entrada", "entrada", "entrada"
]

for movimiento in movimientos:
    if movimiento == "entrada" and vehiculos < capacidad:
        entradaCorrecta = entradaCorrecta + 1
        vehiculos = vehiculos + 1
        if vehiculos > maximo:
            maximo = vehiculos

    if movimiento == "salida" and vehiculos > 0:
        salidaCorrecta = salidaCorrecta + 1
        vehiculos = vehiculos - 1

    print(f"Coches dentro: {vehiculos} | Aparcamientos libres: {capacidad-vehiculos}")

print(f"Máximo de vehiculos dentro simultáneos: {maximo}")
print(f"Entradas validadas correctamente: {entradaCorrecta}")
print(f"Salidas validadas correctamente: {salidaCorrecta}")

porcentajeOcupacion = (vehiculos * 100) / capacidad
print(f"Porcentaje de ocupación final del aparacamiento: {porcentajeOcupacion}%")