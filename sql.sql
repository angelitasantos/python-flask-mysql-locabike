USE heroku_b1c0a9f2a3d0817;

CREATE TABLE IF NOT EXISTS admins (
    aid SERIAL NOT NULL,
    aname VARCHAR(50) NOT NULL,
    apassword CHAR(60) NOT NULL,
    amail VARCHAR(50) NOT NULL,
    sitedata BOOLEAN DEFAULT 0,
    companies BOOLEAN DEFAULT 0,
    stores BOOLEAN DEFAULT 0,
    admins BOOLEAN DEFAULT 0,
    acode CHAR(6) DEFAULT 0,
    PRIMARY KEY (amail)
);

SELECT * FROM admins;

CREATE TABLE IF NOT EXISTS companies (
    id SERIAL NOT NULL,
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
    PRIMARY KEY (id)
);

SELECT * FROM companies;
