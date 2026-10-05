function comprobar() {
    //Asignación constantes básicas
    const nombre = document.getElementById("txtNombre").value.trim();
    const apellido1 = document.getElementById("txtApellido1").value.trim();
    const apellido2 = document.getElementById("txtApellido2").value.trim();

    //Nombre completo
    const texto = nombre + apellido1 + apellido2

    //Asignación de nombre de usuario
    const usuario = (nombre.charAt(0) + apellido1.slice(0,3) + apellido2.slice(0,3)).toLowerCase();

    //Salida
    document.getElementById("salida").innerText = 
        `Tamaño del nombre completo sin espacios: ${texto.length}
        Cadena completa en minúsculas: ${texto.toLowerCase()}
        Cadena completa en mayúsculas: ${texto.toUpperCase()}
        División del nombre en 3 líneas distintas:
        ${nombre}
        ${apellido1}
        ${apellido2}
        Nombre de usuario propuesto: ${usuario}`;
}