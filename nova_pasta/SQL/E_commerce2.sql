-- Inserindo dados na tabela de clientes
INSERT INTO clients (first_name, middle_initial, last_name, cpf, address, birth_date)
VALUES 
('Renato', 'A.', 'Silva', '123.456.789-01', 'Rua das Flores, 123', '1985-07-15'),
('Ana', 'B.', 'Santos', '987.654.321-00', 'Av. Paulista, 456', '1990-03-22');

-- Inserindo dados na tabela de pedidos
INSERT INTO orders (id_client, order_status, order_description, shipping_value, payment_cash)
VALUES 
(1, 'em andamento', 'Compra de smartphone e camiseta', 15.0, FALSE),
(2, 'confirmado', 'Compra de boneca', 10.0, TRUE);

-- Inserindo dados na tabela de produtos dos pedidos
INSERT INTO order_products (id_product, id_order, quantity, status)
VALUES 
(1, 1, 1, 'Disponível'),
(3, 1, 1, 'Disponível'),
(2, 2, 1, 'Disponível');