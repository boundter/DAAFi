DROP TABLE IF EXISTS contact;
DROP TABLE IF EXISTS payment_method;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS money_transfer;

CREATE TABLE contact (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name text UNIQUE NOT NULL
);

CREATE TABLE payment_method (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name text UNIQUE NOT NULL
);

CREATE TABLE category (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name text UNIQUE NOT NULL
);

CREATE TABLE money_transfer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date REAL NOT NULL,
  amount DECIMAL(10,2),
  contact_id INTEGER,
  payment_method_id INTEGER,
  category_id INTEGER,
  FOREIGN KEY (contact_id) REFERENCES contact (id),
  FOREIGN KEY (payment_method_id) REFERENCES payment_method (id),
  FOREIGN KEY (category_id) REFERENCES category (id)
);
