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

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        if valor >= 0:
            self._saldo = valor
        else:
            raise ValueError("No es posible asignar un saldo menor que 0.")

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

try:
    cuenta1.retirar(100)
    cuenta1.retirar(1000)
except ValueError as e:
    print(f"Error: {e}")

try:
    cuenta2.ingresar(20)
except ValueError as e:
    print(f"Error: {e}")

print(cuenta1)
print(cuenta2)