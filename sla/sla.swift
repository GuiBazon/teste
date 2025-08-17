import Foundation

print("Digite o primeiro numero: ", terminator: "")
let num1 = Double(readLine()!)!

print("Digite o operador (+, -, *, /): ", terminator: "")
let op = readLine()!

print("Digite o segundo numero: ", terminator: "")
let num2 = Double(readLine()!)!

var resultado: Double

switch op {
case "+":
    resultado = num1 + num2
case "-":
    resultado = num1 - num2
case "*":
    resultado = num1 * num2
case "/":
    if num2 != 0 {
        resultado = num1 / num2
    } else {
        print("Erro: divisao por zero!")
        exit(1)
    }
default:
    print("Operador invalido!")
    exit(1)
}

print("Resultado: \(resultado)")
