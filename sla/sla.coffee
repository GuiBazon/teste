num1 = parseFloat prompt "Digite o primeiro número:"
op   = prompt "Digite o operador (+, -, *, /):"
num2 = parseFloat prompt "Digite o segundo número:"

if op is "+"
  resultado = num1 + num2
else if op is "-"
  resultado = num1 - num2
else if op is "*"
  resultado = num1 * num2
else if op is "/"
  if num2 isnt 0
    resultado = num1 / num2
  else
    alert "Erro: divisão por zero!"
    throw new Error "Divisão por zero"
else
  alert "Operador inválido!"
  throw new Error "Operador inválido"

alert "Resultado: #{resultado}"
