fun main() {
    print("Digite o primeiro numero: ")
    val num1 = readLine()!!.toDouble()

    print("Digite o operador (+, -, *, /): ")
    val op = readLine()!![0]

    print("Digite o segundo numero: ")
    val num2 = readLine()!!.toDouble()

    val resultado = when (op) {
        '+' -> num1 + num2
        '-' -> num1 - num2
        '*' -> num1 * num2
        '/' -> if (num2 != 0.0) num1 / num2 else {
            println("Erro: divisao por zero!")
            return
        }
        else -> {
            println("Operador invalido!")
            return
        }
    }

    println("Resultado: $resultado")
}
