from get_word_frequency import get_word_frequency, build_word_frequency
import unittest

class Test_Case_Get_Word_Frequency(unittest.TestCase):
    def test_get_word_frequency(self):
        word_freq = build_word_frequency("This is a book by myself \n my name is foo bar and the toes are red, and Tony's friend is Jack.")
        self.assertEqual(get_word_frequency("is", word_freq), 2)