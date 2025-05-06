CREATE DATABASE ecommerce;
USE ecommerce;

-- Tabela de clientes
CREATE TABLE clients (
    id_client INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    middle_initial CHAR(3),
    last_name VARCHAR(50) NOT NULL,
    cpf VARCHAR(14) NOT NULL UNIQUE,
    address VARCHAR(100) NOT NULL,
    birth_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Índice para otimizar buscas por CPF
CREATE INDEX idx_cpf_client ON clients(cpf);

-- Tabela de produtos
CREATE TABLE products (
    id_product INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    classification_kids BOOLEAN DEFAULT FALSE,
    category ENUM('Eletronico', 'Vestuario', 'Toys', 'Smartphone') NOT NULL,
    rating FLOAT CHECK (rating >= 0 AND rating <= 5),
    size VARCHAR(20),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabela de pedidos
CREATE TABLE orders (
    id_order INT AUTO_INCREMENT PRIMARY KEY,
    id_client INT,
    order_status ENUM('cancelado', 'em andamento', 'confirmado') NOT NULL,
    order_description VARCHAR(255),
    shipping_value FLOAT DEFAULT 10,
    payment_cash BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_order_client FOREIGN KEY (id_client) REFERENCES clients(id_client)
        ON UPDATE CASCADE ON DELETE SET NULL
);

-- Tabela de histórico de pedidos
CREATE TABLE order_history (
    id_history INT AUTO_INCREMENT PRIMARY KEY,
    id_order INT NOT NULL,
    status_change ENUM('cancelado', 'em andamento', 'confirmado') NOT NULL,
    change_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_history_order FOREIGN KEY (id_order) REFERENCES orders(id_order)
        ON UPDATE CASCADE ON DELETE CASCADE
);

-- Tabela de avaliações
CREATE TABLE reviews (
    id_review INT AUTO_INCREMENT PRIMARY KEY,
    id_client INT NOT NULL,
    id_product INT NOT NULL,
    rating FLOAT CHECK (rating >= 0 AND rating <= 5),
    comment TEXT,
    review_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_review_client FOREIGN KEY (id_client) REFERENCES clients(id_client)
        ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_review_product FOREIGN KEY (id_product) REFERENCES products(id_product)
        ON UPDATE CASCADE ON DELETE CASCADE
);

-- Tabela de envios
CREATE TABLE shipping (
    id_shipping INT AUTO_INCREMENT PRIMARY KEY,
    id_order INT NOT NULL,
    carrier_name VARCHAR(100) NOT NULL,
    tracking_number VARCHAR(50) NOT NULL UNIQUE,
    estimated_delivery DATE,
    shipping_status ENUM('pendente', 'em transporte', 'entregue') DEFAULT 'pendente',
    CONSTRAINT fk_shipping_order FOREIGN KEY (id_order) REFERENCES orders(id_order)
        ON UPDATE CASCADE ON DELETE CASCADE
);

-- Tabela de histórico de pagamentos
CREATE TABLE payment_history (
    id_payment_history INT AUTO_INCREMENT PRIMARY KEY,
    id_client INT NOT NULL,
    payment_type ENUM('cartão', 'pix', 'boleto') NOT NULL,
    amount FLOAT NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_payment_history_client FOREIGN KEY (id_client) REFERENCES clients(id_client)
        ON UPDATE CASCADE ON DELETE CASCADE
);