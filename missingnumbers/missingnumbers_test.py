import unittest

from missingnumbers import missingnumbers

class missingnumbersTest(unittest.TestCase):

    def test_integer_input(self):
        self.assertEqual(missingnumbers(5), 'Invalid Input')

    def test_string_input(self):
        self.assertEqual(missingnumbers('string'), 'Invalid Input')

    def test_empty_list(self):
        self.assertEqual(missingnumbers([]), 'Invalid Input')

    def test_missing_nums_list(self):
        self.assertEqual(missingnumbers([1, 2, 3, 5, 6, 7, 9]), [4, 8])

    def test_no_missing_nums_list(self):
        self.assertEqual(missingnumbers([1, 2, 3, 4, 5, 6, 7, 8]), [])