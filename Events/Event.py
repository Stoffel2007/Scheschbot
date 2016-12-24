from Events.Task import Task as Task


class Event:
    """Klasse für zeitgesteuerte Events"""
    def __init__(self, chat_id, message_id, tasks=None):
        """
        Constructor
        :param chat_id: ID des Chats, aus dem die Nachricht kam
        :param message_id: ID der Nachricht, auf die geantwortet wird
        :param tasks: Entweder [Task, Task, Task, ...] oder [[t in s, action], ...]
        """
        self.__task_counter = 0
        self.__task_list = []
        self.__chat_id = chat_id
        self.__message_id = message_id
        if type(tasks) == list:
            for task in tasks:
                try:
                    new_task = Task(task[0], task[1])
                    self.__task_list += [new_task]
                except TypeError:
                    self.__task_list += [task]
        else:
            print(Event.__init__.__doc__)

    def check_next_task(self):
        """
        Checks for next task
        :return: false if the current task is the last one
        """
        if self.__task_counter + 1 < len(self.__task_list):
            return True
        return False

    def get_next_task(self):
        """

        :return: Current Task or None
        """
        self.__task_counter += 1
        if self.__task_counter < len(self.__task_list):
            task = self.__task_list[self.__task_counter]
            return task
        return None

    def get_current_task(self):
        """
        This method returns the current task
        :return: Current Task or None
        """
        if self.__task_counter < len(self.__task_list):
            task = self.__task_list[self.__task_counter]
            return task
        return None

    def get_message_id(self):
        return self.__message_id

    def get_chat_id(self):
        return self.__chat_id


if __name__ == '__main__':
    def test_method():
        print("schesch")

    test = Event([[60, lambda: print("0")],
                  [59, lambda: print("asdfasdf")]])
    print(test.get_current_task().time)

    if test.get_next_task() is not None:
        pass
    print(test.get_current_task().time)
