#ACTIVIDAD 1
def media(*notas):
    notas = list(notas)
    print("Las notas introducidas son:", notas)
#media(5, 7, 8, 9, 10)


#ACTIVIDAD 2
def crear_archivos(**datos):
    for clave, valor in datos.items():
        print(f"La clave que estamos viendo es: {clave} y su valor es: {valor}")

pisos = {"pepe": "2º",
        "alberto": "3º",
        "laura": "1º"
        }

notas = {"maria": "6.7",
        "juan": "9",
        "aurora": "10"
        }
#crear_archivos(**pisos, **notas)


#ACTIVIDAD 3
productos = {
    "manzana": 1.5,
    "pera": 2.0,
    "platano": 1.7,
    "naranja": 1.2,
    "sandia": 3.0
}
def produccion(productos):
    productos_ordenados = sorted(productos, key=lambda x: productos[x], reverse=True)
    for producto in productos_ordenados:
        print(f"Producto: {producto}, Precio: {productos[producto]}")


#ACTIIVIDAD 4
def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Iniciando la función...")
        resultado = funcion(*args, **kwargs)
        print("Finalizando la función...")
        return resultado
    return wrapper

@decorador
def suma(a, b):
    print(a*b)
#suma(5,2)


#ACTIVIDAD 5
def decoradorContador(funcion):
    contador = [0]
    def wrapper(*args, **kwargs):
        contador[0] += 1
        print(f"Número de veces que se ha ejecutado esta función: {contador[0]}")
        return funcion(*args, **kwargs)
    return wrapper

@decoradorContador
def funcionPrueba(a, b):
    return a + b
#print(funcionPrueba(2, 7))