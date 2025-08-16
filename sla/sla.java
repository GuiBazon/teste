import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double num1, num2, resultado;
        char op;

        System.out.print("Digite o primeiro numero: ");
        num1 = sc.nextDouble();

        System.out.print("Digite o operador (+, -, *, /): ");
        op = sc.next().charAt(0); // pega o primeiro caractere digitado

        System.out.print("Digite o segundo numero: ");
        num2 = sc.nextDouble();

        if (op == '+') {
            resultado = num1 + num2;
        } else if (op == '-') {
            resultado = num1 - num2;
        } else if (op == '*') {
            resultado = num1 * num2;
        } else if (op == '/') {
            if (num2 != 0) {
                resultado = num1 / num2;
            } else {
                System.out.println("Erro: divisao por zero!");
                sc.close();
                return;
            }
        } else {
            System.out.println("Operador invalido!");
            sc.close();
            return;
        }

        System.out.println("Resultado: " + resultado);
        sc.close();
    }
}
