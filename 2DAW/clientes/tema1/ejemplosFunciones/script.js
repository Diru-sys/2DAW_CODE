const sumar = (a, b) => a + b;

function realizaSuma(a, b) {
    let resultado;
    resultado = sumar(a, b);
    document.getElementById("salida").innerHTML = "El resultado de la suma es: " + resultado;
}
