CREATE DATABASE IF NOT EXISTS ecommerce;

USE ecommerce;

CREATE TABLE cliente (

    ID_Cliente INT PRIMARY KEY,
    Nome VARCHAR(50),
    Email VARCHAR(100),
    Data_Cadastro DATE
    
);

CREATE TABLE produto (

    ID_Produto INT PRIMARY KEY,
    Nome_Produto VARCHAR(50),
    Categoria VARCHAR(50),
    Preco DECIMAL(10,2),
    Estoque INT
    
);

CREATE TABLE pedido (

    ID_Pedido INT PRIMARY KEY,
    ID_Cliente INT,
    Data_Pedido DATE,
    Total DECIMAL(10,2),
    FOREIGN KEY (ID_Cliente) REFERENCES cliente(ID_Cliente)
    
);

CREATE TABLE item (

    ID_Item INT PRIMARY KEY,
    ID_Pedido INT,
    ID_Produto INT,
    Quantidade INT,
    Preco_Unitario DECIMAL(10,2),
    FOREIGN KEY (ID_Pedido) REFERENCES pedido(ID_Pedido),
    FOREIGN KEY (ID_Produto) REFERENCES produto(ID_Produto)

);