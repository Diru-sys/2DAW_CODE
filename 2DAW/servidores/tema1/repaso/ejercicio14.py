class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevoPrecio):
        if nuevoPrecio < 0:
            raise ValueError("El nuevo precio no puede ser inferior a 0.")
        else:
            self._precio = nuevoPrecio

    def aplicarDescuento(self, porcentaje):
        if porcentaje <= 0 or porcentaje > 100:
            raise ValueError("El porcentaje introducido es inválido.")
        else:
            descuento = self.precio * (porcentaje / 100)
            self.precio = self.precio - descuento

    def __str__(self):
        return f"Nombre del producto: {self.nombre} - Precio: {self.precio}"


def main():
    p1 = Producto("Patata", 70)
    print(f"Producto: {p1}")
    p1.aplicarDescuento(20)
    print(f"Precio del producto con descuento de 20% aplicado: {p1.precio}")


if __name__ == "__main__":
    main()