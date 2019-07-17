import unittest

from ..task import Task, NotValidStatus
from ..task_container import TaskContainer, TaskNotFound

class TestTaskContainer(unittest.TestCase):

    def setUp(self):
        self.task_container = TaskContainer()

    def test_task_container_has_dict_of_tasks_instances(self):
        self.assertIsInstance(self.task_container.tasks, dict)

    def test_add_new_task_only_with_name(self):
        task = self.task_container.new_task("Create new task")
        self.assertEqual({task.id : task.get_task_name()},
                        {1 : "Create new task"})

    def test_add_new_task_with_name_and_note(self):
        task = self.task_container.new_task("Create new task", "This is a note")
        self.assertEqual(task.get_note(), "This is a note")

    def test_add_new_task_with_name_note_and_due_date(self):
        task = self.task_container.new_task("Create new task", "This is a note",
                                            "2019, 7, 12")
        self.assertEqual((task.get_note(), "2019, 7, 12"),
                        ("This is a note", "2019, 7, 12"))

    def test_if_id_is_increasing_when_2_tasks_are_added(self):
        task_1 = self.task_container.new_task("First task")
        task_2 = self.task_container.new_task("Second task")
        self.assertTrue(self.task_container.tasks,
                        {task_1.id:task_1, task_2.id:task_2})

    def test_edit_a_task(self):
        task = self.task_container.new_task("Create new task", "This is a note")
        changed_task = self.task_container.edit_task(1, "Edit task")
        self.assertEqual(self.task_container.tasks,
                        {changed_task.id:changed_task})

    def test_delete_a_task(self):
        task = self.task_container.new_task("Create new task")
        self.task_container.del_task(task.id)
        self.assertEqual(self.task_container.tasks, {})

    def test_raises_TaskNotFound_trying_to_edit_task_that_dont_exists(self):
        with self.assertRaises(TaskNotFound):
            self.task_container.edit_task(2, "Fail editing")

    def test_raises_TaskNotFound_trying_delete_task_that_dont_exists(self):
        with self.assertRaises(TaskNotFound):
            self.task_container.del_task(2)

    def test_search_task_by_id(self):
        task = self.task_container.new_task("Task")
        self.assertEqual(self.task_container.search_by_id(1), "Task")

    def test_raises_TasNotFound_trying_to_search_by_task_that_dont_exists(self):
        with self.assertRaises(TaskNotFound):
            self.task_container.search_by_id(2)

    def test_search_matching_word_dont_find_results(self):
        match = self.task_container.search_by_word("new")
        self.assertEqual(match, [])

    def test_search_matching_word_finds_one_result(self):
        task = self.task_container.new_task("Create new task")
        match = self.task_container.search_by_word("new")
        self.assertEqual(match, ["Create new task"])

    def test_search_matching_word_finds_more_than_one_result(self):
        task = self.task_container.new_task("Create new task")
        task_2 = self.task_container.new_task("Very new task")
        task_3 = self.task_container.new_task("Not catch this task")
        match = self.task_container.search_by_word("new")
        self.assertEqual(match, ["Create new task", "Very new task"])

    def test_task_initial_status_is_unfinished(self):
        task = self.task_container.new_task("New task")
        self.assertEqual(task.status, "unfinished")

    def test_change_task_status(self):
        task = self.task_container.new_task("New task")
        self.task_container.change_task_status(1, "finished")
        self.assertEqual(task.status, "finished")

    def test_change_task_status_raise_NotValidStatus(self):
        task = self.task_container.new_task("New task")
        with self.assertRaises(NotValidStatus):
            task.change_status('lalala')

    def test_edit_task_note(self):
        task = self.task_container.new_task("New task")
        self.task_container.edit_note(1, "This is a note.")
        self.assertEqual(task.message.note, "This is a note.")      

    def tearDown(self):
        self.task_container.tasks.clear()
        Task.id = 1
