CREATE TABLE IF NOT EXISTS scheschbot.users
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    telegram_id INT NOT NULL,
    like_percentage INT NOT NULL DEFAULT 50,
    first_name CHAR(64) NOT NULL,
    last_name CHAR(64),
    username CHAR(64)
)
DEFAULT CHARACTER SET = 'utf16';

INSERT INTO scheschbot.users
(telegram_id, like_percentage, first_name)
VALUES
(123153, 30, 'Timo'),
(123547, 90, 'Nusch'),
(124895, 10, 'Frida'),
(123521, 80, 'Andi')