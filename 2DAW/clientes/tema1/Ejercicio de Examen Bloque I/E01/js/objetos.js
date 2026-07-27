class Arbol {
    _codigo;
    _tallaje;
    _especie;

    constructor(codigo, tallaje, especie) {
        this._codigo = codigo;
        this._especie = especie;
        this._tallaje = tallaje;
    }

    get codigo() {
        return this._codigo;
    }

    get tallaje() {
        return this._tallaje;
    }

    get especie() {
        return this._especie;
    }

    set codigo(valor) {
        this._codigo = valor;
    }

    set tallaje(valor) {
        this._tallaje = valor;
    }

    set especie(valor) {
        this._especie = valor;
    }

    toHTMLRow() {
        let salida = "<td>";

        for (let iterar of Object.values(this)) {
            salida += "<td>" + iterar + "</td>";
        }
        salida += "</tr>";

        return salida;
    }
}