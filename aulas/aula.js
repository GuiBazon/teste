// Aula de JavaScript - Conceitos Fundamentais

// 1. TIPOS DE DADOS BÁSICOS
let inteiro = 10;          // number
let real = 3.14;           // number
let texto = "Hello";       // string
let booleano = true;       // boolean

let lista = [1, 2, 3];     // array
let conjunto = new Set([1, 2, 2, 3]); // set
let dicionario = { nome: "Gui", idade: 17 }; // object

console.log(inteiro, real, texto, booleano);
console.log(lista, conjunto, dicionario);

// ------------------------------------------------------
// 2. OPERADORES
let x = 5, y = 2;
console.log(x + y);   // soma
console.log(x - y);   // subtração
console.log(x * y);   // multiplicação
console.log(x / y);   // divisão
console.log(x % y);   // resto
console.log(x ** y);  // potência

console.log(x == y, x > y, x !== y);

// ------------------------------------------------------
// 3. CONTROLE DE FLUXO
if (x > y) {
  console.log("x é maior que y");
} else if (x === y) {
  console.log("x é igual a y");
} else {
  console.log("x é menor que y");
}

// Loop for
for (let i = 0; i < 5; i++) {
  console.log("for:", i);
}

// Loop while
let contador = 0;
while (contador < 3) {
  console.log("while:", contador);
  contador++;
}

// ------------------------------------------------------
// 4. FUNÇÕES
function soma(a, b) {
  return a + b;
}
console.log("Função soma:", soma(3, 4));

// ------------------------------------------------------
// 5. ESTRUTURAS DE DADOS
let numeros = [10, 20, 30];
numeros.push(40);
console.log("Lista:", numeros);

let aluno = { nome: "Ana", nota: 9.5 };
console.log("Nome:", aluno.nome);

// ------------------------------------------------------
// 6. ENTRADA E SAÍDA
// let entrada = prompt("Digite algo:");
// console.log("Você digitou:", entrada);

// ------------------------------------------------------
// 7. TRATAMENTO DE ERROS
try {
  console.log(10 / 0);
} catch (e) {
  console.log("Erro:", e);
}

// ------------------------------------------------------
// 8. ORIENTAÇÃO A OBJETOS
class Pessoa {
  constructor(nome, idade) {
    this.nome = nome;
    this.idade = idade;
  }
  falar() {
    console.log(`Oi, eu sou ${this.nome} e tenho ${this.idade} anos.`);
  }
}

let p1 = new Pessoa("Gui", 17);
p1.falar();

// ------------------------------------------------------
// 9. MÓDULOS / BIBLIOTECAS
// Exemplo: usar a biblioteca Math
console.log("Raiz quadrada de 16:", Math.sqrt(16));

// ------------------------------------------------------
// 10. PARADIGMAS
// Imperativo
x = 10;
y = 20;
console.log(x + y);

// Funcional
let valores = [1, 2, 3, 4];
let dobro = valores.map(n => n * 2);
console.log("Dobro:", dobro);

// OO já vimos com a classe Pessoa
