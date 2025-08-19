// Aula de Java - Conceitos Fundamentais

public class AulaJava {
    public static void main(String[] args) {
        // 1. TIPOS DE DADOS BÁSICOS
        int inteiro = 10;
        double real = 3.14;
        String texto = "Hello";
        boolean booleano = true;

        int[] lista = {1, 2, 3};
        java.util.HashSet<Integer> conjunto = new java.util.HashSet<>();
        conjunto.add(1);
        conjunto.add(2);
        conjunto.add(2);
        conjunto.add(3);

        java.util.HashMap<String, Object> dicionario = new java.util.HashMap<>();
        dicionario.put("nome", "Gui");
        dicionario.put("idade", 17);

        System.out.println(inteiro + " " + real + " " + texto + " " + booleano);
        System.out.println(java.util.Arrays.toString(lista));
        System.out.println(conjunto);
        System.out.println(dicionario);

        // ------------------------------------------------------
        // 2. OPERADORES
        int x = 5, y = 2;
        System.out.println(x + y);
        System.out.println(x - y);
        System.out.println(x * y);
        System.out.println(x / y);
        System.out.println(x % y);
        System.out.println(Math.pow(x, y));

        System.out.println(x == y);
        System.out.println(x > y);
        System.out.println(x != y);

        // ------------------------------------------------------
        // 3. CONTROLE DE FLUXO
        if (x > y) {
            System.out.println("x é maior que y");
        } else if (x == y) {
            System.out.println("x é igual a y");
        } else {
            System.out.println("x é menor que y");
        }

        // Loop for
        for (int i = 0; i < 5; i++) {
            System.out.println("for: " + i);
        }

        // Loop while
        int contador = 0;
        while (contador < 3) {
            System.out.println("while: " + contador);
            contador++;
        }

        // ------------------------------------------------------
        // 4. FUNÇÕES
        System.out.println("Função soma: " + soma(3, 4));

        // ------------------------------------------------------
        // 5. ESTRUTURAS DE DADOS
        java.util.ArrayList<Integer> numeros = new java.util.ArrayList<>();
        numeros.add(10);
        numeros.add(20);
        numeros.add(30);
        numeros.add(40);
        System.out.println("Lista: " + numeros);

        java.util.HashMap<String, Object> aluno = new java.util.HashMap<>();
        aluno.put("nome", "Ana");
        aluno.put("nota", 9.5);
        System.out.println("Nome: " + aluno.get("nome"));

        // ------------------------------------------------------
        // 7. TRATAMENTO DE ERROS
        try {
            System.out.println(10 / 0);
        } catch (ArithmeticException e) {
            System.out.println("Erro: divisão por zero");
        }

        // ------------------------------------------------------
        // 8. ORIENTAÇÃO A OBJETOS
        Pessoa p1 = new Pessoa("Gui", 17);
        p1.falar();

        // ------------------------------------------------------
        // 9. MÓDULOS / BIBLIOTECAS
        System.out.println("Raiz quadrada de 16: " + Math.sqrt(16));

        // ------------------------------------------------------
        // 10. PARADIGMAS
        // Imperativo
        x = 10;
        y = 20;
        System.out.println(x + y);

        // Funcional (Java Streams)
        java.util.List<Integer> valores = java.util.Arrays.asList(1, 2, 3, 4);
        java.util.List<Integer> dobro = valores.stream().map(n -> n * 2).toList();
        System.out.println("Dobro: " + dobro);
    }

    // Função (método estático)
    public static int soma(int a, int b) {
        return a + b;
    }
}

// Classe Pessoa
class Pessoa {
    String nome;
    int idade;

    Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    void falar() {
        System.out.println("Oi, eu sou " + nome + " e tenho " + idade + " anos.");
    }
}
