let num1 = null;
let num2 = null;
let signo = "";
let reiniciar = false;

function mostrarDigito(num) {
    if (reiniciar) {
        if (signo === "") formularioCalculadora.pantallaAuxiliar.value = "0";
        formularioCalculadora.pantallaCalculadora.value = num;
        reiniciar = false;
    } else if (formularioCalculadora.pantallaCalculadora.value === "0") {
        formularioCalculadora.pantallaCalculadora.value = num;
    } else {
        formularioCalculadora.pantallaCalculadora.value += num;
    }
}

function mostrarSigno(nuevoSigno) {
    if (formularioCalculadora.pantallaCalculadora.value === "Error") {
        return;
    }

    if (signo !== "" && reiniciar === true) {
        signo = nuevoSigno;
        formularioCalculadora.pantallaAuxiliar.value = num1 + " " + signo;
        return;
    }

    if (signo !== "") {
        num2 = Number(formularioCalculadora.pantallaCalculadora.value);
        let resultado = operar(num1, num2, signo);
        if (resultado === null){
            return mostrarError();
        }
        num1 = resultado;
    } else {
        num1 = Number(formularioCalculadora.pantallaCalculadora.value);
    }

    signo = nuevoSigno;
    formularioCalculadora.pantallaAuxiliar.value = num1 + " " + signo;
    formularioCalculadora.pantallaCalculadora.value = num1;
    reiniciar = true;
}

function calcular() {
    if (signo === "" || reiniciar){
        return;
    }

    num2 = Number(formularioCalculadora.pantallaCalculadora.value);
    let resultado = operar(num1, num2, signo);

    if (resultado === null){
        return mostrarError();
    } 

    formularioCalculadora.pantallaAuxiliar.value = num1 + " " + signo + " " + num2 + " =";
    formularioCalculadora.pantallaCalculadora.value = resultado;
    num1 = resultado;
    signo = "";
    reiniciar = true;
}

function operar(a, b, op) {
    let r;
    switch (op) {
        case "+": r = a + b; break;
        case "-": r = a - b; break;
        case "x": r = a * b; break;
        case "/":
            if (b === 0) return null;
            r = a / b;
            break;
        default: return null;
    }
    return Math.round(r * 10000000000) / 10000000000;
}

function mostrarError() {
    formularioCalculadora.pantallaCalculadora.value = "Error";
    formularioCalculadora.pantallaAuxiliar.value = "No se puede dividir entre 0";
    num1 = null;
    num2 = null;
    signo = "";
    reiniciar = true;
}