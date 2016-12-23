from Async.Task import Task as Task


class Event:
    """Klasse für zeitgesteuerte Events"""
    def __init__(self, msgid, tasks=None):
        """
        Constructor
        :param msgid:
        :param tasks: Entweder [Task, Task, Task, ...] oder [[t in s, action], ...]
        """
        self.__taskcounter = 0
        self.__tasklist = []
        self.__msgid = msgid
        if type(tasks) == list:
            for task in tasks:
                try:
                    newtask = Task(task[0], task[1])
                    self.__tasklist += [newtask]
                except TypeError:
                    self.__tasklist += [task]
        else:
            print(Event.__init__.__doc__, 1)

    def checknexttask(self):
        """
        Checks for next task
        :return: false if the current task is the last one
        """
        if self.__taskcounter + 1 < len(self.__tasklist):
            return True
        return False

    def getnexttask(self):
        """

        :return: Current Task or None
        """
        self.__taskcounter += 1
        if self.__taskcounter < len(self.__tasklist):
            task = self.__tasklist[self.__taskcounter]
            return task
        return None

    def getcurrenttask(self):
        """
        This method returns the current task
        :return: Current Task or None
        """
        if self.__taskcounter < len(self.__tasklist):
            task = self.__tasklist[self.__taskcounter]
            return task
        return None

    def getmsgid(self):
        return self.__msgid


if __name__ == '__main__':
    def testmethod():
        print("schesch")

    test = Event([[60, lambda: print("0")],
                  [59, lambda: print("asdfasdf")]])
    print(test.getcurrenttask().time)

    if test.getnexttask() is not None:
        pass
    print(test.getcurrenttask().time)
