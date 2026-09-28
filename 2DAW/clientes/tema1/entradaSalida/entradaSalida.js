//Para declarar variables, antes se usaba "var". Ahora se desaconseja. Mejor usar "let"
let mensaje;
mensaje = "Hola, ya casi no queda nada para el recreo";
alert(mensaje); //alert es como un Toast, va por encima de la web

mensaje = prompt("Introduzca el mensaje");

//salida que no sale en el documento
console.log("Hablo a la consola del F12")

//De todo el documento html, dame aquel cuyo id único sea "salida" y le asigno un valor
document.getElementById("salida").innerHTML = mensaje + "!!!!!!!!!!!!!!!!!!!!!!!!!!";

//Sobrecarga de operadores -> un mismo operador puede tener distintos comportamientos según los operandos