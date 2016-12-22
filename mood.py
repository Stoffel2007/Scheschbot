import db_connect


# Liefert die Like_Percentage von einer Telegram ID
def get_mood(telegram_id):
    # Query über db_connect abschicken und ResultSet empfangen
    moods = db_connect.query('SELECT like_percentage FROM users WHERE telegram_id =' + telegram_id.__str__())

    result = moods.fetchone()

    if result:
        return result[0]  # fetchone()[0] muss man machen sonst kommt was komisches raus
    else:
        return -1


def set_mood(user, like_percentage):
    user_result = db_connect.query('SELECT telegram_id FROM users WHERE telegram_id =' + user.id.__str__())

    user_exists = user_result.fetchone()

    if user_exists:
        # Sende like_percentage
        db_connect.query('UPDATE users ' +
                         'SET like_percentage=' + like_percentage.__str__() +
                         ' WHERE telegram_id =' + user.id.__str__())

    else:
        # füge neuen User hinzu
        db_connect.query('INSERT INTO users ' +
                         '(telegram_id, like_percentage, first_name) ' +
                         'VALUES ' +
                         '(' + user.id.__str__() + ',' +
                         like_percentage.__str__() + ',"' +
                         user.first_name.__str__() + '")')
