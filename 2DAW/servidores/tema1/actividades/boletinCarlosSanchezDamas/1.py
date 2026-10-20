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


def procesar(movimiento, vehiculos, maximo, entradaCorrecta, salidaCorrecta):
    if movimiento == "entrada":
        if vehiculos < capacidad:
            entradaCorrecta = entradaCorrecta + 1
            vehiculos = vehiculos + 1

            if vehiculos > maximo:
                maximo = vehiculos
        else:
            print(f"Aparcamiento completo, entrada rechazada.")

    elif movimiento == "salida":
        if vehiculos > 0:
            vehiculos = vehiculos - 1
            salidaCorrecta = salidaCorrecta + 1
        else:
            print("Aparcamiento vacio, salida rechazada.")

    else:
        print("Movimiento no válido.")

    print(f"Coches dentro: {vehiculos} | Aparcamientos libres: {capacidad-vehiculos}")
    return vehiculos, maximo, entradaCorrecta, salidaCorrecta


print(f" --APARCAMIENTO-- ")
for movimiento in movimientos:
    vehiculos, maximo, entradaCorrecta, salidaCorrecta = procesar(movimiento, vehiculos, maximo, entradaCorrecta, salidaCorrecta)

opc = ""
while opc != "fin":
    print("Entrada para añadir entrada.")
    print("Salida para añadir salida.")
    print("Escribe 'fin' para salir")
    opc = input("Opción: ").lower().strip()
    if opc != "fin":
        vehiculos, maximo, entradaCorrecta, salidaCorrecta = procesar(opc, vehiculos, maximo, entradaCorrecta, salidaCorrecta)

print(f"Máximo de vehiculos dentro simultáneos: {maximo}")
print(f"Entradas validadas correctamente: {entradaCorrecta}")
print(f"Salidas validadas correctamente: {salidaCorrecta}")
print(f"Porcentaje de ocupación final del aparacamiento: {vehiculos * 100 / capacidad}%")