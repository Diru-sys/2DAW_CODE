#ACTIVIDAD 1
def actividad1():
    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    temperaturas = [];
    for i in range(7):
        temperatura = int(input("Introduce una temperatura: "))
        temperaturas.append(temperatura)
        
    media = int(sum(temperaturas) / len(temperaturas))

    diasMedia = 0
    dias10 = 0

    diaMax = max(temperaturas)
    indiceMax = temperaturas.index(diaMax)
    diaSemanaMax = dias[indiceMax]

    for temperatura in temperaturas:
        if temperatura > media:
            diasMedia += 1
        if temperatura < 10:
            dias10 += 1

    #Todas las temperaturas registradas
    print("Todas las temperaturas: ", temperaturas)
    #Temperatura máxima
    print("Temperatura máxima: ", diaMax)
    #Temperatura minima
    print("Temperatura minima: ", min(temperaturas))
    #Temperatura media
    print("Temperatura media: ", media)
    #Cuantos dias son superior a la media
    print("Dias que son superior a la media de temperatura: ", diasMedia)
    #Cuantos dias son inferior a 10
    print("Dias que son inferior a 10º: ", dias10)
    #Resultado de la amplicación
    print(f"El dia con la temperatura más alta fue el {diaSemanaMax} con {diaMax} ºC")


#ACTIVIDAD 2
def actividad2():
    compra = []
    numProductos = 0

    while True:
        producto = input("Introduce un producto a la lista (usa fin para terminar): ")
        if producto == "fin":
            break
        #AMPLICACIÓN
        if producto in compra:
            print(f"El producto {producto} ya está en la lista.")
        else:
            compra.append(producto)
            numProductos += 1


    #Mostrar la lista entera
    print("Lista de la compra: ", compra)
    #Muestra el número de productos introducidos
    print("Número de productos introducidos: ", numProductos)
    #Solicita al usuario el nombre de un producto que quiera eliminar
    productoOut = input("Introduce el nombre de un producto que quieras eliminar: ")
    #Si el producto existe eliminalo
    if productoOut in compra:
        compra.remove(productoOut)
    else: #Si el producto no existe, muestra un mensaje indicandolo
        print(f"El producto {productoOut} no existe.")
    #Muestra la lista resultante
    print("Lista resultante de productos final: ", compra)


#ACTIVIDAD 3
def actividad3():
    notas = [7.5, 4.2, 8.1, 3.7, 5.0, 9.3, 2.8, 6.4, 4.9, 7.2]
    aprobados = []
    suspensos = []

    for i in notas:
        if i >= 5.0:
            aprobados.append(i)
        else:
            suspensos.append(i)
    
    numAprobados = len(aprobados)
    numSuspensos = len(suspensos)
    porcentajeAprobados = (numAprobados / len(notas)) * 100
    media = int(sum(notas) / len(notas))

    #Lista de notas original
    print("Lista de notas orignal: ",notas)
    #Lista de aprobados
    print("Lista de aprobados: ",aprobados)
    #Lista de suspensos
    print("Lista de suspensos: ",suspensos)
    #Número de aprobados
    print("Número de aprobados: ",numAprobados)
    #Número de suspensos
    print("Número de suspensos: ",numSuspensos)
    #Porcentaje de aprobados
    print("Porcentaje de aprobados: ",porcentajeAprobados,"%")
    #La nota media de la clase
    print("Nota media de la clase: ",media)


#ACTIVIADAD 4
def actividad4():
    accesos = [12, 7, 5, 12, 8, 7, 15, 5, 9, 12, 3, 8]
    usuarios = []
    accesosRepetidos = 0

    for i in accesos:
        if i in usuarios:
            accesosRepetidos += 1
        elif i not in usuarios:
            usuarios.append(i)

    #Mostrar lista de accesos
    print("Lista de accesos: ",accesos)
    #Mostrar lista de usuarios
    print("Lista de usuarios: ",usuarios)
    #Número total de accesos
    print(f"Número total de accesos: {len(accesos)}")
    #Número total de usuarios
    print(f"Número total de usuarios: {len(usuarios)}")
    #Número total de accesos repetidos
    print("Número total de accesos repetidos: ", accesosRepetidos)


#ACTIVIDAD 5
def actividad5():
    jugadores = ["Ana", "Luis", "Marta", "Pedro", "Lucía"]
    puntos = [125, 80, 150, 95, 110]
    media = int(sum(puntos)/len(puntos))
    contadorMedia = 0
    jugadoresMedia = []

    #Mostrar inicialmente
    for pos in range(len(jugadores)):
        print(f"{jugadores[pos]} - {puntos[pos]} puntos")

    #El jugador con más puntuación
    maxPuntos = max(puntos)
    maxJugador = puntos.index(maxPuntos)
    mayorJugador = jugadores[maxJugador]
    print(f"El jugador con más puntos es {mayorJugador} y tiene {maxPuntos} puntos.")
    #El jugador con menor puntuación
    minPuntos = min(puntos)
    minJugador = puntos.index(minPuntos)
    menorJugador = jugadores [minJugador]
    print(f"El jugador con menos puntos es {menorJugador} y tiene {minPuntos} puntos.")
    #La puntuación media
    print(f"La puntuación media es de: {media} puntos.")
    #Los jugadores que tienen una puntuación superior a la media
    for jugador, punto in zip(jugadores, puntos):
        if punto > media:
            contadorMedia += 1
            jugadoresMedia.append(jugador)
    print(f"Los jugadores por encima de la media son: {jugadoresMedia} y son en total: {contadorMedia}")
    #Clasificación ordenada
    print(" --Lista ordenada-- ")
    numero = len(puntos)
    for i in range(numero):
        for j in range(numero - 1):
            if puntos[j] < puntos[j + 1]:
                auxiliarPuntos = puntos[j]
                puntos[j] = puntos[j + 1]
                puntos[j + 1] = auxiliarPuntos

                auxiliarJugador = jugadores[j]
                jugadores[j] = jugadores[j + 1]
                jugadores[j + 1] = auxiliarJugador
    for pos in range(len(jugadores)):
        print(f"{pos + 1}. {jugadores[pos]} - {puntos[pos]} puntos")


#ACTIVIDAD FINAL
def actividadFinal():
    print(f" ==== GESTIÓN DEL ALUMNADO === ")
    alumnado = [
        {
            "nombre": "Ana",
            "notas": [7.0, 8.0]
        }
    ]
    #Lista de opciones
    while True:
        opc = int(input(f"1. Añadir alumno\n2. Eliminar alumno\n3. Buscar alumno\n4. Añadir nota\n5. Mostrar alumnado\n6. Calcular media\n7. placeholder\n0. Salir"))
        match opc:
            case 1:
                nombre = input("Introduce el nombre del alumno: ")
                alumnado.append({"nombre": nombre, "notas": []})
            case 2:
                eliminar = input("Introduce el nombre del alumno que quieras eliminar: ")
                encontrado = False
                for alumno in alumnado:
                    if alumno["nombre"] == eliminar:
                        alumnado.remove(alumno)
                        print(f"Alumno eliminado")
                        encontrado = True
                        break
                    if not encontrado:
                        print(f"El alumno que buscas no existe.")
            case 3:
                buscar = input("Introduce el nombre del alumno que quieras buscar: ")
                
            case 4:
                print()
            case 5:
                print(f"La lista de los alumnos es: {alumnado}")
            case 6:
                print(f"La media de las notas de los alumnos es de: ")
            case 7:
                print()
            case 0:
                break
            case _:
                print("Error en la selección de opciones, intenta de nuevo")
actividadFinal()