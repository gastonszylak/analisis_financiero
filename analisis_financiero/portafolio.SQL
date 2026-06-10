CREATE DATABASE IF NOT EXISTS portafolio;
USE portafolio;
CREATE TABLE portafolio (
    id_instrumento INT AUTO_INCREMENT PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    tipo_activo VARCHAR(50) NOT NULL,
    riesgo VARCHAR(20) NOT NULL
);
CREATE TABLE movimientos (
   id_movimiento INT AUTO_INCREMENT PRIMARY KEY,
   id_instrumento INT,
   fecha_compra DATE NOT NULL,
   cantidad INT NOT NULL,
    precio_compra DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_instrumento) REFERENCES portafolio(id_instrumento)

);

 #INSERCION DE DATOS
INSERT INTO portafolio (ticker, tipo_activo, riesgo) VALUES
('AAPL', 'Acciones', 'Alto'),
('GOOGL', 'Acciones', 'Alto'),
('TSLA', 'Acciones', 'Alto'),
('AMZN', 'Acciones', 'Alto'),
('MSFT', 'Acciones', 'Alto');
INSERT INTO movimientos (id_instrumento, fecha_compra, cantidad, precio_compra) VALUES
(1, '2023-01-15', 10, 150.00),
(2, '2023-02-20', 5, 2800.00),
(3, '2023-03-10', 8, 700.00),
(4, '2023-04-05', 3, 3300.00),
(5, '2023-05-12', 12, 250.00);
