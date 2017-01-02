import re


# entfernt Sonderzeichen aus einem String
def cut_specialchars(string):
    textarray = []
    for char in string:
        if is_letter(char):
            textarray += char
    output = ''
    for i in textarray:
        output += i
    return output


# überprüft, ob ein Zeichen ein Buchstabe ist
def is_letter(string):
    allowed_letters = re.compile('[ 0-9A-zА-ѿΑ-ω+ÖöÄäÜüß]')
    if allowed_letters.match(string) is not None:
        return True
    return False


# schneidet Leerzeichen am Anfang und Ende eines String ab
# kürzt doppelte Leerzeichen
def cut_spaces(string):
    while string.startswith(' '):  # Leerzeichen am Anfang abschneiden
        string = string[1:]
    while '  ' in string:  # doppelte Leerzeichen kürzen
        string = string.replace('  ', ' ')
    while string.endswith(' '):  # Leerzeichen am Ende abschneiden
        string = string[:-1]
    return string
