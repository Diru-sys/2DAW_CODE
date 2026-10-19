#Analisis de ventas semanales
dias = [
    "Lunes", "Martes", "Miércoles", "Jueves",
    "Viernes", "Sábado", "Domingo"
]
ventas = [1250, 980, 1430, 2100, 1750, 900, 2350]

ventaTotal = 0
ventaMedia = 0
for venta in ventas:
    ventaTotal = venta + ventaTotal
print(f"Venta Media: {int(ventaTotal / len(ventas))}")
print(f"Venta Total: {ventaTotal}")

