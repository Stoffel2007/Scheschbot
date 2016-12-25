import db_connect
import random

#db_connect.insert('aggronymes', ['word','type_id'], ['sadistisch','1'])
#db_connect.insert('aggronymes', ['word','type_id','genus_id'], ['Kräuterwastl','2','1'])

def aggro(command_text):
    def get_words(command_text):
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
                    adj_puffer = db_connect.__query(
                        "SELECT word "
                        "FROM aggronymes "
                        "WHERE type_id = 1 AND word LIKE '" + item_letters + "%'")
                    adj_puffer_copy = list(adj_puffer)
                    arr_adj_temp.append(adj_puffer_copy)
                    # Anzahl an Ajektive für 1 Buchstaben, benötig um dovon random ein Wort auszusuchen
                    for index_buff, item in enumerate(adj_puffer_copy):
                        pass
                    count_adj_pl.append(index_buff + 1)
                # letzter Buchstabe --> hole Nomen
                else:
                    # hole Nomen aus DB mit dazu gehörigem Artikel/Genus
                    noun_puffer = db_connect.__query("SELECT aggronymes.word, genus.article " +
                                                     "FROM aggronymes " +
                                                     "JOIN genus ON aggronymes.genus_id = genus.id " +
                                                     "WHERE word LIKE '" + item_letters + "%'")
                    # Anzahl Adjektive pro Wort
                    count_letters_adj.append(index)
                    # Kopiere Puffer, wenn nicht, geht er kaputt beim iterieren --> nicht weiter verwendbar
                    noun_puffer_copy = list(noun_puffer)
                    # Liste, mit der gearbeitet wird
                    arr_noun.append(noun_puffer_copy)
                    # Iteriere über Pufferkopie, zähle Anzahl an Nomen
                    for index_buff, item in enumerate(noun_puffer_copy):
                        pass

        arr_adj = [[] for i in range(len(arr_adj_temp))]

        # arr_adj in schönere Form formatieren
        for cnt_dim, dim in enumerate(arr_adj_temp):
            for cnt_block, block in enumerate(dim):
                arr_adj[cnt_dim].append(arr_adj_temp[cnt_dim][cnt_block][0])


        # prüft ob leere Elemente vorhanden sind
        # gibt permit, sowie error_message
        err_mess_adj = ""
        err_mess_noun = ""
        for dim in arr_adj:
            if not dim:
                err_mess_adj = 'für mindestens einen Buchstanben kein Adjektiv'
                permit = False
                break
        for dim in arr_noun:
            if not dim:
                err_mess_noun = 'für mindestens einen Buchstaben kein Nomen'
                permit = False
                break
        err_mess = err_mess_adj + ', ' + err_mess_noun
        return permit, arr_adj, arr_noun, err_mess

    # gibt Liste mit einzelnen Nomen nach Randomisierung
    def random_nouns(permit,arr_noun):
        one_noun = []
        if permit:
            for count, dim in enumerate(arr_noun):
                count_noun = len(arr_noun[count])
                rnd_noun = random.choice(dim)
                for row in one_noun:
                    count_while = 0
                    while rnd_noun in one_noun:
                        rnd_noun = random.choice(dim)
                        count_while += 1
                        if count_while == count_noun*3:
                            break
                one_noun.append(rnd_noun)
        return one_noun

    # gibt Liste mit einzelnen Adjektiven nach Randomisierung
    def random_adj(permit, arr_adj):
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

    def build_string(command_text,one_adj,one_noun):
        send_message = ''
        if one_adj and one_noun:
            prep_mes_gen = []
            send_message = ''
            cnt_adj_index = 0  # wievieltes Adjektiv im one_adj
            arr_words = command_text.split()
            for index, word in enumerate(arr_words):  # in arr_words ist String aus Kommando
                if one_noun[index][1] == 'der':
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
                    if i_cnt_lt < count_letters_adj-2:
                        prep_message = prep_message + prep_mes_gen[cnt_adj_index] + ', '
                    if i_cnt_lt == count_letters_adj-2:
                        prep_message = prep_message + prep_mes_gen[cnt_adj_index] + ' und '
                    if i_cnt_lt == count_letters_adj -1:
                        prep_message = prep_message + prep_mes_gen[cnt_adj_index] + ' '

                    cnt_adj_index = cnt_adj_index + 1  # wie vielstes Adj im one_adj
                # verbindet Adjektive mit Nomen

                prep_message = prep_message + one_noun[index][0]
                # verbindet mehrere Wörter
                if (len(arr_words) > 1) and (index < len(arr_words)-1):
                    prep_message = prep_message + ' SOWIE'
                send_message = send_message + prep_message + '\n'
        return send_message

    permit, arr_adj, arr_noun, error_message = get_words(command_text)

    one_noun = random_nouns(permit, arr_noun)

    one_adj = random_adj(permit, arr_adj)

    send_message = build_string(command_text, one_adj, one_noun)

    if not permit:
        send_message = error_message

    return send_message

# Kommando um Wörter hinzuzufügen
# für Adjektive /feedme {Adjektiv}
# für Nomen /feedme {Artikel} {Nomen}
# diese Funktion soll erst aufgerufen werden, wenn ein Admin das Futter bestätigt hat
# Der Bot sendet eine persönliche Nachricht an Admin, mit einem Button kann er das Futter bestätigen oder ablehnen
def fütter_mich(command_text):
    if len(command_text.split()) == 1:
        db_connect.insert('aggronymes', ['word', 'type_id'], [command_text, '1'])
    else:
        futter_nomen = command_text.split()
        if 'der' in futter_nomen:
            futter_nomen[0] = 1
        if 'die' in futter_nomen:
            futter_nomen[0] = 2
        if 'das' in futter_nomen:
            futter_nomen[0] = 3
        db_connect.insert('aggronymes', ['word', 'type_id', 'genus_id'], [futter_nomen[1], '2', futter_nomen[0]])
    return True
#####################################################################

command_text = 'Janosch'

send_message = aggro(command_text)

print(send_message)

fütter_mich('der Hans!')


if __name__ == '__main__':
    pass