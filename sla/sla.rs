use std::io;

fn main() {
    let mut input = String::new();

    println!("Digite o primeiro numero:");
    io::stdin().read_line(&mut input).unwrap();
    let num1: f64 = input.trim().parse().unwrap();

    input.clear();
    println!("Digite o operador (+, -, *, /):");
    io::stdin().read_line(&mut input).unwrap();
    let op = input.trim().chars().next().unwrap();

    input.clear();
    println!("Digite o segundo numero:");
    io::stdin().read_line(&mut input).unwrap();
    let num2: f64 = input.trim().parse().unwrap();

    let resultado = match op {
        '+' => num1 + num2,
        '-' => num1 - num2,
        '*' => num1 * num2,
        '/' => {
            if num2 != 0.0 { num1 / num2 }
            else { println!("Erro: divisao por zero!"); return; }
        }
        _ => { println!("Operador invalido!"); return; }
    };

    println!("Resultado: {}", resultado);
}
