import unittest
from unittest.mock import patch
from datetime import datetime

from ..task import Task, NotValidStatus, TaskNotFound
from ..note import Note

class TestTask(unittest.TestCase):

    def setUp(self):
        self.task = Task("Create new task")

    def test_if_a_task_has_a_name(self):
        self.assertEqual(self.task.name, "Create new task")

    def test_if_a_task_note_is_None_if_not_given(self):
        self.assertIsNone(self.task.message)

    def test_if_a_task_note_is_given_is_an_instance_of_Note(self):
        task = Task("Create new task", "Very important task")
        self.assertIsInstance(task.message, Note)

    def test_get_note(self):
        task = Task("Create new task", "Very important task")
        self.assertEqual(task.get_note(), "Very important task")

    def test_change_note(self):
        self.assertEqual(self.task.change_note("Changing message"),
        "Changing message")

    def test_has_creation_date(self):
        self.assertIsInstance(self.task.creation_date, datetime)

    def test_if_task_due_date_is_None_if_not_given(self):
        task = Task("Create new task", "Very important task", "2019, 7, 12")
        self.assertEqual(task.due_date, "2019, 7, 12")

    def test_task_id(self):
        self.assertEqual(self.task.id, 1)

    def test_task_id_is_increasing(self):
        task_2 = Task("Creating another task")
        self.assertEqual(task_2.id, 2)

    def test_initial_task_status_is_unfinished(self):
        self.assertEqual(self.task.status, 'unfinished')

    def test_change_task_status_to_valid_status(self):
        self.task.change_status('finished')
        self.assertEqual(self.task.status, 'finished')

    def test_change_task_status_to_invalid_status_raise_NotValidStatus(self):
        with self.assertRaises(NotValidStatus):
            self.task.change_status('lalala')

    def test_search_task_by_matching_word(self):
        self.assertTrue(self.task.match('Create'))

    def test_search_task_by_matching_word_raises_TaskNotFound_if_no_match(self):
        self.assertFalse(self.task.match('ala'))

    def tearDown(self):
        Task.id = 1
