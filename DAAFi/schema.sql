DROP TABLE IF EXISTS associates;
DROP TABLE IF EXISTS method;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS transfer;

CREATE TABLE associates (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name text UNIQUE NOT NULL
);

CREATE TABLE method (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name text UNIQUE NOT NULL
);

CREATE TABLE category (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name text UNIQUE NOT NULL
);

CREATE TABLE transfer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date REAL NOT NULL,
  amount DECIMAL(10,2),
  associates_id INTEGER,
  method_id INTEGER,
  category_id INTEGER,
  FOREIGN KEY (associates_id) REFERENCES associates (id),
  FOREIGN KEY (method_id) REFERENCES method (id),
  FOREIGN KEY (category_id) REFERENCES category (id)
);
