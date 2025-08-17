double num1, num2, resultado;
char op;

void setup() {
  Serial.begin(9600); // inicia comunicação serial
  while (!Serial);    // espera a Serial iniciar

  Serial.println("Digite o primeiro numero:");
  while (Serial.available() == 0) {} // espera input
  num1 = Serial.parseFloat();

  Serial.println("Digite o operador (+, -, *, /):");
  while (Serial.available() == 0) {}
  op = Serial.read(); 
  Serial.read(); // consome o '\n' extra

  Serial.println("Digite o segundo numero:");
  while (Serial.available() == 0) {}
  num2 = Serial.parseFloat();

  if (op == '+') resultado = num1 + num2;
  else if (op == '-') resultado = num1 - num2;
  else if (op == '*') resultado = num1 * num2;
  else if (op == '/') {
    if (num2 != 0) resultado = num1 / num2;
    else {
      Serial.println("Erro: divisao por zero!");
      return;
    }
  } else {
    Serial.println("Operador invalido!");
    return;
  }

  Serial.print("Resultado: ");
  Serial.println(resultado);
}

void loop() {
  // nada aqui, roda só uma vez no setup
}
