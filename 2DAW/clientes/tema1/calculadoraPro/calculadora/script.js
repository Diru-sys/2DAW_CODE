let num1, num2;
let repetir = false;

function muestraDigito(num) {
    if (frmCalculadora.pantalla.value === "0") {
        frmCalculadora.pantalla.value = num;
    } else {
        frmCalculadora.pantalla.value += num;
    }
}

function sumar() {
    num1 = frmCalculadora.pantalla.value;
    frmCalculadora.pantalla.value = "0";
    repetir = false;
}

function igual() {
    if (num1 === undefined) return;

    if (!repetir) {
        num2 = frmCalculadora.pantalla.value;
        repetir = true;
    }

    num1 = Number(num1) + Number(num2);
    frmCalculadora.pantalla.value = num1;
}