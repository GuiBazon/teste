using System;

class Calculadora {
    static void Main() {
        Console.Write("Digite o primeiro numero: ");
        double num1 = double.Parse(Console.ReadLine());

        Console.Write("Digite o operador (+, -, *, /): ");
        char op = Console.ReadLine()[0];

        Console.Write("Digite o segundo numero: ");
        double num2 = double.Parse(Console.ReadLine());

        double resultado;

        if (op == '+') resultado = num1 + num2;
        else if (op == '-') resultado = num1 - num2;
        else if (op == '*') resultado = num1 * num2;
        else if (op == '/') {
            if (num2 != 0) resultado = num1 / num2;
            else { Console.WriteLine("Erro: divisao por zero!"); return; }
        } else { Console.WriteLine("Operador invalido!"); return; }

        Console.WriteLine("Resultado: " + resultado);
    }
}
