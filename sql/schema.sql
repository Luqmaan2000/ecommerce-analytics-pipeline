CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    signup_date DATE,
    country TEXT,
    currency TEXT
);

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    order_date DATE,
    quantity INTEGER,
    total_amount_local REAL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
