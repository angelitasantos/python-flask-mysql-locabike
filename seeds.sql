INSERT INTO admins(aname, apassword, amail, sitedata, companies, stores, admins) 
VALUES('Admin', '$2b$12$vE2qFBLAuBWW8tI/6mH9uurZaUEmUpPvUZ4lDH3NsFJ32j251gkPa', 'admin@admin.com', 1, 1, 1, 1);

INSERT INTO companies(id, nome, razaosocial, email) 
VALUES  (1, 'COMPANY 01', 'COMPANY NAME 01', 'company1@company.com'),
        (2, 'COMPANY 02', 'COMPANY NAME 02', 'company2@company.com');

INSERT INTO stores(id, nome, razaosocial, email, id_company) 
VALUES  (1, 'STORE 01', 'STORE NAME 01', 'store1@store.com', 1),
        (2, 'STORE 02', 'STORE NAME 02', 'store2@store.com', 1),
        (3, 'STORE 03', 'STORE NAME 03', 'store3@store.com', 2),
        (4, 'STORE 04', 'STORE NAME 04', 'store4@store.com', 2);

INSERT INTO providers(id, nome, razaosocial, email, id_company) 
VALUES  (1, 'PROVIDER 01', 'PROVIDER NAME 01', 'provider1@provider.com', 1),
        (2, 'PROVIDER 02', 'PROVIDER NAME 02', 'provider2@provider.com', 1),
        (3, 'PROVIDER 03', 'PROVIDER NAME 03', 'provider3@provider.com', 2),
        (4, 'PROVIDER 04', 'PROVIDER NAME 04', 'provider4@provider.com', 2);

INSERT INTO clients(id, nome, razaosocial, email, id_company) 
VALUES  (1, 'CLIENT 01', 'CLIENT NAME 01', 'client1@client.com', 1),
        (2, 'CLIENT 02', 'CLIENT NAME 02', 'client2@client.com', 1),
        (3, 'CLIENT 03', 'CLIENT NAME 03', 'client3@client.com', 2),
        (4, 'CLIENT 04', 'CLIENT NAME 04', 'client4@client.com', 2);

INSERT INTO brands(id, description)
VALUES  (1, 'BRAND 01'),
        (2, 'BRAND 02');

INSERT INTO categories(id, description)
VALUES  (1, 'CATEGORY 01'),
        (2, 'CATEGORY 02');

INSERT INTO products(id, name, price, stock, colors, id_brand, id_category, id_company) 
VALUES  (1, 'PRODUCT 01', 18.50, 27, 'AMARELO', 1, 1, 1),
        (2, 'PRODUCT 02', 25.75, 12, 'VERDE', 1, 2, 2),
        (3, 'PRODUCT 03', 12.68, 32, 'VERMELHO', 2, 1, 2),
        (4, 'PRODUCT 04', 31.15, 15, 'LARANJA', 1, 1, 2);