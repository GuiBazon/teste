#!/bin/bash

read -p "Digite uma operacao (+ - * /): " op
read -p "Digite o primeiro numero: " a
read -p "Digite o segundo numero: " b

case $op in
  +) res=$(echo "$a + $b" | bc) ;;
  -) res=$(echo "$a - $b" | bc) ;;
  \*) res=$(echo "$a * $b" | bc) ;;
  /) 
    if [ "$b" -ne 0 ]; then
      res=$(echo "scale=2; $a / $b" | bc)
    else
      res="Erro: divisao por zero!"
    fi ;;
  *) res="Operacao invalida!" ;;
esac

echo "Resultado: $res"
