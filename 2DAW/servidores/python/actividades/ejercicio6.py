#1.- Mostrar todos los números pares entre 1 y 100.
#2.- Calcular la suma de los números del 1 al 100.
#3.- Pedir números hasta que el usuario introduzca 0 y mostrar su suma.

#1 ->
for i in range(2,101,2):
    print(i, "\n")


#2 ->
contador=0
for i in range(1,101):
    contador+=i


#3 ->
numeroUsuario = 0
suma = 0
while(True):
    numeroUsuario=int(input("Introduce tu número: "))
    if(numeroUsuario==0):
        break
    suma+=numeroUsuario

print(suma)