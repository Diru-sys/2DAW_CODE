class Alumno {
    nombre;
    apellidos;
    edad;

    constructor(nombre,apellidos,edad) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.edad = edad;
    }

    imprimeAlumno() {
        return this.nombre + " " + this.apellidos + " - " + this.edad + " años.";
    }
}

let alum1 = new Alumno("Pedro","Sánchez Chivato", 45);
let alum2 = new Alumno("Feijoo","Muy Mid", 50);
let alum3 = new Alumno("Santiago","Abascal De Francisco Franco", 41);

document.getElementById("salida").innerHTML = alum1.imprimeAlumno() + "<br>" + alum2.imprimeAlumno() + "<br>" + alum3.imprimeAlumno()