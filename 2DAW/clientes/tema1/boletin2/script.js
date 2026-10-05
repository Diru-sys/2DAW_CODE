function comprobar() {
    const txtNombre = document.getElementById("txtNombre").value;
    const txtApellido1 = document.getElementById("txtApellido1").value;
    const txtApellido2 = document.getElementById("txtApellido2").value;

    const texto = txtNombre.trim() + txtApellido1.trim() + txtApellido2.trim()

    //Longitud
    let txtLongitud = texto.length;
    document.getElementById("salida").innerText = `Longitud de nombre + apellidos (sin espacios): ${txtLongitud}`;

    //Minusculas
    let txtMin = texto.toLowerCase();
    document.getElementById("salida").innerText += `\nCadena completa en minúsculas: ${txtMin}`;

    //Mayusculas
    let txtMay = texto.toUpperCase();
    document.getElementById("salida").innerText += `\nCadena completa en mayúsculas: ${txtMay}`;

    //División
    document.getElementById("salida").innerText += `\nDivisón del nombre completo:\n${txtNombre}\n${txtApellido1}\n${txtApellido2}`

    //NombreUsuario
    let txtUsuario = txtNombre.charAt(0).toLowerCase() + 
                    txtApellido1.slice(0, 3).toLowerCase() + 
                    txtApellido2.slice(0, 3).toLowerCase();

document.getElementById("salida").innerText += `\nNombre de usuario: ${txtUsuario}`;
}