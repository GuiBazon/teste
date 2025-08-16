num1 = float(input("Digite o primeiro numero: "))
op = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo numero: "))

if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisao por zero!")
        exit()
else:
    print("Operador invalido!")
    exit()

print("Resultado:", resultado)
