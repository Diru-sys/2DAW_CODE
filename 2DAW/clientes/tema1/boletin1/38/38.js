function determinar(){
    let num, esPrimo;
    num = Number(frmNum.iNum.value);
    esPrimo = true;

    if (!Number.isInteger(num) || num < 2) {
        esPrimo = false;
    } else {
        for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            esPrimo = false;
            break;
        }
    }
    }
}