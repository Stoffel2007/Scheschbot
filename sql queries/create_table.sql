CREATE TABLE IF NOT EXISTS users
(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    telegram_id INT NOT NULL,
    first_name CHAR(64) NOT NULL,
    last_name CHAR(64),
    username CHAR(64)
)
DEFAULT CHARACTER SET = 'utf16';