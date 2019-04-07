import db_connect


# liefert die sympathy_percentage eines Users
def get_mood(telegram_id):
    result = db_connect.select('users', 'sympathy_percentage', 'telegram_id = ' + telegram_id.__str__())

    # bei Fehlschlagen der Datenbankanfrage würde False zurückgeliefert werden
    if result is not False:
        # zurückgeliefertes Array enthält einen Wert
        if len(result) > 0:
            return result[0][0]  # select() liefert ein 2D-Array (auch wenn nur ein Wert enthalten ist)
        else:  # Abfrage lieferte kein Ergebnis
            return -1
    else:
        return False


# sympathy_percentage eines bestimmten Users ändern
# falls User nicht existiert, neuen Eintrag in Tabelle erzeugen
# andere User-Attribute (first_name, last_name, username) werden ebenfalls gesetzt
def set_mood(user, sympathy_percentage):
    if sympathy_percentage > 100:
        sympathy_percentage = 100
    elif sympathy_percentage < 0:
        sympathy_percentage = 0

    user_result = db_connect.select('users', where_expression='telegram_id = ' + user.id.__str__())

    # bei Fehlschlagen der Datenbankanfrage würde False zurückgeliefert werden
    if user_result is not False:
        # zurückgeliefertes Array enthält einen Wert
        if len(user_result) > 0:  # sympathy_percentage (und andere User-Attribute) aktualisieren
            db_connect.update('users',
                              ['sympathy_percentage', 'first_name', 'last_name', 'username'],
                              [sympathy_percentage, user.first_name, user.last_name, user.username],
                              'telegram_id=' + user.id.__str__())
        # zurückgeliefertes Array enthält keinen Wert
        else:  # neuen User hinzufügen
            db_connect.insert('users',
                              ['telegram_id', 'sympathy_percentage', 'first_name', 'last_name', 'username'],
                              [user.id, sympathy_percentage, user.first_name, user.last_name, user.username])
