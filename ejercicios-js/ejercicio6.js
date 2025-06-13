function factorial(n) {
    let resultado = 1;
    for (let i = 2; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}


let numero = Math.floor(Math.random() * 10) + 1;


let resultado = factorial(numero);


console.log(`${numero}! = ${resultado}`);