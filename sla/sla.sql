-- Tabela Cliente
CREATE TABLE Cliente (
    cpf CHAR(11) PRIMARY KEY,
    telefone VARCHAR(15),
    nome VARCHAR(100),
    logradouro VARCHAR(100),
    numero VARCHAR(10),
    complemento VARCHAR(50),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    estado CHAR(2),
    cep CHAR(8),
    referencia VARCHAR(100)
);

-- Tabela Pizza
CREATE TABLE Pizza (
    id_pizza INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    valor DECIMAL(10,2)
);

-- Tabela Pedido
CREATE TABLE Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    hora TIME,
    valor DECIMAL(10,2),
    fk_id_cliente CHAR(11),
    FOREIGN KEY (fk_id_cliente) REFERENCES Cliente(cpf)
);

-- Tabela Pizzas_do_Pedido (tabela associativa)
-- Serve pra fazer uma relacao N:N, como muitas pizzas em muitos pedidos
CREATE TABLE Pizzas_do_Pedido (
    id_pizzas_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fk_id_pedido INT,
    fk_id_pizza INT,
    quantidade INT,
    valor DECIMAL(10,2),
    FOREIGN KEY (fk_id_pedido) REFERENCES Pedido(id_pedido),
    FOREIGN KEY (fk_id_pizza) REFERENCES Pizza(id_pizza)
);

