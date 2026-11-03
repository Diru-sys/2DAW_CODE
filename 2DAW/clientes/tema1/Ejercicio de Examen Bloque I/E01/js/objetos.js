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
        let salida = "<tr>";

        /*salida =
        "<tr><td>" +
        this.codigo +
        "</td><td>" +
        this.especie +
        "</td><td>" +
        this.tallaje +
        "</td></tr>";*/

    for (let atrib of Object.values(this)) {
        salida += "<td>" + atrib + "</td>";
    }
    salida += "</tr>";

    return salida;
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

    /*toHTMLRow() {
        let salida;
        salida = super.toHTMLRow();
        salida = salida.replace("</tr>", "");
        salida += "<td>" + this.frutal + "</td></tr>";
        return salida;
    }*/
}

class Caduco extends Arbol {
    _mesFloracion;
    
    constructor(codigo, tallaje, especie, frutal) {
        super(codigo, tallaje, especie);
        this._mesFloracion = this.mesFloracion;
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

    altaArbol(oArbol){
        if (this.arboles.some()){
        return false;    
        } else {
            this.arboles.push(oArbol);
            return true;
        }
    }   
}