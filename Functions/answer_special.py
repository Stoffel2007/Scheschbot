import time

from Util import StringUtils


def get_answer(message):
    answer = ''

    # Sonderzeichen abschneiden
    normalized_message = StringUtils.cut_specialchars(message)

    if normalized_message.startswith('moin ') or normalized_message == 'moin':
        answer = __get_greeting()

    return answer


# liefert je nach Uhrzeit eine andere Antwort zurück
def __get_greeting():
    greetings_array = [['Nix "moin"! Es ist mitten in der Nacht, du Vollidiot!', 5],
                       ['Was treibt dich denn bitte um zu dieser unchritlichen Stunde?!', 8],
                       ['Moin, du Önn0 :3', 12],
                       ['Was für "moin"?! Es ist hellichter Tag, du Langschläfer!', 16],
                       ['Was hast du denn für einen Schlafrhythmus, dass du erst jetzt aufstehst?!', 20],
                       ['Geh mal lieber önnen, es ist spätabends, du Depp!', 24]]
    hour = time.gmtime().tm_hour
    for greeting in greetings_array:
        if hour < greeting[1]:
            return greeting[0]
