class Jugador:
    def __init__(self, nombreJugador, raza, experiencia):
        self.nombreJugador = nombreJugador
        self.raza = raza
        self.experiencia = experiencia

    def atacar(self, jugador):
        return f"El jugador {self.nombreJugador} está atacando al jugador {jugador} de forma básica."

    def __str__(self):
        return f"El jugador se llama: {self.nombreJugador}, es de una raza tipo: {self.raza} y tiene {self.experiencia} puntos de experiencia."


class Mago(Jugador):
    def __init__(self, nombreJugador, arma, raza, experiencia):
        super().__init__(nombreJugador, raza, experiencia)
        self.arma = arma

    def atacar(self, jugador):
        return f"El jugador {self.nombreJugador} está atacando al jugador {jugador} con su {self.arma}."

    def hechizoHielo(self):
        return f"El mago ataca con su hechizo de hielo a todas las criaturas cercanas a 30 pies."

    def __str__(self):
        return f"El jugador se llama: {self.nombreJugador}, es de una raza tipo: {self.raza}, tiene esta arma: {self.arma} y {self.experiencia} puntos de experiencia."


class Barbaro(Jugador):
    def __init__(self, nombreJugador, arma, raza, experiencia):
        super().__init__(nombreJugador, raza, experiencia)
        self.arma = arma

    def atacar(self, jugador):
        return f"El jugador {self.nombreJugador} está atacando al jugador {jugador} con su {self.arma}."

    def rabia(self):
        return f"El bárbaro entra en su modo de rabia y asusta a todas las criaturas a 15 pies cerca de el"

    def __str__(self):
        return f"El jugador se llama: {self.nombreJugador}, es de una raza tipo: {self.raza}, tiene esta arma: {self.arma} y {self.experiencia} puntos de experiencia."


jugador1 = Jugador("Carlos", "Golem", 60)

jugador2 = Mago("Álvaro", "Bastón de magia oscura", "Enano", 6767)

jugador3 = Barbaro("Hugo", "Hacha", "Orco", 2000)

print(f" ===JUGADORES=== ")
print(jugador1)
print(jugador2)
print(jugador3)
print()
print(f" ===RONDA DE ATAQUE=== ")
print(jugador1.atacar(jugador2.nombreJugador))
print(jugador2.atacar(jugador3.nombreJugador))
print(jugador1.atacar(jugador3.nombreJugador))
print()
print(f" ===RONDA ESPECIAL=== ")
print(jugador2.hechizoHielo())
print(jugador3.rabia())
