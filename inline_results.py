import telegram


def get_inline_results(query_string):
    text_mederer = "Oh, hallo, Herr " + query_string + "!"
    text_blyatkek = "Blyat, du dämlicher " + query_string + "!"

    input_text_mederer = telegram.InputTextMessageContent(text_mederer)
    input_text_blyatkek = telegram.InputTextMessageContent(text_blyatkek)

    return [telegram.InlineQueryResultArticle('inline_query_mederer', "Mederer", input_text_mederer),
            telegram.InlineQueryResultArticle('inline_query_blyatkek', "Blyat-Kek", input_text_blyatkek)]
