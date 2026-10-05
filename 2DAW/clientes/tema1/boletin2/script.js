function comprobar() {
    const nombre = document.getElementById("txtNombre").value;
    const apellido1 = document.getElementById("txtApellido1").value;
    const apellido2 = document.getElementById("txtApellido2").value;

    const texto = nombre.trim() + apellido1.trim() + apellido2.trim()

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
    document.getElementById("salida").innerText += `\nDivisón del nombre completo:\n${nombre}\n${apellido1}\n${apellido2}`

    //NombreUsuario
    let txtUsuario = nombre.charAt(0).toLowerCase() + 
                    apellido1.slice(0, 3).toLowerCase() + 
                    apellido2.slice(0, 3).toLowerCase();

document.getElementById("salida").innerText += `\nNombre de usuario: ${txtUsuario}`;
}