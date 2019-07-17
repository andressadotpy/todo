from datetime import datetime

from todo.note import Note

class Task:
    id = 1

    def __init__(self, name, note=None, due_date=None):
        self.name = name
        self.creation_date = datetime.today()
        self.status = 'unfinished'
        self.message = Note(note) if note is not None else None
        self.due_date = due_date if due_date is not None else None
        self.id = Task.id
        Task.id += 1

    def get_task_name(self):
        return f'{self.name}'

    def get_note(self):
        return f'{self.message}'

    def change_note(self, new_message):
        self.message = Note(new_message)
        return f'{self.message.note}'

    def change_status(self, new_status):
        valid_status = ['unfinished',
                        'in process',
                        'finished']
        if new_status.lower() not in valid_status:
            raise NotValidStatus
        self.status = new_status
        return self.status

    def match(self, word):
        if word in self.name:
            return True
        return False


class NotValidStatus(Exception):
    pass

class TaskNotFound(Exception):
    pass
