let num, num1, num2;
function mostrarDigito(num) {
    if (formularioCalculadora.pantallaAuxiliar.value === "0") {
        formularioCalculadora.pantallaAuxiliar.value = num;
    } else {
        formularioCalculadora.pantallaAuxiliar.value += num;
    }
}