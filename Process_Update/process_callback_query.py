from Functions import aggronyme


def get_message_list(callback_query):
    params_dict = {'chat_id': callback_query.message.chat.id,
                   'message_id': callback_query.message.message_id}

    data_array = callback_query.data.split(' ', 1)
    params = data_array[1]
    if data_array[0] == 'yes':
        if aggronyme.insert_words(params) is True:
            params_dict['text'] = 'legg0 :3\n' \
                                  '"' + params + '" erfolgreich zur Datenbank hinzugefügt'
        else:
            # Artikel rausnehmen, falls vorhanden
            if params.startswith('der ') or params.startswith('die ') or params.startswith('die '):
                word = params.split(' ', 1)[1]
            else:
                word = params

            vote_incremented = aggronyme.increment_vote(word)
            if not vote_incremented:
                print('\tkonnte Votes von ' + word + ' nicht inkrementieren')
            params_dict['text'] = '"' + params + '"  konnte nicht zur Datenbank hinzugefügt werden\n' + \
                                  'Eventuell ist dieses Wort bereits vorhanden'
    elif data_array[0] == 'no':
        params_dict['text'] = '"' + params + '" abgelehnt'

    return [{'action': 'edit_message', 'params_dict': params_dict}]
