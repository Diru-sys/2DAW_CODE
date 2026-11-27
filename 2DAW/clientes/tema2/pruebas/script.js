const regexp = /^(0[1-9]|[1-4]\d|5[0-2])\d{3}$/;
// 5 digitos obligatorios
// 2 primeros digitos entre 01 y 52
// 3 digitos posteriores cualesquiera

regexp.test("28013");
// deberia ser true porque los dos primeros digitos estan entre 01 y 52,
// luego tiene 3 digitos y 5 digitos en total en exacto


regexp.test("60129");
// deberia de ser false porque los 2 primeros digitos estan por encima del 52.

const regexpLOL = /^\d{4}[- ]?[BCDFGHJKLMNPRSTVWXYZ]{3}$/;
// 4 digitos obligatorios
// Opcional puede ser un espacio en blanco o un guion
// 3 letras posteriores consonantes en mayusucla, sin vocales
// Sin la Ñ o la Q