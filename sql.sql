USE heroku_b1c0a9f2a3d0817;

CREATE TABLE IF NOT EXISTS admins (
    aid SERIAL,
    aname VARCHAR(50) NOT NULL,
    apassword CHAR(60) NOT NULL,
    amail VARCHAR(50) NOT NULL,
    sitedata BOOLEAN DEFAULT 0,
    companies BOOLEAN DEFAULT 0,
    stores BOOLEAN DEFAULT 0,
    admins BOOLEAN DEFAULT 0,
    PRIMARY KEY (amail)
);

SELECT * FROM admins;