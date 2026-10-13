function mostrarReloj() {
    const r = new Date()
    const horaCorta = r.toLocaleTimeString();

    document.getElementById("reloj").innerHTML = `<strong>${horaCorta}</strong>`;
}

setInterval(mostrarReloj, 1000)