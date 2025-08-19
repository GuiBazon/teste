# Aula de Python - Conceitos Fundamentais

# 1. TIPOS DE DADOS BÁSICOS
inteiro = 10              # int
real = 3.14               # float
texto = "Hello"           # string
booleano = True           # bool

lista = [1, 2, 3]         # list
conjunto = {1, 2, 2, 3}   # set (não aceita repetição)
dicionario = {"nome": "Gui", "idade": 17}  # dict

print(inteiro, real, texto, booleano)
print(lista, conjunto, dicionario)

# ------------------------------------------------------
# 2. OPERADORES
x, y = 5, 2
print(x + y)   # soma
print(x - y)   # subtração
print(x * y)   # multiplicação
print(x / y)   # divisão (float)
print(x // y)  # divisão inteira
print(x % y)   # resto
print(x ** y)  # potência

# Comparações retornam True/False
print(x == y, x > y, x != y)

# ------------------------------------------------------
# 3. CONTROLE DE FLUXO
if x > y:
    print("x é maior que y")
elif x == y:
    print("x é igual a y")
else:
    print("x é menor que y")

# Loop for
for i in range(5):
    print("for:", i)

# Loop while
contador = 0
while contador < 3:
    print("while:", contador)
    contador += 1

# ------------------------------------------------------
# 4. FUNÇÕES
def soma(a, b):
    return a + b

print("Função soma:", soma(3, 4))

# ------------------------------------------------------
# 5. ESTRUTURAS DE DADOS
numeros = [10, 20, 30]
numeros.append(40)
print("Lista:", numeros)

# Dicionário
aluno = {"nome": "Ana", "nota": 9.5}
print("Nome:", aluno["nome"])

# ------------------------------------------------------
# 6. ENTRADA E SAÍDA
# entrada = input("Digite algo: ")
# print("Você digitou:", entrada)

# ------------------------------------------------------
# 7. TRATAMENTO DE ERROS
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Erro: divisão por zero")

# ------------------------------------------------------
# 8. ORIENTAÇÃO A OBJETOS
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar(self):
        print(f"Oi, eu sou {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Gui", 17)
p1.falar()

# ------------------------------------------------------
# 9. MÓDULOS / BIBLIOTECAS
import math
print("Raiz quadrada de 16:", math.sqrt(16))

# ------------------------------------------------------
# 10. PARADIGMAS
# Imperativo
x = 10
y = 20
print(x + y)

# Funcional (map, filter, reduce)
valores = [1, 2, 3, 4]
dobro = list(map(lambda n: n * 2, valores))
print("Dobro:", dobro)

# OO já vimos com a classe Pessoa
