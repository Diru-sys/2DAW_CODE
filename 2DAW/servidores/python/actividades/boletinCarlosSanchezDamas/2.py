#Analisis de ventas semanales
dias = [
    "Lunes", "Martes", "Miércoles", "Jueves",
    "Viernes", "Sábado", "Domingo"
]
ventas = [1250, 980, 1430, 2100, 1750, 900, 2350]

ventaTotal = sum(ventas)
ventaMedia = int(ventaTotal / len(ventas))
mayores = []

diaNumMayor = max(ventas)
diaNumMenor = min(ventas)
diaMayor = ""
diaMenor = ""

contador1500 = 0

porcentaje = (diaNumMayor / ventaTotal) * 100

ventasOrdenadas = sorted(zip(ventas, dias), reverse=True)

for venta, dia in zip(ventas, dias):
    if venta > ventaMedia:
        mayores.append(dia)

    if venta == diaNumMayor:
        diaMayor = dia
    elif venta == diaNumMenor:
        diaMenor = dia

    if venta > 1500:
        contador1500 = contador1500 + 1

print(f"Venta Media: {ventaMedia}")
print(f"Venta Total: {ventaTotal}")
print(f"Dias cuyas ventas superan la media: {mayores}")
print(f"Dia con mayor número de ventas: {diaMayor}")
print(f"Dia con menor número de ventas: {diaMenor}")
print(f"Cuantos dias superan los 1500€ -> {contador1500}")
print(f"Porcentaje que corresponde al mejor dia: {porcentaje:.2f}%")

print(f" --DIAS ORDENADOS DE MAYOR A MENOR-- ")
for venta, dia in ventasOrdenadas:
    print(f"Dia: {dia} - Venta: {venta}€")

