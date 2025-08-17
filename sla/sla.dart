import 'dart:io';

void main() {
  stdout.write("Digite o primeiro número: ");
  double a = double.parse(stdin.readLineSync()!);

  stdout.write("Digite o operador (+, -, *, /): ");
  String op = stdin.readLineSync()!;

  stdout.write("Digite o segundo número: ");
  double b = double.parse(stdin.readLineSync()!);

  double result;

  switch (op) {
    case '+':
      result = a + b;
      break;
    case '-':
      result = a - b;
      break;
    case '*':
      result = a * b;
      break;
    case '/':
      if (b != 0) {
        result = a / b;
      } else {
        print("Erro: divisão por zero!");
        return;
      }
      break;
    default:
      print("Operador inválido!");
      return;
  }

  print("Resultado: $result");
}
