-- Active: 1695330752154@@db.ethereallab.app@3306@hg345
CREATE TABLE
    IS601_Users(
        id int auto_increment PRIMARY KEY,
        email VARCHAR(60) unique,
        password VARCHAR(60) not null,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )