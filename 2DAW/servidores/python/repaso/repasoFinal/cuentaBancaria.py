"""
Crea la clase Cuenta con titular y saldo.

El saldo es una property y no puede ser negativo (ValueError).
Métodos: ingresar(cantidad), retirar(cantidad) y __str__.
retirar lanza ValueError si no hay saldo suficiente.
Crea 2 cuentas, haz operaciones y captura los errores con try/except.
"""
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad
        print("Saldo ingresado correctamente.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("La cantidad a retirar es mayor al saldo.")
        else:
            self.saldo = self.saldo - cantidad
            print("Saldo retirado correctamente.")

    def __str__(self):
        return f"Titular de la cuenta: {self.titular} | Saldo: {self.saldo}"

cuenta1 = Cuenta("Carlos", 500)
cuenta2 = Cuenta("David", 1000)

cuenta1.retirar(100)
cuenta2.ingresar(20)

print(cuenta1)
print(cuenta2)