"""
Con la clase Cuenta del ejercicio anterior:

Crea guardar_cuentas(lista), que escribe cuentas.json (convierte cada objeto en diccionario).
Crea cargar_cuentas(), que lee el JSON y devuelve una lista de objetos Cuenta.
Si el archivo no existe, devuelve una lista vacía (FileNotFoundError).
Prueba guardando 3 cuentas, cargándolas y mostrándolas.
Gestión de cuentas bancarias con persistencia JSON utilizando pathlib y rutas relativas.
"""
import json
from pathlib import Path

RUTA = Path(__file__).resolve().parent
RUTACUENTAS = RUTA / "cuentas.json"

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

    def toDict(self):
        pass

    @classmethod
    def fromDict(cls, datos):
        pass

    def __str__(self):
        return f"Titular de la cuenta: {self.titular} | Saldo: {self.saldo}"
