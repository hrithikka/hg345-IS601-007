-- Active: 1695330752154@@db.ethereallab.app@3306@hg345
CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    imageURL VARCHAR(255),
    genre VARCHAR(255),
    imdb_id VARCHAR(255),
    title VARCHAR(255),
    imdbrating DECIMAL(5, 2),
    released INT,
    `language` VARCHAR(255),
    `type` VARCHAR(255) NOT NULL,
    synopsis TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);