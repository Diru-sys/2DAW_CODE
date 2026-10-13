let min = 0;
let seg = 0;
let dec = 0;
let contador = false;

function actualizar() {
    if (contador === false) {
        return;
    }

    dec++
    if (dec === 10) {
        dec = 0;
        seg++;
    }

    if (seg === 60) {
        seg = 0;
        min++;
    }

    let minTexto = min;
    if (min < 10) {
        minTexto  = "0" + min;
    }

    let segTexto = seg;
    if (seg < 10) {
        segTexto = "0" + seg;
    }

    mostrarCrono(minTexto, segTexto);
}

function mostrarCrono(minTexto, segTexto){
    document.getElementById("salida").innerHTML = minTexto + ":" + segTexto + ":" + dec;
}

function iniciarPausar() {
    if (contador === true) {
        contador = false;
    } else {
        contador = true;
    }
}

function reset() {
    contador = false;
    min = 0;
    seg = 0;
    dec = 0;
    mostrarCrono("00", "00");
}

setInterval(actualizar, 100);   