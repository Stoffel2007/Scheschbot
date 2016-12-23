from Async.Event import Event
import threading
import time


class AsyncHandler:
    def __init__(self):
        """
        Constroctor
        """
        # self.__events = []
        self.__update = []

    def getupdate(self):
        """
        :return: returns the Handleroutput, delets the update
        """
        re = self.__update
        self.__update = []
        return re

    def updateavailable(self):
        if len(self.__update) > 0:
            return True
        return False

    def addevent(self, event):
        t = threading.Timer(event.getcurrenttask().time, lambda x=event: self.__timout(x))
        t.start()
        # self.__events.append(event)

    def __timout(self, event):
        self.__update += [[event.getmsgid(), event.getcurrenttask().content]]
        if event.checknexttask():
            t = threading.Timer(event.getnexttask().time, lambda x=event: self.__timout(x))
            t.start()

    # def getnextevent(self): # obsolet
    #     if len(self.__events) < 1:
    #         return None
    #     nextevent = self.__events[0]
    #     for event in self.__events:
    #         if event.getcurrenttask().time < nextevent.getcurrenttask().time:
    #             nextevent = event
    #     return nextevent
    #


if __name__ == '__main__':
    event1 = Event(1, [[10, "MsG"],
                       [10, 2]])
    test = Event(2, [[60, lambda: print("0")],
                     [59, lambda: print("asdfasdf")]])
    handler = AsyncHandler()
    handler.addevent(event1)

    while 1:
        print(handler.getupdate())
        time.sleep(1)



    # handler.addevent(test)
    # test = handler.getnextevent().showcurrenttask().content()
    #
    # eieruhr = threading.Timer(7, lambda: print("Fieff"))
    # eieruhr.start()
    # while 1:
    #     print("fief")
    #     time.sleep(5)
