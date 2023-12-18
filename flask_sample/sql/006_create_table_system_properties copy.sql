-- Active: 1695330752154@@db.ethereallab.app@3306@hg345
CREATE TABLE
    IS601_System_Properties (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(40) UNIQUE NOT NULL,
        value TEXT,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );