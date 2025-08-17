program calculadora
  implicit none
  real :: num1, num2, resultado
  character :: op

  print *, "Digite o primeiro numero:"
  read *, num1
  print *, "Digite o segundo numero:"
  read *, num2
  print *, "Escolha a operacao (+ - * /):"
  read *, op

  select case (op)
  case ('+')
     resultado = num1 + num2
  case ('-')
     resultado = num1 - num2
  case ('*')
     resultado = num1 * num2
  case ('/')
     resultado = num1 / num2
  case default
     print *, "Operacao invalida."
     stop
  end select

  print *, "Resultado:", resultado
end program calculadora
