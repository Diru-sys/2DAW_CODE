"""
Crea una lista con 8 notas.

Muestra la media, la máxima y la mínima.
Ordénala de mayor a menor.
Con una comprehension, crea una lista solo con los aprobados (5 o más).
Cuenta cuántos suspensos hay.
"""
notas = [4,10,4,2,8,9,5,7]

media = sum(notas) / len(notas)
print(f"Media: {media:.2f}")

print(f"Max: {max(notas)}")

print(f"Min: {min(notas)}")

notas.sort(reverse=True)
print(f"Notas ordenadas de mayor a menor: {notas}")

aprobados = [nota for nota in notas if nota >= 5]
print(f"Aprobados: {aprobados}")

contadorSuspensos = 0
for nota in notas:
    if nota < 5:
        contadorSuspensos += 1
print(f"Suspensos totales: {contadorSuspensos}")