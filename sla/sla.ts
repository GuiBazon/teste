import * as readlineSync from 'readline-sync';

let num1 = parseFloat(readlineSync.question("Digite o primeiro numero: "));
let op = readlineSync.question("Digite o operador (+, -, *, /): ");
let num2 = parseFloat(readlineSync.question("Digite o segundo numero: "));

let resultado: number;

if (op === "+") resultado = num1 + num2;
else if (op === "-") resultado = num1 - num2;
else if (op === "*") resultado = num1 * num2;
else if (op === "/") {
    if (num2 !== 0) resultado = num1 / num2;
    else { console.log("Erro: divisao por zero!"); process.exit(1); }
} else { console.log("Operador invalido!"); process.exit(1); }

console.log("Resultado:", resultado);
