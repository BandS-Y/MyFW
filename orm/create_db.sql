
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS person;
CREATE TABLE person (
    idperson INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    firstname  VARCHAR (32),
    lastname VARCHAR (32),
    email VARCHAR (32),
    telephone VARCHAR (12));
INSERT INTO person (firstname, lastname, email, telephone) VALUES ('Ivan', 'Ivanov', 'abc@mail.ru', '+79132312345');
INSERT INTO person (firstname, lastname, email, telephone) VALUES ('Petr', 'Petrov', 'bcd@mail.ru', '+79131231234');
INSERT INTO person (firstname, lastname, email, telephone) VALUES ('Nikolay', 'Sidor', 'cde@gmail.ru', '+79133456778');
INSERT INTO person (firstname, lastname, email, telephone) VALUES ('Olga', 'Odina', 'efg@gmail.ru', '+79131234567');
INSERT INTO person (firstname, lastname, email, telephone) VALUES ('Fedorov', 'Fedor', 'sfg@gmail.ru', '+73218526598');

DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    idcategory INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    categoryname VARCHAR (32));
INSERT INTO categories (categoryname) VALUES ('Python');
INSERT INTO categories (categoryname) VALUES ('Java');
INSERT INTO categories (categoryname) VALUES ('JavaScript');

DROP TABLE IF EXISTS levels;
CREATE TABLE levels (
    idlevel INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    levelname VARCHAR (32));
INSERT INTO levels (levelname) VALUES ('junior');
INSERT INTO levels (levelname) VALUES ('middle');
INSERT INTO levels (levelname) VALUES ('senior');

DROP TABLE IF EXISTS types;
CREATE TABLE types (
    idtype INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    typename VARCHAR (32));
INSERT INTO types (typename) VALUES ('online');
INSERT INTO types (typename) VALUES ('offline');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
