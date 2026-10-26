class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo


    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Ingreso realizado.")
        else:
            print(f"La cantidad debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print(f"La cantidad debe ser positiva.")
        elif cantidad > self.saldo:
            print(f"Saldo insuficiente.")
        else:
            self.saldo -= cantidad
            print(f"Retirada realizada.")

    def mostrar_saldo(self):
        print(f"Saldo: {round(self.saldo, 2)}€")

    def mostrar_datos(self):
        print(f"Número: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {round(self.saldo, 2)}€")

    def transferir(self, destino, cantidad):
        if cantidad <= 0:
            print(f"La cantidad debe ser positiva.")
        elif cantidad > self.saldo:
            print(f"Saldo insuficiente.")
        else:
            self.saldo -= cantidad
            destino.saldo += cantidad
            print(f"Transferencia realizada.")

def main():
    cuentas = [
        CuentaBancaria("001", "Ana", 500),
        CuentaBancaria("002", "Luis", 1200),
        CuentaBancaria("003", "Alejandro", 800),
        CuentaBancaria("004", "Marta", 2000),
        CuentaBancaria("005", "Lucía", 1500)
    ]

    cuentas[0].ingresar(100)
    cuentas[1].retirar(50)
    cuentas[2].transferir(cuentas[0], 200)

    total = 0
    mayor = cuentas[0]

    print(f"DATOS DE LAS CUENTAS")

    for cuenta in cuentas:
        cuenta.mostrar_datos()
        print()

        total += cuenta.saldo

        if cuenta.saldo > mayor.saldo:
            mayor = cuenta

    print(f"Cuenta con mayor saldo:")
    mayor.mostrar_datos()

    print(f"\nDinero total: {round(total, 2)} €")


if __name__ == "__main__":
    main()