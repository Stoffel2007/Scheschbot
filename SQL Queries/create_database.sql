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
    FOREIGN KEY (type_id) REFERENCES scheschbot.word_types (id) ON DELETE CASCADE,
    FOREIGN KEY (genus_id) REFERENCES scheschbot.genus (id) ON DELETE CASCADE
)
DEFAULT CHARACTER SET = 'utf16'


CREATE TABLE IF NOT EXISTS scheschbot.answer_input
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    input CHAR(64) NOT NULL,
    text_before BOOLEAN NOT NULL DEFAULT 0,
    text_after BOOLEAN NOT NULL DEFAULT 0,
    is_question BOOLEAN NOT NULL DEFAULT 0,
    contains_specialchars BOOLEAN NOT NULL DEFAULT 0
)
DEFAULT CHARACTER SET = 'utf16'


CREATE TABLE IF NOT EXISTS scheschbot.answer_output
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    output CHAR(64) NOT NULL
)
DEFAULT CHARACTER SET = 'utf16'


CREATE TABLE IF NOT EXISTS scheschbot.answer_relations
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    input_id INT NOT NULL,
    output_id INT NOT NULL,
    previous_output_id INT DEFAULT NULL,
    FOREIGN KEY (input_id) REFERENCES scheschbot.answer_input (id) ON DELETE CASCADE,
    FOREIGN KEY (output_id) REFERENCES scheschbot.answer_output (id) ON DELETE CASCADE,
    FOREIGN KEY (previous_output_id) REFERENCES scheschbot.answer_output (id) ON DELETE CASCADE
)
DEFAULT CHARACTER SET = 'utf16'