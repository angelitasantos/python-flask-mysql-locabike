INSERT INTO admins(aname, apassword, amail, sitedata, companies, stores, admins) 
VALUES('Admin', '$2b$12$vE2qFBLAuBWW8tI/6mH9uurZaUEmUpPvUZ4lDH3NsFJ32j251gkPa', 'admin@admin.com', 1, 1, 1, 1);

INSERT INTO companies(id, nome, razaosocial, email) 
VALUES(1, 'COMPANY', 'COMPANY NAME', 'company@company.com');

INSERT INTO stores(id, nome, razaosocial, email, id_company) 
VALUES(1, 'STORE', 'STORE NAME', 'store@store.com', 1);

INSERT INTO providers(id, nome, razaosocial, email, id_company) 
VALUES(1, 'PROVIDER', 'PROVIDER NAME', 'provider@provider.com', 1);

INSERT INTO clients(id, nome, razaosocial, email, id_company) 
VALUES(1, 'CLIENT', 'CLIENT NAME', 'client@client.com', 1);