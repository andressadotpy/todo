from datetime import datetime

from todo.note import Note

class Task:
    """Represents one task."""
    id = 1

    def __init__(self, name, note=None, due_date=None):
        """Initializes each Task with a task name,
        a date time of when the Task was created,
        a status attribute primarly setted to 'unfinished',
        a Note object (if the user wants to add a message to the task),
        a due date (if the user wants to set a due date to the task),
        and a unique id.
        """
        self.name = name
        self.creation_date = datetime.today()
        self.status = 'unfinished'
        self.message = Note(note) if note is not None else None
        self.due_date = due_date if due_date is not None else None
        self.id = Task.id
        Task.id += 1

    def get_task_name(self):
        """Returns the string name of a Task."""
        return f'{self.name}'

    def get_note(self):
        """Returns the string representation of the message attribute."""
        return f'{self.message}'

    def change_note(self, new_message):
        """Creates another Note object and changes the Note object
        associated with the message attribute of the Task.
        Returns the string representation of the note.
        """
        self.message = Note(new_message)
        return f'{self.message.note}'

    def change_status(self, new_status):
        """Receives a new status argument and checks if the status
        is valid. If it's valid, change the status attribute ot the Task
        to the new status.
        Raises NotValidStatus otherwise.
        """
        valid_status = ['unfinished',
                        'in process',
                        'finished']
        if new_status.lower() not in valid_status:
            raise NotValidStatus
        self.status = new_status
        return self.status

    def match(self, word):
        """Checks if a word matches the name attribute of the Task.
        Returns True if matches and False otherwise.
        """
        if word in self.name:
            return True
        return False


class NotValidStatus(Exception):
    pass

class TaskNotFound(Exception):
    pass
