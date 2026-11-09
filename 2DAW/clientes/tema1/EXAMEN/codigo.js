"use strict";

// Instancia global del contenedor
let oConcesionario = new Concesionario();

// Carga inicial de datos de prueba
datosIniciales();

function datosIniciales() {
  oConcesionario.altaVehiculo(new Electrico(101, 15000, "Tesla", "Model 3", 450));
  oConcesionario.altaVehiculo(new Combustion(102, 95000, "Seat", "Ibiza", "Gasolina"));
  oConcesionario.altaVehiculo(new Electrico(103, 60000, "Nissan", "Leaf", 270));
  oConcesionario.altaVehiculo(new Combustion(104, 120000, "Volkswagen", "Golf", "Diesel"));
  oConcesionario.altaVehiculo(new Combustion(105, 45000, "Toyota", "Yaris", "Hibrido"));
}

// Control de visibilidad de formularios
function gestionFormularios(sFormularioVisible) {
  ocultarTodosLosFormularios();

  switch (sFormularioVisible) {
    case "frmAltaVehiculo":
      frmAltaVehiculo.style.display = "block";
      break;
    case "frmActualizarKms":
      frmActualizarKms.style.display = "block";
      break;
    case "frmListadoElectricos":
      frmListadoElectricos.style.display = "block";
      break;
    case "frmListadoCombustion":
      frmListadoCombustion.style.display = "block";
      break;
    case "TotalVehiculos":
      alert("Hay " + oConcesionario.totalVehiculosOferta() + " vehículos en oferta");
      break;
  }
}

function ocultarTodosLosFormularios() {
  let oFormularios = document.querySelectorAll("form");
  for (let i = 0; i < oFormularios.length; i++) {
    oFormularios[i].style.display = "none";
  }
}

// Manejador: Alta de Vehículo
function aceptarAltaVehiculo() {
  const sBastidor = frmAltaVehiculo.txtBastidor.value.trim();
  const sKms = frmAltaVehiculo.txtKms.value.trim();
  const sMarca = frmAltaVehiculo.txtMarca.value.trim();
  const sModelo = frmAltaVehiculo.txtModelo.value.trim();
  const sTipoVehiculo = frmAltaVehiculo.rbtTipoVehiculo.value;
  const sAutonomia = frmAltaVehiculo.txtAutonomia.value.trim();
  const sCombustible = frmAltaVehiculo.selectCombustible.value;

  // Validación de campos vacíos
  if (
    sBastidor === "" ||
    sKms === "" ||
    sMarca === "" ||
    sModelo === "" ||
    (sTipoVehiculo === "electrico" && sAutonomia === "")
  ) {
    alert("Error: Debe rellenar todos los datos requeridos del vehículo.");
    return;
  }

  const iBastidor = Number(sBastidor);
  const iKms = Number(sKms);

  if (isNaN(iBastidor) || isNaN(iKms)) {
    alert("Error: El bastidor y el kilometraje deben ser valores numéricos.");
    return;
  }

  let oVehiculo;
  if (sTipoVehiculo === "electrico") {
    const iAutonomia = Number(sAutonomia);
    if (isNaN(iAutonomia)) {
      alert("Error: La autonomía debe ser un número.");
      return;
    }
    oVehiculo = new Electrico(iBastidor, iKms, sMarca, sModelo, iAutonomia);
  } else {
    oVehiculo = new Combustion(iBastidor, iKms, sMarca, sModelo, sCombustible);
  }

  // Insertar vehículo
  if (oConcesionario.altaVehiculo(oVehiculo)) {
    alert("Vehículo registrado correctamente");
    frmAltaVehiculo.reset();
    frmAltaVehiculo.style.display = "none";
  } else {
    alert("Error: El número de bastidor ya existe");
  }
}

// Manejador: Actualizar Kilometraje
function aceptarActualizarKms() {
  const sBastidor = frmActualizarKms.txtBastidorKms.value.trim();
  const sKms = frmActualizarKms.txtNuevoKms.value.trim();

  if (sBastidor === "" || sKms === "") {
    alert("Error: Debe introducir el número de bastidor y el nuevo kilometraje.");
    return;
  }

  const iBastidor = Number(sBastidor);
  const iKms = Number(sKms);

  if (isNaN(iBastidor) || isNaN(iKms)) {
    alert("Error: Los datos introducidos deben ser numéricos.");
    return;
  }

  let sRespuesta = oConcesionario.actualizarKms(iBastidor, iKms);
  alert(sRespuesta);

  if (sRespuesta.includes("Correcto")) {
    frmActualizarKms.reset();
    frmActualizarKms.style.display = "none";
  }
}

// Manejador: Listado Eléctricos en Ventana Emergente
function aceptarListadoElectricos() {
  const sAutonomiaMin = frmListadoElectricos.txtAutonomiaMin.value.trim();

  if (sAutonomiaMin === "" || isNaN(Number(sAutonomiaMin))) {
    alert("Error: Debe indicar una autonomía mínima válida.");
    return;
  }

  const iAutonomiaMin = Number(sAutonomiaMin);

  let oVentana = open("", "_blank", "");
  oVentana.document.open();
  oVentana.document.write(
    "Listado de vehículos eléctricos (Autonomía min: " + iAutonomiaMin + " km)<br>"
  );
  oVentana.document.write(oConcesionario.listadoElectricos(iAutonomiaMin));
  oVentana.document.close();
  oVentana.document.title = "Listado Eléctricos";

  frmListadoElectricos.reset();
  frmListadoElectricos.style.display = "none";
}

// Manejador: Listado Combustión en Ventana Emergente
function aceptarListadoCombustion() {
  const sCombustible = frmListadoCombustion.selectCombustibleFiltro.value;

  let oVentana = open("", "_blank", "");
  oVentana.document.open();
  oVentana.document.write("Listado de vehículos de combustión: " + sCombustible + "<br>");
  oVentana.document.write(oConcesionario.listadoCombustion(sCombustible));
  oVentana.document.close();
  oVentana.document.title = "Listado Combustión";

  frmListadoCombustion.reset();
  frmListadoCombustion.style.display = "none";
}