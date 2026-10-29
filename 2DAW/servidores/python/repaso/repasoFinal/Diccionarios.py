"""
Crea un diccionario {producto: unidades} con 4 productos.

Añade uno nuevo y cambia las unidades de otro.
Elimina uno con del o pop.
Recórrelo mostrando producto: unidades.
Muestra solo los que tengan menos de 5 unidades.
"""
diccionario = {
    "manzana": 5,
    "pera": 10,
    "rabano": 2,
    "patata": 99,
    "coliflor": 1
}

diccionario["zanahoria"] = 25

diccionario["manzana"] = 45

diccionario.pop("patata")

for clave, valor in diccionario.items():
    print(f"Producto: {clave} | Unidades: {valor}")

for clave, valor in diccionario.items():
    if valor < 5:
        print(f"Producto: {clave}")