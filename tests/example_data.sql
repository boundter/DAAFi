INSERT INTO contact (name) VALUES ("Amazon"), ("ebay");

INSERT INTO payment_method (name) VALUES ("Cash"), ("Credit Card");

INSERT INTO category (name) VALUES ("Fun"), ("Work");

INSERT INTO money_transfer (transaction_date, amount, contact_id,
                            payment_method_id, category_id)
VALUES
  (1542727811, 50.00, 1, 1, 1),
  (1542717811, 30.00, 1, 2, 1),
  (1542719811, 20.00, 2, 2, 1);
