const t = [3, 19, 5, 44, 67, 12, 0, 1, 98, 6, 69, 22]

imprimirArray(t, "og");
if (t.length % 2 === 0) {
    t.sort(ordenarPar);
} else {
    t.sort(ordenarImpar)
}
imprimirArray(t, "salida");

function ordenarPar(a, b) {
    let x;
    if (a % 2 === b % 2) {
        x = a-b
    } else if (a % 2 == 0) {
        x = -1
    } else {
        x = 1
    }
    return x;
}

function ordenarImpar(a, b) {
    let x;
    if (a % 2 === b % 2) {
        x = a-b;
    } else if (a % 2 != 0) {
        x = -1;
    } else {
        x = 1;
    }
    return x;
}

function imprimirArray (a, salida) {
    document.getElementById(salida).innerHTML = a.join(" , ");
}
