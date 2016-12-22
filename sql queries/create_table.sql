CREATE TABLE IF NOT EXISTS scheschbot.users
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    telegram_id INT NOT NULL,
    like_percentage INT NOT NULL DEFAULT 50,
    first_name CHAR(64) NOT NULL,
    last_name CHAR(64),
    username CHAR(64)
)
DEFAULT CHARACTER SET = 'utf16'

INSERT INTO scheschbot.users
(telegram_id, like_percentage, first_name, last_name, username)
VALUES
(105131864, 60, 'Joschi', NULL, NULL),
(54185905, 48, 'Alex', 'Ey', NULL),
(44867338, 10, 'Fredi', 'B', 'Oenner'),
(213190902, 28, 'Pascal', 'Rögner', NULL),
(82613330, 69, 'Wilhelmina', 'Fuchs', NULL),
(72111412, 88, 'Stoffel', 'Zink', 'Stuffla')


CREATE TABLE IF NOT EXISTS scheschbot.word_types
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name CHAR(64) NOT NULL
)
DEFAULT CHARACTER SET = 'utf16'

INSERT INTO scheschbot.word_types
(name)
VALUES
('Adjektiv'),
('Nomen')


CREATE TABLE IF NOT EXISTS scheschbot.aggronymes
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    word CHAR(64) NOT NULL,
    type_id INT NOT NULL,
    FOREIGN KEY (type_id) REFERENCES word_types (id)
)
DEFAULT CHARACTER SET = 'utf16'

INSERT INTO scheschbot.aggronymes
(word, type_id)
VALUES
('abartig', 1),
('assozial', 1),
('ägglhaft', 1),
('balancelos', 1),
('belanglos', 1),
('charismatisch', 1),
('deppert', 1),
('egglhaft', 1),
('ersetzbar', 1),
('frauenfeindlich', 1),
('hochnäsig', 1),