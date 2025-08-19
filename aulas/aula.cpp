// Aula de C++ - Conceitos Fundamentais
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
using namespace std;

// Função (fora da main)
int soma(int a, int b) {
    return a + b;
}

// Classe Pessoa
class Pessoa {
public:
    string nome;
    int idade;

    Pessoa(string n, int i) {
        nome = n;
        idade = i;
    }

    void falar() {
        cout << "Oi, eu sou " << nome << " e tenho " << idade << " anos." << endl;
    }
};

int main() {
    // 1. TIPOS DE DADOS BÁSICOS
    int inteiro = 10;
    double real = 3.14;
    string texto = "Hello";
    bool booleano = true;

    vector<int> lista = {1, 2, 3}; // vetor (lista)
    set<int> conjunto = {1, 2, 2, 3}; // set (não aceita repetição)
    map<string, int> dicionario; // map (dicionário)
    dicionario["idade"] = 17;

    cout << inteiro << " " << real << " " << texto << " " << booleano << endl;

    // ------------------------------------------------------
    // 2. OPERADORES
    int x = 5, y = 2;
    cout << x + y << endl;
    cout << x - y << endl;
    cout << x * y << endl;
    cout << x / y << endl; // divisão inteira
    cout << x % y << endl; // resto
    cout << pow(x, y) << endl; // potência

    cout << (x == y) << " " << (x > y) << " " << (x != y) << endl;

    // ------------------------------------------------------
    // 3. CONTROLE DE FLUXO
    if (x > y) {
        cout << "x é maior que y" << endl;
    } else if (x == y) {
        cout << "x é igual a y" << endl;
    } else {
        cout << "x é menor que y" << endl;
    }

    // Loop for
    for (int i = 0; i < 5; i++) {
        cout << "for: " << i << endl;
    }

    // Loop while
    int contador = 0;
    while (contador < 3) {
        cout << "while: " << contador << endl;
        contador++;
    }

    // ------------------------------------------------------
    // 4. FUNÇÕES
    cout << "Função soma: " << soma(3, 4) << endl;

    // ------------------------------------------------------
    // 5. ESTRUTURAS DE DADOS
    vector<int> numeros = {10, 20, 30};
    numeros.push_back(40);
    cout << "Lista: ";
    for (int n : numeros) cout << n << " ";
    cout << endl;

    map<string, double> aluno;
    aluno["nota"] = 9.5;
    aluno["idade"] = 16;
    cout << "Nota: " << aluno["nota"] << endl;

    // ------------------------------------------------------
    // 7. TRATAMENTO DE ERROS
    try {
        int a = 10 / 0; // isso dá erro
        cout << a << endl;
    } catch (exception& e) {
        cout << "Erro: " << e.what() << endl;
    }

    // ------------------------------------------------------
    // 8. ORIENTAÇÃO A OBJETOS
    Pessoa p1("Gui", 17);
    p1.falar();

    // ------------------------------------------------------
    // 9. MÓDULOS / BIBLIOTECAS
    cout << "Raiz quadrada de 16: " << sqrt(16) << endl;

    // ------------------------------------------------------
    // 10. PARADIGMAS
    // Imperativo
    x = 10;
    y = 20;
    cout << x + y << endl;

    // Funcional (usando lambda e transform)
    vector<int> valores = {1, 2, 3, 4};
    vector<int> dobro;
    for (int n : valores) {
        dobro.push_back(n * 2);
    }
    cout << "Dobro: ";
    for (int d : dobro) cout << d << " ";
    cout << endl;

    return 0;
}
