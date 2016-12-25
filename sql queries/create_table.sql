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

INSERT INTO scheschbot.users
(telegram_id, like_percentage, first_name, last_name, username, is_admin)
VALUES
(105131864, 60, 'Joschi', NULL, NULL, 0),
(54185905, 48, 'Alex', 'Ey', NULL, 1),
(44867338, 10, 'Fredi', 'B', 'Oenner', 0),
(213190902, 28, 'Pascal', 'Rögner', NULL, 0),
(82613330, 69, 'Wilhelmina', 'Fuchs', NULL, 0),
(72111412, 88, 'Stoffel', 'Zink', 'Stuffla', 1),
(33545033, 88, 'Andi', NULL, 'Der_Batman', 1)


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


CREATE TABLE IF NOT EXISTS scheschbot.genus
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    article CHAR(3) NOT NULL
)
DEFAULT CHARACTER SET = 'utf16'

INSERT INTO scheschbot.genus
(article)
VALUES
('der'),
('die'),
('das')


CREATE TABLE IF NOT EXISTS scheschbot.aggronymes
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    word CHAR(64) NOT NULL,
    type_id INT NOT NULL,
    genus_id INT,
    votes INT NOT NULL DEFAULT 0,
    FOREIGN KEY (type_id) REFERENCES scheschbot.word_types (id),
    FOREIGN KEY (genus_id) REFERENCES scheschbot.genus (id)
)
DEFAULT CHARACTER SET = 'utf16'

INSERT INTO scheschbot.aggronymes
(word, type_id, genus_id)
VALUES
('abartig', 1, NULL),
('assozial', 1, NULL),
('ägglhaft', 1, NULL),
('balancelos', 1, NULL),
('belanglos', 1, NULL),
('blöd', 1, NULL),
('charismatisch', 1, NULL),
('deppert', 1, NULL),
('dumm', 1, NULL),
('doof', 1, NULL),
('egglhaft', 1, NULL),
('ersetzbar', 1, NULL),
('frauenfeindlich', 1, NULL),
('hochnäsig', 1, NULL),
('idiotisch', 1, NULL),
('ignorant', 1, NULL),
('joggend', 1, NULL),
('kannibalistisch', 1, NULL),
('lieblos', 1, NULL),
('mickrig', 1, NULL),
('Monokel', 2, 3),
('nebulös', 1, NULL),
('oval', 1, NULL),
('Obazda', 2, 1),
('Orange', 2, 2),
('Omen', 2, 3),
('öde', 1, NULL),
('phasenverschoben', 1, NULL),
('qualifiziert', 1, NULL),
('respektlos', 1, NULL),
('Scheiß', 2, 1),
('Sauklaue', 2, 2),
('transatlantisch', 1, NULL),
('Taliban', 2, 1),
('unterirdisch', 1, NULL),
('überlebenswichtig', 1, NULL),
('verflucht', 1, NULL),
('weiß', 1, NULL),
('weis', 1, NULL),
('Yuppie verachtend', 1, NULL)