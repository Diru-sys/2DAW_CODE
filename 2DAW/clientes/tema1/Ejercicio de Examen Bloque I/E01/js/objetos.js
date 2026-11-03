class Arbol {
    _codigo;
    _tallaje;
    _especie;

    constructor(codigo, tallaje, especie) {
        this._especie = especie;
        this._codigo = codigo;
        this._tallaje = tallaje;
    }
    get especie() {
        return this._especie;
    }

    set especie(value) {
        this._especie = value;
    }

    get tallaje() {
        return this._tallaje;
    }

    set tallaje(value) {
        this._tallaje = value;
    }

    get codigo() {
        return this._codigo;
    }

    set codigo(value) {
        this._codigo = value;
    }

    toHTMLRow() {
        /*salida =
        "<tr><td>" +
        this.codigo +
        "</td><td>" +
        this.especie +
        "</td><td>" +
        this.tallaje +
        "</td></tr>";*/
        return `<tr><td>${this.codigo}</td><td>${this.tallaje}</td><td>${this.especie}</td></tr>`;
}
}

class Perenne extends Arbol {
    _frutal;

    constructor(codigo, tallaje, especie, frutal) {
        super(codigo, tallaje, especie);
        this._frutal = frutal;
    }
    get frutal() {
        return this._frutal;
    }

    set frutal(value) {
        this._frutal = value;
    }

    toHTMLRow() {
        return `<tr><td>${this.codigo}</td><td>${this.tallaje}</td><td>${this.especie}</td><td>${this.frutal}</td></tr>`;
    }

    
}

class Caduco extends Arbol {
    _mesFloracion;
    
    constructor(codigo, tallaje, especie, mesFloracion) {
        super(codigo, tallaje, especie);
        this._mesFloracion = mesFloracion;
}
    get mesFloracion() {
        return this._mesFloracion;
    }

    set mesFloracion(value) {
        this._mesFloracion = value;
    }
}

class Vivero {
    _arboles;

    constructor() {
        this._arboles = [];
    }

    get arboles() {
        return this._arboles;
    }

    set arboles(value) {
        this._arboles = value;
    }

    altaArbol(oArbol) {
        /*
        function condicion(arbol) {
            return arbol.codigo == oArbol.codigo;
        }
        existe = this.arboles.some(test);
        if (!existe) {
            this.arboles.push(oArbol)
        }
        return !existe;
        */
        let existe = this.arboles.some((elem) => (elem.codigo === oArbol.codigo));
        if (!existe) {
            this.arboles.push(oArbol)
        }
        return !existe;
    }

    tallajeArbol(iCodigo, iTallaje) {
        let arbol = this.arboles.find((elem) => elem.codigo === iCodigo);
        let respuesta = "";

        if (arbol === undefined) {
            respuesta = "Arbol no registrado";
        } else if (arbol.tallaje > iTallaje) {
            respuesta = "Tallaje inferior al registrado.";
        } else {
            arbol.tallaje = iTallaje;
            respuesta = "Correcto, tallaje actualizado.";
            let tipoArbol;
            arbol instanceof Caduco
                ? (tipoArbol = "Caduco")
                : (tipoArbol = "Perenne");
            respuesta += " " + tipoArbol;
        }
        return respuesta;
    }

    listadoPerennes(iMinAltura) {
        let tablaPerennes;

        tablaPerennes = this.arboles.filter(
            (elem) => elem instanceof Perenne && elem.tallaje >= iMinAltura
        );

        tablaPerennes.sort((a,b) => b.tallaje - a.tallaje);

        let salida = "<table><thead><tr><th>Código</th><th>Tallaje</th><th>Especie</th><th>Frutal</th></tr></thead><tbody>";

        for (let arbol of tablaPerennes) {
            salida += arbol.toHTMLRow();
        }

        salida += "</tbody></table>"
        return salida;
    }
}