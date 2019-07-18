from todo.task import Task, TaskNotFound, NotValidStatus

class TaskContainer:

    def __init__(self):
        """Initializes a dictionary to store Task objects
        The dictionary keys are the id attribute of a Task object and
        the values are the Task objects.
        """
        self.tasks = {}

    def new_task(self, task_name, note=None, due_date=None):
        """Creates a new Task object with name, note and due date.
        If note and due date aren't specified, by default are None.
        Updates the dictionary of Task objects and returns
        the created task."""
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
        """Receive as arguments an id and a task name and
        changes the name attribute of the Task object with the given id.
        Return the task with the name edited."""
        if not self._is_valid_id(id):
            raise TaskNotFound
        task = self._get_task_by_id(id)
        task.name = task_name
        return task

    def del_task(self, id):
        """Receive as argument an id attribute of the Task object.
        Searches for the task inside the dictionary of tasks.
        If the id is in the dictionary, removes the Task object from it.
        Raises TaskNotFound otherwise.
        """
        if not self._is_valid_id(id):
            raise TaskNotFound
        del self.tasks[id]

    def search_by_id(self, id):
        """Receive as argument an id attribute of the Task object.
        Searches for the task inside the dictionary of tasks.
        If the id is in the dictionary, returns the name attribute of
        the Task object. Raises TaskNotFound otherwise.
        """
        if not self._is_valid_id(id):
            raise TaskNotFound
        task = self._get_task_by_id(id)
        return task.name

    def search_by_word(self, word):
        """Receive as argument a word.
        Searches for task names that matches this word.
        Stores all matching task names inside a list.
        Returns the list of matching words.
        """
        matches = []
        for id, task in self.tasks.items():
            if word in task.name:
                matches.append(task.name)
        return matches

    def change_task_status(self, id, new_status):
        """Receive as argument an id attribute of the Task object and a
        new status to change the status attribute of the Task object.
        Searches for the task inside the dictionary of tasks.
        If the id is in the dictionary, calls change_status() method
        inside Task and returns the changed status.
        Raises TaskNotFound otherwise.
        """
        if not self._is_valid_id(id):
            raise TaskNotFound
        task = self._get_task_by_id(id)
        changed_status = task.change_status(new_status)
        return changed_status

    def edit_note(self, id, new_note):
        """Receive as argument an id attribute of the Task object and
        a string note to change the task not.
        Searches for the task inside the dictionary of tasks.
        If the id is in the dictionary, change the Note associated with the
        Task object.
        Raises TaskNotFound otherwise.
        """
        if not self._is_valid_id(id):
            raise TaskNotFound
        task = self._get_task_by_id(id)
        task.change_note(new_note)

    def get_task_note(self, id):
        """Receive as argument an id attribute of the Task object.
        Searches for the task inside the dictionary of tasks.
        If the id is in the dictionary, returns the Note associated with
        the Task object. Raises TaskNotFound otherwise.
        """
        if not self._is_valid_id(id):
            raise TaskNotFound
        task = self._get_task_by_id(id)
        return task.get_note()
