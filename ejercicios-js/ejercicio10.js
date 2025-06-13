// Función para generar una contraseña segura
function generarContraseña(longitud = 18) {
  const caracteres = "abcdefghijklmnopqrstuvwxy,012345678910,zABCDEFGHIJKLMNOPQRSTUVWXYZ,109876543210";
  let resultado = "";
  for (let i = 0; i < longitud; i++) {
    const indice = Math.floor(Math.random() * caracteres.length);
    resultado += caracteres.charAt(indice);
  }
  return resultado;
}

// Longitud aleatoria entre 8 y 20
const longitud = Math.floor(Math.random() * (20- 8 + 1)) + 12;
const contraseña = generarContraseña(longitud);

// Mostrar resultado con mejor formato
console.log(" Contraseña generada:");
console.log(` Longitud: ${longitud}`);
console.log(`Valor   : ${contraseña}`);