const prompt = require("prompt-sync")(); // precisa instalar prompt-sync (npm install prompt-sync)

let num1 = parseFloat(prompt("Digite o primeiro numero: "));
let op = prompt("Digite o operador (+, -, *, /): ");
let num2 = parseFloat(prompt("Digite o segundo numero: "));

let resultado;

if (op === "+") {
  resultado = num1 + num2;
} else if (op === "-") {
  resultado = num1 - num2;
} else if (op === "*") {
  resultado = num1 * num2;
} else if (op === "/") {
  if (num2 !== 0) {
    resultado = num1 / num2;
  } else {
    console.log("Erro: divisao por zero!");
    process.exit(1);
  }
} else {
  console.log("Operador invalido!");
  process.exit(1);
}

console.log("Resultado:", resultado);
