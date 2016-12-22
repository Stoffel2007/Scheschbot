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
    # username und last_name können "None" sein
    # in diesem Fall NULL in die Datenbank eintragen
    if user.last_name:
        last_name = '"' + user.last_name + '"'
    else:
        last_name = "NULL"

    if user.username:
        username = '"' + user.username + '"'
    else:
        username = "NULL"

    user_result = db_connect.query('SELECT telegram_id FROM users WHERE telegram_id =' + user.id.__str__())

    # bei Fehlschlagen der Datenbankanfrage würde False zurückgeliefert werden
    if user_result:
        user_exists = user_result.fetchone()

        if user_exists:
            # Sende like_percentage
            db_connect.query('UPDATE users ' +
                             'SET like_percentage = ' + like_percentage.__str__() + ', ' +
                             'first_name = "' + user.first_name + '", ' +
                             'last_name = ' + last_name + ', ' +
                             'username = ' + username + ' '
                             'WHERE telegram_id = ' + user.id.__str__())

        else:
            # füge neuen User hinzu
            db_connect.query('INSERT INTO users ' +
                             '(telegram_id, like_percentage, first_name, last_name, username) ' +
                             'VALUES ' +
                             '(' + user.id.__str__() + ', ' +
                             like_percentage.__str__() + ', "' +
                             user.first_name.__str__() + '", ' +
                             last_name.__str__() + ', ' +
                             username.__str__() + ')')
