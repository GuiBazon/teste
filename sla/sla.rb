print "Digite o primeiro numero: "
num1 = gets.to_f

print "Digite o operador (+, -, *, /): "
op = gets.chomp

print "Digite o segundo numero: "
num2 = gets.to_f

if op == "+"
  resultado = num1 + num2
elsif op == "-"
  resultado = num1 - num2
elsif op == "*"
  resultado = num1 * num2
elsif op == "/"
  if num2 != 0
    resultado = num1 / num2
  else
    puts "Erro: divisao por zero!"
    exit
  end
else
  puts "Operador invalido!"
  exit
end

puts "Resultado: #{resultado}"
