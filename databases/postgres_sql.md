# Denormalized Products

CREATE TABLE Products (
    id int,
    name varchar(255),
    price float,
    description varchar(255),
    department varchar(255)
);

INSERT INTO Products (id, name, price, description, department)
VALUES (1, 'Apple', 1.99, 'Delicious Apple', 'Produce');

INSERT INTO Products (id, name, price, description, department)
VALUES (2, 'Banana', 3.49, 'Bunch of Bananas', 'Produce');

INSERT INTO Products (id, name, price, description, department)
VALUES (3, 'Bread', 3.99, 'Loaf of whole wheat', 'Bakery');

INSERT INTO Products (id, name, price, description, department)
VALUES (4, 'Cheddar', 2.79, 'Sliced cheddar', 'Deli');

# Normalized Products and Departments

CREATE TABLE Products (
    id int,
    department_id int,
    name varchar(255),
    price float,
    description varchar(255)
);

INSERT INTO Products (id, department_id, name, price, description)
VALUES (1, 1, 'Apple', 1.99, 'Delicious Apple');

INSERT INTO Products (id, department_id, name, price, description)
VALUES (2, 1, 'Banana', 3.49, 'Bunch of Bananas');

INSERT INTO Products (id, department_id, name, price, description)
VALUES (3, 2, 'Bread', 3.99, 'Loaf of whole wheat');

INSERT INTO Products (id, department_id, name, price, description)
VALUES (4, 3, 'Cheddar', 2.79, 'Sliced cheddar');

CREATE TABLE Departments (
    id int,
    name varchar(255),
    description varchar(255)
);

INSERT INTO Departments (id, name, description)
VALUES (1, 'Produce', 'Healthy stuff!');

INSERT INTO Departments (id, name, description)
VALUES (2, 'Bakery', 'Breads and goodies');

INSERT INTO Departments (id, name, description)
VALUES (3, 'Deli', 'Meats, cheeses, etc');


# Join Query

SELECT p.name, d.name, price
FROM products p
FULL OUTER JOIN departments d ON d.id = p.department_id;
