<?php
echo "Digite o primeiro número: ";
$a = (float)trim(fgets(STDIN));

echo "Digite o operador (+, -, *, /): ";
$op = trim(fgets(STDIN));

echo "Digite o segundo número: ";
$b = (float)trim(fgets(STDIN));

$result = null;

switch ($op) {
    case '+':
        $result = $a + $b;
        break;
    case '-':
        $result = $a - $b;
        break;
    case '*':
        $result = $a * $b;
        break;
    case '/':
        if ($b != 0) {
            $result = $a / $b;
        } else {
            echo "Erro: divisão por zero!\n";
            exit;
        }
        break;
    default:
        echo "Operador inválido!\n";
        exit;
}

echo "Resultado: $result\n";
?>
