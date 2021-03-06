USE heroku_b1c0a9f2a3d0817;

CREATE TABLE IF NOT EXISTS admins (
    aid INTEGER AUTO_INCREMENT,
    aname VARCHAR(50) NOT NULL,
    apassword CHAR(60) NOT NULL,
    amail VARCHAR(50) NOT NULL,
    sitedata BOOLEAN DEFAULT 0,
    companies BOOLEAN DEFAULT 0,
    stores BOOLEAN DEFAULT 0,
    admins BOOLEAN DEFAULT 0,
    acode CHAR(6) DEFAULT 0,
    active BOOLEAN DEFAULT 1,
    CONSTRAINT PK_admins PRIMARY KEY (aid, amail)
);

SELECT * FROM admins;

CREATE TABLE IF NOT EXISTS companies (
    id INTEGER AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    razaosocial VARCHAR(150),
    tipo CHAR(10) NOT NULL DEFAULT 'JURIDICA',
    cnpj CHAR(20),
    inscest CHAR(20),
    cpf CHAR(11),
    rg CHAR(11),
    endereco VARCHAR(100),
    numero CHAR(10),
    complemento CHAR(20),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    uf CHAR(2),
    cep CHAR(8),
    telefone1 CHAR(15),
    telefone2 CHAR(15),
    email VARCHAR(50),
    ativo BOOLEAN DEFAULT 1,
    CONSTRAINT PK_companies PRIMARY KEY (id, email)
);

SELECT * FROM companies;

CREATE TABLE IF NOT EXISTS stores (
    id INTEGER AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    razaosocial VARCHAR(150),
    tipo CHAR(10) NOT NULL DEFAULT 'JURIDICA',
    cnpj CHAR(20),
    inscest CHAR(20),
    cpf CHAR(11),
    rg CHAR(11),
    endereco VARCHAR(100),
    numero CHAR(10),
    complemento CHAR(20),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    uf CHAR(2),
    cep CHAR(8),
    telefone1 CHAR(15),
    telefone2 CHAR(15),
    email VARCHAR(50),
    ativo BOOLEAN DEFAULT 1,
    id_company INTEGER NOT NULL,
    CONSTRAINT PK_stores PRIMARY KEY (id, id_company, email),
    FOREIGN KEY (id_company)
        REFERENCES companies (id)
);

SELECT * FROM stores;

CREATE TABLE IF NOT EXISTS providers (
    id INTEGER AUTO_INCREMENT,
    grupo VARCHAR(20),
    subgrupo VARCHAR(20),
    nome VARCHAR(50) NOT NULL,
    razaosocial VARCHAR(150),
    tipo CHAR(10) NOT NULL DEFAULT 'JURIDICA',
    cnpj CHAR(20),
    inscest CHAR(20),
    cpf CHAR(11),
    rg CHAR(11),
    endereco VARCHAR(100),
    numero CHAR(10),
    complemento CHAR(20),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    uf CHAR(2),
    cep CHAR(8),
    telefone1 CHAR(15),
    telefone2 CHAR(15),
    email VARCHAR(50),
    ativo BOOLEAN DEFAULT 1,
    id_company INTEGER NOT NULL,
    CONSTRAINT PK_providers PRIMARY KEY (id, id_company, email),
    FOREIGN KEY (id_company)
        REFERENCES companies (id)
);

SELECT * FROM providers;


CREATE TABLE IF NOT EXISTS clients (
    id INTEGER AUTO_INCREMENT,
    grupo VARCHAR(20),
    subgrupo VARCHAR(20),
    nome VARCHAR(50) NOT NULL,
    razaosocial VARCHAR(150),
    tipo CHAR(10) NOT NULL DEFAULT 'JURIDICA',
    cnpj CHAR(20),
    inscest CHAR(20),
    cpf CHAR(11),
    rg CHAR(11),
    endereco VARCHAR(100),
    numero CHAR(10),
    complemento CHAR(20),
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    uf CHAR(2),
    cep CHAR(8),
    telefone1 CHAR(15),
    telefone2 CHAR(15),
    email VARCHAR(50),
    ativo BOOLEAN DEFAULT 1,
    id_company INTEGER NOT NULL,
    CONSTRAINT PK_clients PRIMARY KEY (id, id_company, email),
    FOREIGN KEY (id_company)
        REFERENCES companies (id)
);

SELECT * FROM clients;


CREATE TABLE IF NOT EXISTS items (
    id INTEGER AUTO_INCREMENT,
    grupo VARCHAR(20),
    subgrupo VARCHAR(20),
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(150),
    un CHAR(10),
    tipo CHAR(10) NOT NULL DEFAULT 'PRODUTO',
    codigointerno CHAR(20),
    ean CHAR(13),
    dun CHAR(14),
    cor CHAR(20),
    tamanho CHAR(10),
    largura FLOAT,
    altura FLOAT,
    comprimento FLOAT,
    pesoliquido FLOAT,
    pesobruto FLOAT,
    estoqueminino INTEGER,
    estoquemaximo INTEGER,
    leadtime INTEGER,
    loteminino INTEGER,
    lotemaximo INTEGER,
    ncm CHAR(20),
    cest CHAR(20),
    classificacao CHAR(20),
    ativo BOOLEAN DEFAULT 1,
    id_company INTEGER NOT NULL,
    CONSTRAINT PK_clients PRIMARY KEY (id, id_company, nome),
    FOREIGN KEY (id_company)
        REFERENCES companies (id)
);

SELECT * FROM items;


CREATE TABLE IF NOT EXISTS brands (
    id INTEGER AUTO_INCREMENT,
    description VARCHAR(20) NOT NULL,
    CONSTRAINT PK_brands PRIMARY KEY (id, description)
);

SELECT * FROM brands;


CREATE TABLE IF NOT EXISTS categories (
    id INTEGER AUTO_INCREMENT,
    description VARCHAR(20) NOT NULL,
    CONSTRAINT PK_categories PRIMARY KEY (id, description)
);

SELECT * FROM categories;


CREATE TABLE IF NOT EXISTS products (
    id INTEGER AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(150),
    price FLOAT,
    discount FLOAT,
    stock INTEGER,
    colors VARCHAR(50),
    image LONGBLOB,
    id_brand INTEGER NOT NULL,
    id_category INTEGER NOT NULL,
    id_company INTEGER NOT NULL,
    CONSTRAINT PK_products PRIMARY KEY (id, id_company, name),
    FOREIGN KEY (id_brand)
        REFERENCES brands (id),
    FOREIGN KEY (id_category)
        REFERENCES categories (id),
    FOREIGN KEY (id_company)
        REFERENCES companies (id)
);

SELECT * FROM products;