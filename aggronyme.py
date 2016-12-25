import db_connect
import random


def aggro(command_text):
    if len(command_text) < 2:
        return 'Text muss mindestens 2 Buchstaben enthalten'

    permit, arr_adj, arr_noun, error_message = __get_words(command_text)

    one_noun = __random_nouns(permit, arr_noun)

    one_adj = __random_adj(permit, arr_adj)

    send_message = __build_string(command_text, one_adj, one_noun)

    if not permit:
        send_message = error_message

    return send_message


# Kommando um Wörter hinzuzufügen
# für Adjektive /feedme {Adjektiv}
# für Nomen /feedme {Artikel} {Nomen}
# diese Funktion soll erst aufgerufen werden, wenn ein Admin das Futter bestätigt hat
# Der Bot sendet eine persönliche Nachricht an Admin, mit einem Button kann er das Futter bestätigen oder ablehnen
def insert_words(params):
    genus_id = None
    if params.startswith('der '):
        genus_id = 1
    elif params.startswith('die '):
        genus_id = 2
    elif params.startswith('das '):
        genus_id = 3

    if genus_id:  # Nomen einfügen
        noun = params.split(' ', 1)[1]
        result = db_connect.select('aggronymes', where_expression="word = '" + noun + "'")
        if len(result) == 0:  # Wort noch nicht vorhanden
            result = db_connect.insert('aggronymes',
                                       ['word', 'type_id', 'genus_id'],
                                       [noun, 2, genus_id])
            return result
        return False
    else:  # Adjektiv einfügen
        result = db_connect.select('aggronymes', where_expression="word = '" + params + "'")
        if len(result) == 0:  # Wort noch nicht vorhanden
            result = db_connect.insert('aggronymes',
                                       ['word', 'type_id'],
                                       [params, 1])
            return result
        return False


def __get_words(command_text):
    arr_noun = []
    arr_adj_temp = []
    count_adj_pl = []
    count_letters_adj = []
    arr_words = command_text.split()
    permit = True
    for word in arr_words:  # iteriere über x-Wörter
        # list() macht Array von Buchstaben aus einem Wort
        arr_letters = list(word)
        # Größe des Arrays mit zukünftigen Adjektiven festlegen
        # Anzahl der Adjektive ist (Arraygröße - 1), da letzter Buchstabe ein Nomen ist
        # iteriere über x-Buchstaben
        for index, item_letters in enumerate(arr_letters):
            # solange nicht letzter Buchstabe werden Adjektive aus DB geholt
            if index < len(arr_letters) - 1:
                # x-dimensionales Array, zu jedem Buchstabe eine Dimension
                adj_puffer = db_connect.select("aggronymes",
                                               "word",
                                               "type_id = 1 AND word LIKE '" + item_letters + "%'")
                arr_adj_temp.append(adj_puffer)
                # Anzahl an Ajektive für 1 Buchstaben, benötig um davon random ein Wort auszusuchen
                count_adj_pl.append(len(adj_puffer))
            # letzter Buchstabe --> hole Nomen
            else:
                # hole Nomen aus DB mit dazu gehörigem Artikel/Genus
                noun_puffer = db_connect.__query("SELECT agg.word, genus.article " +
                                                 "FROM aggronymes AS agg " +
                                                 "JOIN genus ON agg.genus_id = genus.id " +
                                                 "WHERE word LIKE '" + item_letters + "%'")
                # Anzahl Adjektive pro Wort
                count_letters_adj.append(index)
                # Kopiere Puffer, wenn nicht, geht er kaputt beim iterieren --> nicht weiter verwendbar
                noun_puffer_copy = list(noun_puffer)
                # Liste, mit der gearbeitet wird
                arr_noun.append(noun_puffer_copy)

    arr_adj = []
    for i in range(len(arr_adj_temp)):
        arr_adj.append([])
    print("arr_adj =", arr_adj)

    # arr_adj in schönere Form formatieren
    for cnt_dim, dim in enumerate(arr_adj_temp):
        for cnt_block, block in enumerate(dim):
            arr_adj[cnt_dim].append(arr_adj_temp[cnt_dim][cnt_block][0])

    # prüft ob leere Elemente vorhanden sind
    # gibt permit, sowie error_message
    err_mess = []
    for dim in arr_adj:
        if not dim:
            err_mess.append('für mindestens einen Buchstaben kein Adjektiv in der Datenbank')
            permit = False
            break
    for dim in arr_noun:
        if not dim:
            err_mess.append('für mindestens einen Buchstaben kein Nomen in der Datenbank')
            permit = False
            break
    err_mess = ', '.join(err_mess)
    return permit, arr_adj, arr_noun, err_mess


# gibt Liste mit einzelnen Nomen nach Randomisierung
def __random_nouns(permit, arr_noun):
    one_noun = []
    if permit:
        for count, dim in enumerate(arr_noun):
            count_noun = len(arr_noun[count])
            rnd_noun = random.choice(dim)
            for i in range(len(one_noun)):
                count_while = 0
                while rnd_noun in one_noun:
                    rnd_noun = random.choice(dim)
                    count_while += 1
                    if count_while == count_noun * 3:
                        break
            one_noun.append(rnd_noun)
    return one_noun


# gibt Liste mit einzelnen Adjektiven nach Randomisierung
def __random_adj(permit, arr_adj):
    one_adj = []
    if permit:
        for i in range(len(arr_adj)):
            rnd_adj = random.choice(arr_adj[i])
            for dim in one_adj:
                count_adj_pl = len(dim)
                count_while = 0
                while rnd_adj in dim:
                    rnd_adj = random.choice(arr_adj[i])
                    count_while += 1
                    if count_while == count_adj_pl*3:
                        break
            one_adj.append(rnd_adj)
    return one_adj


def __build_string(command_text, one_adj, one_noun):
    send_message = ''
    if one_adj and one_noun:
        prep_mes_gen = []
        send_message = ''
        cnt_adj_index = 0  # wievieltes Adjektiv im one_adj
        arr_words = command_text.split()
        for index, word in enumerate(arr_words):  # in arr_words ist String aus Kommando
            add_genus = 'er'
            if one_noun[index][1] == 'die':
                add_genus = 'e'
            if one_noun[index][1] == 'das':
                add_genus = 'es'
            prep_message = ''
            count_letters_adj = len(word)-1  # Anzahl der Adjektive pro Wort
            for i_cnt_lt in range(count_letters_adj):
                # fügt zu jedem Adjektiv den richtigen Genus hinzu
                prep_mes_gen.append(one_adj[cnt_adj_index] + add_genus)

                # verbindet Adjektive
                if i_cnt_lt < count_letters_adj - 2:
                    prep_message = prep_message + prep_mes_gen[cnt_adj_index] + ', '
                if i_cnt_lt == count_letters_adj - 2:
                    prep_message = prep_message + prep_mes_gen[cnt_adj_index] + ' und '
                if i_cnt_lt == count_letters_adj - 1:
                    prep_message = prep_message + prep_mes_gen[cnt_adj_index] + ' '

                cnt_adj_index += 1  # wie vieltes Adj im one_adj
            # verbindet Adjektive mit Nomen

            prep_message = prep_message + one_noun[index][0]
            # verbindet mehrere Wörter
            if (len(arr_words) > 1) and (index < len(arr_words)-1):
                prep_message += ' SOWIE'
            send_message = send_message + prep_message + '\n'
    return send_message
