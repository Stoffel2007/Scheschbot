from Events.Event import Event


def cook(message, food, event_handler):
    if food != '':
        name = message.from_user.first_name
        food = food.title()  # auf Großschreibung achten
        events = Event(message, [[5, 'koche Wass0 für ' + name + '....'],
                                 [5, 'koche ' + food + ' für ' + name + '....'],
                                 [5, food + ' für ' + name + ' sind fertig! :3']])
        event_handler.add_event(events)

        return 'Ok, wird gemacht....'
    # falls kein Gericht angegeben wurde
    return 'Was soll ich denn bitte kochen?! Das musst du schon dazusagen, du Trottel!'
