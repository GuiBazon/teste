# Calculadora simples em Julia

println("Digite o primeiro número:")
a = parse(Float64, readline())

println("Digite o operador (+, -, *, /):")
op = readline()

println("Digite o segundo número:")
b = parse(Float64, readline())

result = 0.0

if op == "+"
    result = a + b
elseif op == "-"
    result = a - b
elseif op == "*"
    result = a * b
elseif op == "/"
    result = b != 0 ? a / b : error("Divisão por zero!")
else
    error("Operador inválido")
end

println("Resultado: ", result)
