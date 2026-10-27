class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevoSaldo):
        if nuevoSaldo < 0:
            raise ValueError("El nuevo saldo no puede ser menor que 0.")
        else:
            self._saldo = nuevoSaldo

    def ingresar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a ingresar es menor o igual que 0.")
        else:
            self.saldo = self.saldo + cantidad
            print(f"Dinero ingresado correctamente.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe de ser mayor o igual que 0.")
        else:
            self.saldo = self.saldo - cantidad
            print(f"Dinero retirado correctamente.")

    def __str__(self):
        return f"Propietario de la cuenta: {self.titular} | Saldo: {self.saldo}"


def main():
    cuenta = Cuenta("Carlos", 5000)
    while True:
        print()
        print(f"1. Mostrar mi cuenta")
        print(f"2. Ingresar")
        print(f"3. Retirar")
        print(f"0. Cerrar")
        opc = int(input("Opción: "))

        match opc:
            case 1:
                print(cuenta)
            case 2:
                dinero = int(input("Dinero a ingresar: "))
                cuenta.ingresar(dinero)
            case 3:
                dinero = int(input("Dinero a retirar: "))
                cuenta.retirar(dinero)
            case 0:
                print(f"Saliendo...")
                break
            case _:
                print("Opción introducida inválida.")

if __name__ == "__main__":
    main()