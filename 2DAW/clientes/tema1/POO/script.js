class Alumno {
    _nombre;
    _apellidos;
    _edad;

    constructor(nombre,apellidos,edad) {
        this._nombre = nombre;
        this._apellidos = apellidos;
        this._edad = edad;
    }

    imprimeAlumno() {
        return this.nombre + " " + this.apellidos + " - " + this.edad + " años.";
    }

    get nombre() {
        return this._nombre;
    }

    get apellidos() {
        return this._apellidos;
    }

    get edad() {
        return this._edad;
    }

    set nombre(nombre) {
        if (nombre.length < 4) {
            alert("El nombre no  puede tener menos de 4 letras.");
        } else {
            this._nombre = nombre;
        }
    }

    set apellidos(apellidos) {
        this._apellidos = apellidos;
    }

    set edad(edad) {
        if (edad <= 0) {
            alert("La edad no puede ser menor o igual que 0.");
        } else {
            this._edad = edad;
        }
    }
}

let alum1 = new Alumno("Pedro","Sánchez Chivato", 45);
let alum2 = new Alumno("Feijoo","Muy Mid", 50);
let alum3 = new Alumno("Santiago","Abascal De Francisco Franco", 41);

document.getElementById("salida1").innerHTML = "<strong>Objetos sin ser manipulados:</strong> <br> " + alum1.imprimeAlumno() + "<br>" + alum2.imprimeAlumno() + "<br>" + alum3.imprimeAlumno();

alum1.nombre = "Ma";
alum1.nombre = "Mario";

alum2.edad = -2;
alum2.edad = 100;

document.getElementById("salida2").innerHTML = "<strong>Objetos manipulados:</strong> <br> " + alum1.imprimeAlumno() + "<br>" + alum2.imprimeAlumno() + "<br>" + alum3.imprimeAlumno();