function esPrimo(numero) {
    if (numero <= 1) return false; // Los números menores o iguales a 1 no son primos
    if (numero === 2) return true; // El 2 es primo
    if (numero % 2 === 0) return false; // Los pares mayores que 2 no son primos

    // Solo revisamos hasta la raíz cuadrada del número
    const limite = Math.sqrt(numero);
    for (let i = 3; i <= limite; i += 2) {
        if (numero % i === 0) {
            return false;
        }
    }
    return true;

}
