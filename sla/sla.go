package main
import (
    "fmt"
)

func main() {
    var num1, num2, resultado float64
    var op string

    fmt.Print("Digite o primeiro numero: ")
    fmt.Scan(&num1)

    fmt.Print("Digite o operador (+, -, *, /): ")
    fmt.Scan(&op)

    fmt.Print("Digite o segundo numero: ")
    fmt.Scan(&num2)

    if op == "+" {
        resultado = num1 + num2
    } else if op == "-" {
        resultado = num1 - num2
    } else if op == "*" {
        resultado = num1 * num2
    } else if op == "/" {
        if num2 != 0 {
            resultado = num1 / num2
        } else {
            fmt.Println("Erro: divisao por zero!")
            return
        }
    } else {
        fmt.Println("Operador invalido!")
        return
    }

    fmt.Println("Resultado:", resultado)
}
