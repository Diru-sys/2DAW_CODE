class Vehiculo {
    _bastidor;
    _kms;
    _marca;
    _modelo;

    constructor (bastidor, kms, marca, modelo) {
        this._bastidor = bastidor;
        this._kms = kms;
        this._marca = marca;
        this._modelo = modelo;
    }

    //Getters
    get bastidor() {
        return this._bastidor;
    }

    get kms() {
        return this._kms;
    }

    get marca() {
        return this._marca;
    }

    get modelo() {
        return this._modelo;
    }

    //Setters
    set bastidor(valor) {
        this._bastidor = valor;
    }

    set kms(valor) {
        this._kms = valor;
    }

    set marca(valor) {
        this._marca = valor;
    }

    set modelo(valor) {
        this._modelo = valor;
    }

    toHTMLRow() {
        let salida = "<tr>";

        for (let i of Object.values(this)) {
            salida += "<td>" + i + "</td>";
        }

        salida += "</tr>";
        return salida;
    }
}


class Electrico extends Vehiculo {
    _autonomia;

    constructor(bastidor, kms, marca, modelo, autonomia) {
        super(bastidor, kms, marca, modelo);
        this._autonomia = autonomia;
    }

    //Getters
    get autonomia() {
        return this._autonomia;
    }

    //Setters
    set autonomia(valor) {
        this._autonomia = valor;
    }
}


class Combustion extends Vehiculo {
    _combustible;

    constructor(bastidor, kms, marca, modelo, combustible) {
        super(bastidor, kms, marca, modelo);
        this._combustible = combustible;
    }

    //Getters
    get combustible() {
        return this._combustible;
    }

    //Setters
    set combustible(valor) {
        this._combustible = valor;
    }
}


class Concesionario {
    _vehiculos;
    
    constructor () {
        this._vehiculos = [];
    }

    //Getters
    get vehiculos() {
        return this._vehiculos;
    }

    //Setters
    set vehiculos(valor) {
        this._vehiculos = valor;
    }

    altaVehiculo(oVehiculo) {
        let existe = this.vehiculos.some(elem => elem.bastidor === oVehiculo.bastidor);
        if (existe) {
            return false;
        } else {
            this.vehiculos.push(oVehiculo);
            return true;
        }
    }

    actualizarKms(iBastidor, iNuevoKms) {
        let vehiculo = this.vehiculos.find(elem => elem.bastidor === iBastidor);
        if (vehiculo === undefined) {
            return "Vehículo no registrado.";
        } else {
            if (vehiculo.kms > iNuevoKms) {
                return "Kilometraje inferior al registrado.";
            } else {
                vehiculo.kms = iNuevoKms;
                let tipoVehiculo = (vehiculo instanceof Electrico) ? "Electrico" : "Combustion";
                return "Correcto, kilometraje actualizado. Tipo: " + tipoVehiculo;
            }
        }
    }

    listadoElectricos(iMinAutonomia) {
        let vehiculosElectricos = this.vehiculos.filter(elem => elem instanceof Electrico && elem.autonomia >= iMinAutonomia);
        vehiculosElectricos.sort((a, b) => b.autonomia - a.autonomia);

        let salida = '<table border="1"><thead><tr><th>Bastidor</th><th>Kms</th><th>Marca</th><th>Modelo</th><th>Autonomía (km)</th></tr></thead><tbody>';
        for (let vehiculo of vehiculosElectricos) {
            salida += vehiculo.toHTMLRow();
        }
        salida += "</tbody></table>";
        return salida;
    }
    
    listadoCombustion(sCombustible) {
        let vehiculosCombustion = this.vehiculos.filter(elem => elem instanceof Combustion && elem.combustible.trim().toLowerCase() === sCombustible.trim().toLowerCase());

        let salida = '<table border="1"><thead><tr><th>Bastidor</th><th>Kms</th><th>Marca</th><th>Modelo</th><th>Combustible</th></tr></thead><tbody>';
        for (let vehiculo of vehiculosCombustion) {
            salida += vehiculo.toHTMLRow();
        }
        salida += "</tbody></table>";
        return salida;
    }

    totalVehiculosOferta() {
        
    }
}