#include <stdio.h>

int main() {
    double num1, num2, resultado;
    char op;

    printf("Digite o primeiro numero: ");
    scanf("%lf", &num1);  // %lf = double

    printf("Digite o operador (+, -, *, /): ");
    scanf(" %c", &op);    // espaço antes do %c ignora o enter anterior

    printf("Digite o segundo numero: ");
    scanf("%lf", &num2);

    if (op == '+') resultado = num1 + num2;
    else if (op == '-') resultado = num1 - num2;
    else if (op == '*') resultado = num1 * num2;
    else if (op == '/') {
        if (num2 != 0) resultado = num1 / num2;
        else { printf("Erro: divisao por zero!\n"); return 1; }
    } else {
        printf("Operador invalido!\n");
        return 1;
    }

    printf("Resultado: %.2lf\n", resultado); // %.2lf = 2 casas decimais
    return 0;
}
