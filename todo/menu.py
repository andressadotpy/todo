import sys

from todo.task import Task, TaskNotFound, NotValidStatus
from todo.task_container import TaskContainer

class Menu:
    """Menu options for a command line todo list.
    Initialized with a TaskContainer object, that keeps track
    of Tasks created/deleted.
    """

    def __init__(self):
        self.task_container = TaskContainer()
        self.choices = {1: self.add_new_task,
                        2: self.change_task,
                        3: self.delete_task,
                        4: self.search_task,
                        5: self.search_task_by_word,
                        6: self.edit_task_status,
                        7: self.edit_task_note,
                        8: self.show_finished_tasks,
                        9: self.show_unfinished_tasks_with_due_date,
                        10: self.show_all_tasks,
                        11: self.show_task_note,
                        12: self.quit}

    def display_menu(self):
        print(
        """
        1: Add new task
        2: Edit a task
        3: Delete a task
        4: Search a task by id
        5: Search a task by a matching word
        6: Edit a task status
        7: Edit a task note
        8: Show all finished tasks
        9: Show all unfinished tasks with due date
        10: Show all tasks
        11: Show note to a task
        12: Quit
        """)

    def run(self):
        """Display the options available and asks the user to choose one.
        Then, the action of choice is executed.
        Repeats displaying menu options untill the user Quit.
        """
        while True:
            self.display_menu()
            choice = int(input("CHOOSE AN OPTION: "))
            action = self.choices.get(choice)
            if action:
                action()
            else:
                (f'{choice} is not a valid choice. Try again')


    def _get_task(self, id):
        task = self.task_container.tasks.get(id)
        return task

    def add_new_task(self):
        """Creates a new Task object. A Task object must have a name and can
        have a Note and a due date attribute.
        Calls for new_task() inside TaskContainer to build the new task.
        """
        task_name = input("Task name: ")
        note = input("Add a note: ")
        due_date = input("Due date: ")
        task = self.task_container.new_task(task_name, note, due_date)
        return task

    def change_task(self):
        """Asks for the id ttribute of a Task object and edit the name
        of this object calling for edit_task() method at TaskContainer.
        """
        id = int(input("Task ID: "))
        new_task_name = input("Edited task: ")
        changed_task = self.task_container.edit_task(id, new_task_name)
        return changed_task

    def delete_task(self):
        """Asks for the id attribute of a Task object and delete this object,
        calling for del_task() inside TaskContainer."""
        id = int(input("Task ID: "))
        self.task_container.del_task(id)

    def search_task(self):
        """Asks for the id attribute of the Task object and calls
        search_by_id() method inside TaskContainer to searches for the task.
        Prints the task name and returns it.
        """
        id = int(input("Task ID: "))
        task_name = self.task_container.search_by_id(id)
        print(task_name)
        return task_name

    def search_task_by_word(self):
        """Asks for a word the user wants to match and calls for
        search_by_word() method inside TaskContainer.
        Prints the names of the tasks that match the word and returns a list
        of matching tasks.
        """
        word = input("Type word to be matched: ")
        matches = self.task_container.search_by_word(word)
        for match in matches:
            print(match)
        return matches

    def edit_task_status(self):
        """Asks for the id attribute of the Task object the
        user wants to change status and prints the possible status for a task.
        The user enters the new status and the method calls for
        change_task_status() method inside TaskContainer.
        """
        id = int(input("Task ID: "))
        print("""AVAILABLE STATUS:
        Unfinished
        In process
        Finished
        """)
        new_status = input("Type new status: ")
        changed_status = self.task_container.change_task_status(id, new_status)

    def edit_task_note(self):
        """Asks for the id attribute of the Task object the user wants
        to edit the Note and the new message to change the Note.
        Calls for edit_note() method inside TaskContainer."""
        id = int(input("Task ID: "))
        new_note = input("New note: ")
        self.task_container.edit_note(id, new_note)

    def show_finished_tasks(self):
        """Search all Task objects with the status attribute 'finished' and
        stores the task name of all this objects in a list.
        Prints tasks names of the list of finished tasks and returns it.
        """
        finished = []
        for id, task in self.task_container.tasks.items():
            if task.status == 'finished':
                finished.append(task.name)
        for task_name in finished:
            print(task_name)
        return finished

    def show_unfinished_tasks_with_due_date(self):
        """Search all Task objects with the status attribute 'unfinished' and
        stores the task name inside a list and the due date for each of
        this unfinished tasks in another list.
        Prints the task name and the due date and returns the list of
        names of unfinished tasks. """
        unfinished = []
        due_dates = []
        for id, task in self.task_container.tasks.items():
            if task.status == 'unfinished':
                unfinished.append(task.name)
                due_dates.append(task.due_date)
        for task, due_date in zip(unfinished, due_dates):
            print(task, '-', due_date)
        return unfinished

    def show_all_tasks(self):
        """Prints the id and name attributes of a Task object."""
        for id, task in self.task_container.tasks.items():
            print(task.id, '-', task.name)

    def show_task_note(self):
        """Asks for the id attribute of a Task object the user wants to
        see the note and calls for get_note() method inside Task.
        Returns the note."""
        id = int(input("Task ID: "))
        task = self._get_task(id)
        print(task.get_note())
        return task.get_note()

    def quit(self):
        sys.exit(0)
