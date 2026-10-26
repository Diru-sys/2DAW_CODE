
class Vehiculo:
    def __init__(self, matricula, marca, modelo, precio_dia):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.precio_dia = precio_dia
        self.disponible = True

    def alquilar(self):
        if self.disponible:
            self.disponible = False
            print(f"Vehículo alquilado.")
        else:
            print(f"El vehículo no está disponible.")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Vehículo devuelto.")
        else:
            print(f"El vehículo ya estaba disponible.")

    def mostrar(self):
        print(f"Matrícula: {self.matricula}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio por día: {self.precio_dia}€")
        print(f"Disponible: {self.disponible}")

    def calcular_precio(self, dias):
        return self.precio_dia * dias


class EmpresaAlquiler:
    def __init__(self):
        self.vehiculos = []

    def añadir_vehiculo(self, vehiculo):
        if self.buscar_vehiculo(vehiculo.matricula) is None:
            self.vehiculos.append(vehiculo)
            print(f"Vehículo añadido.")
        else:
            print(f"La matrícula ya existe.")

    def buscar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                return vehiculo
        return None

    def mostrar_vehiculos(self):
        for vehiculo in self.vehiculos:
            vehiculo.mostrar()
            print()

    def mostrar_disponibles(self):
        for vehiculo in self.vehiculos:
            if vehiculo.disponible:
                vehiculo.mostrar()
                print()

    def alquilar_vehiculo(self, matricula):
        vehiculo = self.buscar_vehiculo(matricula)

        if vehiculo is not None:
            vehiculo.alquilar()
        else:
            print(f"Vehículo no encontrado.")

    def devolver_vehiculo(self, matricula):
        vehiculo = self.buscar_vehiculo(matricula)

        if vehiculo is not None:
            vehiculo.devolver()
        else:
            print(f"Vehículo no encontrado.")

    def consultar_precio(self, matricula, dias):
        vehiculo = self.buscar_vehiculo(matricula)

        if vehiculo is not None:
            if vehiculo.disponible:
                precio = vehiculo.calcular_precio(dias)
                print(f"Precio del alquiler:", precio, "€")
            else:
                print(f"El vehículo no está disponible.")
        else:
            print(f"Vehículo no encontrado.")

    def precio_mas_alto(self):
        if len(self.vehiculos) == 0:
            print(f"No hay vehículos.")
            return

        mayor = self.vehiculos[0]

        for vehiculo in self.vehiculos:
            if vehiculo.precio_dia > mayor.precio_dia:
                mayor = vehiculo

        print(f"Vehículo con mayor precio diario:")
        mayor.mostrar()


def main():
    empresa = EmpresaAlquiler()
    empresa.añadir_vehiculo(
        Vehiculo("1234ABC", "Toyota", "Corolla", 35)
    )
    empresa.añadir_vehiculo(
        Vehiculo("5678DEF", "Seat", "León", 40)
    )
    empresa.añadir_vehiculo(
        Vehiculo("9012GHI", "Ford", "Focus", 30)
    )

    while True:
        print("\n1. Añadir vehículo")
        print("2. Mostrar vehículos")
        print("3. Mostrar vehículos disponibles")
        print("4. Alquilar vehículo")
        print("5. Devolver vehículo")
        print("6. Consultar precio de alquiler")
        print("7. Mostrar vehículo más caro por día")
        print("8. Salir")

        opc = int(input("Opción: "))

        match opc:
            case 1:
                matricula = input("Matrícula: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                precio = float(input("Precio por día: "))

                if precio > 0:
                    vehiculo = Vehiculo(matricula, marca, modelo, precio)
                    empresa.añadir_vehiculo(vehiculo)
                else:
                    print(f"El precio debe ser positivo.")

            case 2:
                empresa.mostrar_vehiculos()
            case 3:
                empresa.mostrar_disponibles()
            case 4:
                matricula = input("Matrícula: ")
                empresa.alquilar_vehiculo(matricula)
            case 5:
                matricula = input("Matrícula: ")
                empresa.devolver_vehiculo(matricula)
            case 6:
                matricula = input("Matrícula: ")
                dias = int(input("Número de días: "))

                if dias > 0:
                    empresa.consultar_precio(matricula, dias)
                else:
                    print("Los días deben ser positivos.")
            case 7:
                empresa.precio_mas_alto()
            case 8:
                print("Saliendo...")
                break
            case _:
                print("Opción incorrecta.")


if __name__ == "__main__":
    main()