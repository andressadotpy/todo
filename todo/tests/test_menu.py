import unittest
from unittest.mock import patch

from ..menu import Menu
from ..task_container import TaskContainer
from ..task import Task, TaskNotFound, NotValidStatus

class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.task = self.menu.task_container.new_task("A task")

    def test_Menu_initialized_with_TaskContainer_object(self):
        self.assertIsInstance(self.menu.task_container, TaskContainer)

    def test_Menu_initialized_with_dict_of_choices(self):
        self.assertIsInstance(self.menu.choices, dict)

    @patch('builtins.input', side_effect=["New task", "This is a note", "2019"])
    def test_Menu_option_add_new_task(self, mock_inputs):
        task = self.menu.add_new_task()
        self.assertEqual(self.menu.task_container.tasks,
                         {1: self.task, 2: task})

    @patch('builtins.input', side_effect=["New task", "This is a note", "2019"])
    def test_is_working_my_patch_function(self, mock_inputs):
        task = self.menu.add_new_task()
        note = self.menu.task_container.get_task_note(task.id)
        self.assertEqual(note, task.message.note)

    @patch('builtins.input', side_effect=[1, 'Editing task'])
    def test_change_task(self, mock_inputs):
        changed_task = self.menu.change_task()
        self.assertEqual(changed_task.id, 1)

    @patch('builtins.input', return_value=1)
    def test_delete_task(self, mock_id):
        self.menu.delete_task()
        self.assertEqual(self.menu.task_container.tasks, {})

    @patch('builtins.input', return_value=2)
    def test_delete_task_raise_TaskNotFound_if_id_not_found(self, mock_id):
        with self.assertRaises(TaskNotFound):
            self.menu.delete_task()

    @patch('builtins.input', return_value=1)
    def test_search_task_by_id(self, mock_id):
        task_name = self.menu.search_task()
        self.assertTrue(task_name, self.task.name)

    @patch('builtins.input', return_value=2)
    def test_search_task_by_id_raises_TaskNotFound_if_wrong_id(self, mock_id):
        with self.assertRaises(TaskNotFound):
            self.menu.search_task()

    @patch('builtins.input', return_value='task')
    def test_search_task_by_word(self, mock_word):
        self.assertEqual(self.menu.search_task_by_word(), ["A task"])

    @patch('builtins.input', side_effect=[1, 'finished'])
    def test_edit_task_status(self, mock_inputs):
        self.menu.edit_task_status()
        self.assertTrue(self.task.status =='finished')

    @patch('builtins.input', side_effect=[2, 'finished'])
    def test_edit_task_status_raise_TaskNotFound_if_wrong_id(self, mock_inputs):
        with self.assertRaises(TaskNotFound):
            self.menu.edit_task_status()

    @patch('builtins.input', side_effect=[1, "changing this note"])
    def test_edit_task_note(self, mock_inputs):
        self.menu.edit_task_note()
        self.assertTrue(self.task.get_note() == "changing this note")

    @patch('builtins.input', side_effect=[2, "changing this note"])
    def test_edit_task_note_raises_TaskNotFound_if_wrong_id(self, mock_inputs):
        with self.assertRaises(TaskNotFound):
            self.menu.edit_task_note()

    def test_show_finished_tasks(self):
        task_2 = self.menu.task_container.new_task("Adding one more task")
        self.task.change_status('finished')
        self.assertEqual(self.menu.show_finished_tasks(), [self.task.name])


    def test_show_finished_tasks_return_empty_list_if_no_finished_task(self):
        self.assertEqual(self.menu.show_finished_tasks(), [])

    def test_show_unfinished_tasks(self):
        task_2 = self.menu.task_container.new_task("Adding one more task",
                                                "This is a note",
                                                "2019, 1, 7")
        self.assertEqual(self.menu.show_unfinished_tasks_with_due_date(),
                        [self.task.name, task_2.name])

    @patch('builtins.input', return_value=2)
    def test_show_task_note(self, mock_id):
        task_2 = self.menu.task_container.new_task("Adding one more task",
                                                "This is a note",
                                                "2019, 1, 7")
        note = self.menu.show_task_note()
        self.assertTrue(task_2.get_note() == note == "This is a note")

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.menu.quit()

    def tearDown(self):
        self.menu.task_container.tasks.clear()
        Task.id = 1
