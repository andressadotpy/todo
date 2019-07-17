from todo.task import Task, TaskNotFound, NotValidStatus

class TaskContainer:

    def __init__(self):
        self.tasks = {}

    def new_task(self, task_name, note=None, due_date=None):
        task = Task(task_name, note, due_date)
        self.tasks.update({task.id:task})
        return task

    def _is_valid_id(self, id):
        if id in self.tasks.keys():
            return True
        return False

    def _get_task_by_id(self, id):
        return self.tasks.get(id)

    def edit_task(self, id, task_name):
        if not self._is_valid_id(id):
            raise TaskNotFound
        task = self._get_task_by_id(id)
        task.name = task_name
        return task

    def del_task(self, id):
        if not self._is_valid_id(id):
            raise TaskNotFound
        del self.tasks[id]

    def search_by_id(self, id):
        if not self._is_valid_id(id):
            raise TaskNotFound
        task = self._get_task_by_id(id)
        return task.name

    def search_by_word(self, word):
        matches = []
        for id, task in self.tasks.items():
            if word in task.name:
                matches.append(task.name)
        return matches

    def change_task_status(self, id, new_status):
        if not self._is_valid_id(id):
            raise TaskNotFound
        task = self._get_task_by_id(id)
        changed_status = task.change_status(new_status)
        return changed_status

    def edit_note(self, id, new_note):
        if not self._is_valid_id(id):
            raise TaskNotFound
        task = self._get_task_by_id(id)
        task.change_note(new_note)

    def get_task_note(self, id):
        if not self._is_valid_id(id):
            raise TaskNotFound
        task = self._get_task_by_id(id)
        return task.get_note()
