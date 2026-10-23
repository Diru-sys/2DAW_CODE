import csv
import json


def cargar_productos():
    productos = []
    with open("productos.csv", "r", encoding="utf-8") as fichero:
        lector = csv.DictReader(fichero)

        for fila in lector:
            producto = {
                "codigo": fila["codigo"],
                "nombre": fila["nombre"],
                "precio": float(fila["precio"]),
                "stock": int(fila["stock"])
            }
            productos.append(producto)
    return productos

def mostrar_productos(productos):
    for producto in productos:
        print(producto)

def mostrar_stock_bajo(productos):
    for producto in productos:
        if producto["stock"] < 5:
            print(producto)

def valor_inventario(productos):
    total = 0

    for producto in productos:
        total += producto["precio"] * producto["stock"]

    print(f"Valor total del inventario: {round(total, 2)}€")

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto
    return None

def modificar_stock(productos):
    codigo = input("Código del producto: ")
    producto = buscar_producto(productos, codigo)

    if producto is not None:
        stock = int(input("Nuevo stock: "))

        if stock >= 0:
            producto["stock"] = stock
            print(f"Stock actualizado.")
        else:
            print(f"El stock no puede ser negativo.")
    else:
        print(f"Producto no encontrado.")

def guardar_json(productos):
    with open("productos.json", "w", encoding="utf-8") as fichero:
        json.dump(productos, fichero, indent=4, ensure_ascii=False)

    print(f"Datos guardados en productos.json")

def main():
    productos = cargar_productos()

    while True:
        print("\n1. Mostrar productos")
        print("2. Mostrar productos con stock inferior a 5")
        print("3. Calcular valor del inventario")
        print("4. Buscar producto por código")
        print("5. Modificar stock")
        print("6. Guardar en JSON")
        print("7. Salir")
        opc = int(input("Opción: "))

        match opc:
            case 1:
                mostrar_productos(productos)
            case 2:
                mostrar_stock_bajo(productos)
            case 3:
                valor_inventario(productos)
            case 4:
                codigo = input("Código: ")
                producto = buscar_producto(productos, codigo)

                if producto is not None:
                    print(producto)
                else:
                    print("Producto no encontrado.")
            case 5:
                modificar_stock(productos)
            case 6:
                guardar_json(productos)
            case 7:
                print(f"Saliendo...")
                break
            case _:
                print("Opción incorrecta.")


if __name__ == "__main__":
    main()
