#EJERCICIO CLASE 1
def ejercicio1():
    print(" --EJERCICIO 1-- ")
    temperaturas = []
    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    for i in range(7):
        temperaturas.append(int(input("Introduce una temperatura: ")))

    print()
    #Imprime todas las temperaturas
    print("Todas las temperaturas:")
    print(temperaturas)

    #Temperatura máxima
    print("Temperatura máxima")
    print(max(temperaturas))

    #Temperatura mínima
    print("Temperatura mínima")
    print(min(temperaturas))

    #Temperatura media
    print("Temperatura media")
    media = ((sum(temperaturas) / len(temperaturas)))
    print(media)

    #Cuántos dias tuvieron una temperatura superior a la media
    print("Cuantos dias tuvieron una temperatura superior a la media")
    temperaturaSuperior = [t for t in temperaturas if t > media]
    print(len(temperaturaSuperior))

    #Cuántos días tuvieron una temperatura inferior a 10 °C
    print("Cuántos días tuvieron una temperatura inferior a 10 °C")
    temperaturaInferior = [t for t in temperaturas if t < 10]
    print(len(temperaturaInferior))

    #AMPLIACIÓN - Muestra también qué día de la semana tuvo la temperatura más alta
    print("Muestra también qué día de la semana tuvo la temperatura más alta")
    max = max(temperaturas)
    maxPosicion = temperaturas.index(max)
    diaCaluroso = dias[maxPosicion]

    print(diaCaluroso)


#EJERCICIO 2
def ejercicio2():
    print(" --Ejercicio  2-- ")



#EJERCICIO 3
def ejercicio3():
    print(" --Ejercicio 3-- ")
    notas = [7.5, 4.2, 8.1, 3.7, 5.0, 9.3, 2.8, 6.4, 4.9, 7.2]
    aprobados = []
    suspensos = []

    aprobados = [a for a in notas if a >= 5]
    suspensos = [s for s in notas if s < 5]

    #La lista de notas original
    print(notas)

    #La lista de aprobados
    print(aprobados)

    #La lista de suspensos
    print(suspensos)

    #El número de aprobados
    print(len(aprobados))

    #El número de suspensos
    print(len(suspensos))

    #El porcentaje de aprobados
    porcentaje = (len(aprobados) * 100) / len(notas)
    print(porcentaje)

    #La nota media de la clase
    print((sum(notas) / len(notas)))


#EJERCICIO 4
def ejercicio4():
    print(" --Ejercicio  4-- ")



#EJERCICIO 5
def ejercicio5():
    print(" --Ejercicio  5-- ")
    jugadores = ["Ana", "Luis", "Marta", "Pedro", "Lucía"]
    puntos = [125, 80, 150, 95, 110]
    relacion = {
        jugadores[0] : puntos[0],
        jugadores[1] : puntos[1],
        jugadores[2] : puntos[2],
        jugadores[3] : puntos[3],
        jugadores[4] : puntos[4]
    }
    #Mostrar relacion
    print(relacion)

    
ejercicio5()