import telegram


def get_inline_results(query_string):
    text = "Oh, hallo, Herr " + query_string + "!"
    input_text = telegram.InputTextMessageContent(text)
    return [telegram.InlineQueryResultArticle('test_inline_query', "Mederer", input_text)]
