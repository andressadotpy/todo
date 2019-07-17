import unittest

from ..note import Note

class TestNote(unittest.TestCase):

    def setUp(self):
        self.message = Note("This is a note")

    def test_if_can_get_a_note(self):
        self.assertEqual(self.message.note, "This is a note")

    def test_if_a_not_can_be_set(self):
        self.message.note = "I am changing the note now"
        self.assertEqual(self.message.note, "I am changing the note now")
