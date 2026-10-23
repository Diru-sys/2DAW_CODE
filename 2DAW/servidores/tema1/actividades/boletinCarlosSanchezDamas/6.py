pedidos = [
    {
        "numero": 101,
        "cliente": "Ana",
        "importe": 125.50,
        "estado": "pendiente"
    },
    {
        "numero": 102,
        "cliente": "Luis",
        "importe": 89.90,
        "estado": "enviado"
    }
]

estados = ["pendiente", "enviado", "entregado", "cancelado"]

def buscar_pedido(pedidos, numero):
    for pedido in pedidos:
        if pedido["numero"] == numero:
            return pedido
    return None

def registrar_pedido(pedidos):
    numero = int(input("Número del pedido: "))

    if buscar_pedido(pedidos, numero) is not None:
        print(f"Ese número ya existe.")
        return

    cliente = input("Cliente: ")
    importe = float(input("Importe: "))

    pedido = {
        "numero": numero,
        "cliente": cliente,
        "importe": importe,
        "estado": "pendiente"
    }

    pedidos.append(pedido)
    print(f"Pedido registrado.")

def cambiar_estado(pedidos):
    numero = int(input("Número del pedido: "))
    pedido = buscar_pedido(pedidos, numero)
    if pedido is None:
        print(f"Pedido no encontrado.")
        return

    estado = input("Nuevo estado: ").lower()

    if estado in estados:
        pedido["estado"] = estado
        print(f"Estado actualizado.")
    else:
        print(f"Estado no válido.")

def mostrar_pendientes(pedidos):
    for pedido in pedidos:
        if pedido["estado"] == "pendiente":
            print(pedido)

def mostrar_cliente(pedidos):
    cliente = input("Nombre del cliente: ").lower()

    for pedido in pedidos:
        if pedido["cliente"].lower() == cliente:
            print(pedido)

def importe_total(pedidos):
    total = 0

    for pedido in pedidos:
        total += pedido["importe"]

    print(f"Importe total:", round(total, 2), "€")

def pedido_mayor(pedidos):
    if len(pedidos) == 0:
        print(f"No hay pedidos.")
        return

    mayor = pedidos[0]

    for pedido in pedidos:
        if pedido["importe"] > mayor["importe"]:
            mayor = pedido
    print(f"Pedido de mayor importe:", mayor)

def contar_estados(pedidos):
    for estado in estados:
        cantidad = 0

        for pedido in pedidos:
            if pedido["estado"] == estado:
                cantidad += 1
        print(f"{estado} : {cantidad}")

def main():
    while True:
        print("\n1. Registrar pedido")
        print("2. Buscar pedido")
        print("3. Cambiar estado")
        print("4. Mostrar pendientes")
        print("5. Mostrar pedidos de un cliente")
        print("6. Importe total")
        print("7. Pedido de mayor importe")
        print("8. Contar pedidos por estado")
        print("9. Salir")

        opcion = int(input("Opción: "))

        match opcion:
            case 1:
                registrar_pedido(pedidos)
            case 2:
                numero = int(input("Número: "))
                pedido = buscar_pedido(pedidos, numero)

                if pedido is not None:
                    print(pedido)
                else:
                    print(f"Pedido no encontrado.")
            case 3:
                cambiar_estado(pedidos)
            case 4:
                mostrar_pendientes(pedidos)
            case 5:
                mostrar_cliente(pedidos)
            case 6:
                importe_total(pedidos)
            case 7:
                pedido_mayor(pedidos)
            case 8:
                contar_estados(pedidos)
            case 9:
                print(f"Saliendo...")
                break
            case _:
                print(f"Opción incorrecta.")


if __name__ == "__main__":
    main()