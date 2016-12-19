import telegram
import time
import constants
import db_connect


def main():
    # Beispiel-Query
    result = db_connect.query('SELECT * FROM users')
    for line in result:
        for value in line:
            print(value, end="\t")
        print()

    # Bot-Objekt erstellen
    bot = telegram.Bot(constants.scheschkey)

    # ID des letzten unverarbeiteten Updates holen
    try:
        last_update_id = bot.getUpdates()[-1].update_id
    except IndexError:  # falls keine Updates
        last_update_id = None
    print("last_update_id = ", last_update_id)

    while True:
        temp = last_update_id
        # alle Updates seit letztem Update holen
        for update in bot.getUpdates(offset=last_update_id):
            if update.inline_query and update.inline_query.query:
                bot.answer_inline_query(update.inline_query.id, answer_inline(update.inline_query))
            # Update-Objekt mit allen Attributen wie in der Bot-API beschrieben
            print("update = ", update)
            last_update_id = update.update_id + 1
        if temp is not last_update_id:
            print("last_update_id", last_update_id)
        time.sleep(3)


def answer_inline(inline_query):
    text = "Oh, hallo, Herr " + inline_query.query + "!"
    input_text = telegram.InputTextMessageContent(text)
    return [telegram.InlineQueryResultArticle('test_inline_query', "Mederer", input_text)]


if __name__ == '__main__':
    main()
