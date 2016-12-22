import db_connect


# liefert die like_percentage eines Users
def get_mood(telegram_id):
    moods = db_connect.select('users', 'like_percentage', 'telegram_id = ' + telegram_id.__str__())

    result = moods.fetchone()

    if result:
        return result[0]  # fetchone() liefert ein Array (auch wenn nur ein Wert enthalten ist)
    else:  # Abfrage lieferte kein Ergebnis
        return -1


# like_percentage eines bestimmten Users ändern
# falls User nicht existiert, neuen Eintrag in Tabelle erzeugen
# andere User-Attribute (first_name, last_name, username) werden ebenfalls gesetzt
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

    user_result = db_connect.select('users', 'telegram_id', 'telegram_id = ' + user.id.__str__())

    # bei Fehlschlagen der Datenbankanfrage würde False zurückgeliefert werden
    if user_result:
        user_exists = user_result.fetchone()

        if user_exists:  # like_percentage (und andere User-Attribute) aktualisieren
            db_connect.update('users',
                              ['like_percentage', 'first_name', 'last_name', 'username'],
                              [like_percentage, user.first_name, last_name, username],
                              'telegram_id=' + user.id.__str__())

        else:  # neuen User hinzufügen
            db_connect.insert('users',
                              ['telegram_id', 'like_percentage', 'first_name', 'last_name', 'username'],
                              [user.id, like_percentage, user.first_name, last_name, username])
