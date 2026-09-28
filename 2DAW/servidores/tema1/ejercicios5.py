#Actividad 1: clasificación de una nota
#Solicita una nota de 0 a 10 y muestra:
nota = float(input("Introduce la nota: "))
if (nota < 0 or nota > 10):
    print("No es posible valores menores que 0 o mayores que 10.")
elif(nota < 5):
    print("Suspenso")
elif(nota < 6 ):
    print("Suficiente")
elif(nota < 8):
    print("Bien")
elif(nota>=8 and nota<9):
    print("Notable")
else:
    print("Sobresaliente")


# Actividad 2: año bisiesto
# Investiga las reglas y crea un programa que determine si un año es bisiesto.
año = int(input("Introduce el año: "))
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print ("El año es bisiesto")
else:
    print("El año no es bisiesto")


#Actividad 3: tarifa de entrada
#Calcula el precio de una entrada según edad y condición de estudiante.
precio = 10

edad = int(input("Introduce tu edad: "))

estudiante = (input("¿Eres estudiante? (S/N): ")).lower
if estudiante in ('s','n'):
    precio-=2

if edad<=30:
    precio-=2
if edad>=60:
    precio-=5

print(f"El precio de la entrada es {precio}")