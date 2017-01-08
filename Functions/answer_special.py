import time
from Util import StringUtils


def get_answer(message, last_output):
    # Sonderzeichen abschneiden
    normalized_message = StringUtils.cut_specialchars(message)

    # auf 'moin' der Uhrzeit entsprechend antworten
    if normalized_message.startswith('moin ') or normalized_message == 'moin':
        return __get_greeting()
    # :3 und andere Zahlen runterzählen (außer :3 selbst)
    if len(message.split(':')) > 1:
        number_string = message.split(':')[-1]
        if __is_float(number_string):
            return __get_colonthree(number_string, last_output)

    # kein Ergebnis gefunden
    return ''


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


# :<x> wird zu :<x-1>
def __get_colonthree(number_string, last_output):
    # Sonderfall: :3 wird zu :3 (außer es wird von :4 runtergezählt)
    if number_string == '3' and last_output != ':4':
        return ':3'
    else:
        number_string_minus_one = __countdown(number_string)
        return ':' + number_string_minus_one


# zählt eine Zahl um 1 runter (egal ob Ganzzahl oder Gleitkommazahl)
def __countdown(number):
    # Komma durch Punkt ersetzen, damit der String als Zahl erkannt werden kann
    contains_comma = ',' in str(number)
    if contains_comma:
        number = str(number).replace(',', '.')

    if __is_int(number):  # Ganzzahl extra runterzählen, damit kein Punkt entsteht
        number = int(number) - 1
    else:
        # Anzahl der Nachkommastellen merken (für späteres Runden)
        number_of_digits = __get_number_of_digits(number)

        number = float(number) - 1

        # Nachkommastellen runden (bei Fehlern durch Floating Point Precision)
        format_string = '{0:.' + number_of_digits.__str__() + 'f}'
        number = format_string.format(number)

        # Punkt wieder durch Komma ersetzen, falls vorher ein Komma da war
        if contains_comma:
            number = str(number).replace('.', ',')

    return str(number)


# liefert die Anzahl an Nachkommastellen einer Zahl
def __get_number_of_digits(number):
    if '.' in str(number):
        return len(str(number).split('.')[1])
    return 0


# gibt an, ob ein String eine Ganzzahl ist
def __is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


# gibt an, ob ein String eine Kommazahl ist
def __is_float(string):
    # Komma durch Punkt ersetzen, damit eine Gleitkommaahl erkannt werden kann
    number = string.replace(',', '.')
    try:
        float(number)
        return True
    except ValueError:
        return False
