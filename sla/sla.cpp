#include <iostream>
using namespace std;

int main() {
    double num1, num2, resultado;
    char op;

    cout << "Digite o primeiro numero: ";
    cin >> num1;

    cout << "Digite o operador (+, -, *, /): ";
    cin >> op;

    cout << "Digite o segundo numero: ";
    cin >> num2;

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
            cout << "Erro: divisao por zero!" << endl;
            return 1; // sai do programa com erro
        }
    } else {
        cout << "Operador invalido!" << endl;
        return 1;
    }

    cout << "Resultado: " << resultado << endl;
    return 0;
}
