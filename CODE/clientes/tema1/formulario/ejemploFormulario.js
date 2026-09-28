// Creas con 'let variable' y luego la usas tal que: 'variable=nombreFormulario.nombreCampo.value'
// Posteriori, escribes el mensaje que quieres enseñar y 'document.getElementById("nombreDiv").innerHTML = variableSalida'
function mostrarDatos(){
    let nombre,apellidos,mensajeSalida;
    nombre=frmDatos.iNombre.value;
    apellidos=frmDatos.iApellidos.value;

    mensajeSalida="Hola, " + nombre + " " + apellidos;
    document.getElementById("salida").innerHTML=mensajeSalida;
}