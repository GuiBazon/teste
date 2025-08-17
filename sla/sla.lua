io.write("Digite o primeiro numero: ")
local num1 = tonumber(io.read())

io.write("Digite o operador (+, -, *, /): ")
local op = io.read()

io.write("Digite o segundo numero: ")
local num2 = tonumber(io.read())

local resultado

if op == "+" then
    resultado = num1 + num2
elseif op == "-" then
    resultado = num1 - num2
elseif op == "*" then
    resultado = num1 * num2
elseif op == "/" then
    if num2 ~= 0 then
        resultado = num1 / num2
    else
        print("Erro: divisao por zero!")
        os.exit()
    end
else
    print("Operador invalido!")
    os.exit()
end

print("Resultado: " .. resultado)
