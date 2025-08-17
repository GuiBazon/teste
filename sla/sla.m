op = input('Digite uma operacao (+ - * /): ', 's');
a = input('Digite o primeiro numero: ');
b = input('Digite o segundo numero: ');

switch op
    case '+'
        resultado = a + b;
    case '-'
        resultado = a - b;
    case '*'
        resultado = a * b;
    case '/'
        if b ~= 0
            resultado = a / b;
        else
            resultado = 'Erro: divisao por zero!';
        end
    otherwise
        resultado = 'Operacao invalida!';
end

disp(['Resultado: ', num2str(resultado)])
