function mostrarTabla(){
    let mensajeSalida = "";
    let num=Number(fromDatos.iNumero.value);
    for(i=1;i<=10;i++){
        mensajeSalida += num + " x " + i + " = " + num*i + "<br>"
    }
    document.getElementById("salida").innerHTML = mensajeSalida;
}