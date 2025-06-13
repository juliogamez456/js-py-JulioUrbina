// Genera un arreglo de 45 números aleatorios entre 1 y 355
const numeros = Array.from({ length: 355}, () => Math.floor(Math.random() * 355) + 1);

// Calcula la suma de los números
const suma = numeros.reduce((total, numero) => total + numero, 0);

// Muestra los resultados de forma clara
console.log(` Números aleatorios: [${numeros.join(', ')}]`);
console.log(` Suma total: ${suma}`);