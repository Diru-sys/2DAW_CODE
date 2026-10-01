def ejecutar(funcion):
    def wrapper(*args, **kwargs):
        print("Estamos ejecutando una función llamada:", funcion.__name__)
        resultado = funcion(*args, **kwargs)
        print("Pieza de codigo terminada.")
        return resultado
    return wrapper


@ejecutar
def suma(a, b):
    print("La suma de", a, "y", b, "es:", a + b)

suma(3, 5)