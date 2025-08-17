print "Digite uma operacao (+ - * /): ";
my $op = <STDIN>;
chomp($op);

print "Digite dois numeros: ";
my $a = <STDIN>;
my $b = <STDIN>;

my $res;
if ($op eq "+") { $res = $a + $b; }
elsif ($op eq "-") { $res = $a - $b; }
elsif ($op eq "*") { $res = $a * $b; }
elsif ($op eq "/") { 
    $res = $b != 0 ? $a / $b : "Erro: divisao por zero!";
} else {
    $res = "Operacao invalida!";
}

print "Resultado: $res\n";
