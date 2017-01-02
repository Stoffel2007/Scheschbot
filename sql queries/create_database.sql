CREATE DATABASE IF NOT EXISTS scheschbot
DEFAULT CHARACTER SET = 'utf16';


CREATE TABLE IF NOT EXISTS scheschbot.users
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    telegram_id INT NOT NULL,
    like_percentage INT NOT NULL DEFAULT 50,
    first_name CHAR(64) NOT NULL,
    last_name CHAR(64),
    username CHAR(64),
    is_admin BOOLEAN NOT NULL DEFAULT 0
)
DEFAULT CHARACTER SET = 'utf16'


CREATE TABLE IF NOT EXISTS scheschbot.word_types
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name CHAR(64) NOT NULL
)
DEFAULT CHARACTER SET = 'utf16'


CREATE TABLE IF NOT EXISTS scheschbot.genus
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    article CHAR(3) NOT NULL
)
DEFAULT CHARACTER SET = 'utf16'


CREATE TABLE IF NOT EXISTS scheschbot.aggronymes
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    word CHAR(64) NOT NULL,
    type_id INT NOT NULL,
    genus_id INT,
    votes INT NOT NULL DEFAULT 1,
    FOREIGN KEY (type_id) REFERENCES scheschbot.word_types (id),
    FOREIGN KEY (genus_id) REFERENCES scheschbot.genus (id)
)
DEFAULT CHARACTER SET = 'utf16'