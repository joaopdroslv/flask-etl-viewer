CREATE DATABASE IF NOT EXISTS sales_data_pipeline;

USE sales_data_pipeline;

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS buyers (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    sex ENUM('M', 'F') NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL,
    contact VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS sellers (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    sex ENUM('M', 'F') NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL,
    contact VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    product_id INTEGER NOT NULL,
    buyer_id INTEGER NOT NULL,
    seller_id INTEGER NOT NULL,
    sale_date DATE NOT NULL,
    units_sold INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    payment_method ENUM(
        'Credit Card (Visa)', 'Credit Card (MasterCard)', 'Credit Card (American Express)', 
        'Debit Card', 'Pix', 'Cash', 'Bank Transfer', 'Cryptocurrency (Bitcoin)', 
        'Cryptocurrency (Ethereum)', 'PayPal', 'Google Pay', 'Apple Pay') NOT NULL,
    discount BOOLEAN NOT NULL,
    discount_perc INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (buyer_id) REFERENCES buyers(id) ON DELETE CASCADE,
    FOREIGN KEY (seller_id) REFERENCES sellers(id) ON DELETE CASCADE
);
