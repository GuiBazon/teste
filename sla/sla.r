op <- readline("Digite uma operacao (+ - * /): ")
a <- as.numeric(readline("Digite o primeiro numero: "))
b <- as.numeric(readline("Digite o segundo numero: "))

resultado <- switch(op,
  "+" = a + b,
  "-" = a - b,
  "*" = a * b,
  "/" = if (b != 0) a / b else "Erro: divisao por zero!",
  "Operacao invalida!"
)

cat("Resultado:", resultado, "\n")
