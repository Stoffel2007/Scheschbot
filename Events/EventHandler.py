from Events.Event import Event
import threading


class EventHandler:
    def __init__(self):
        """
        Constroctor
        """
        self.__update = []

    def get_update(self):
        """
        :return: returns the Handleroutput, delets the update
        """
        re = self.__update
        self.__update = []
        return re

    def update_available(self):
        """
        Checks if a update is available
        :return:
        """
        if len(self.__update) > 0:
            return True
        return False

    def add_event(self, event):
        """
        Adds event to an timer
        :param event:
        :return:
        """
        t = threading.Timer(event.get_current_task().time, lambda x=event: self.__timout(x))
        t.start()

    def __timout(self, event):
        """
        method that pushes the event output into __updates and restarts the timer if needed
        :param event:
        :return:
        """
        self.__update += [[event.get_message(), event.get_current_task().content]]
        if event.check_next_task():
            t = threading.Timer(event.get_next_task().time, lambda x=event: self.__timout(x))
            t.start()


if __name__ == '__main__':
    event1 = Event(1, [[10, "MsG"],
                       [10, 2]])
    test = Event(2, [[60, lambda: print("0")],
                     [59, lambda: print("asdfasdf")]])
    handler = EventHandler()
    handler.add_event(event1)
