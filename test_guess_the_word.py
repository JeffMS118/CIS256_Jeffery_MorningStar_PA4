#Jeffery Morning Star
#CIS256 Fall 2026
#Programming Assignment 4

import unittest
from unittest.mock import patch
from guess_the_word import select_word, check_guess, word_list

class TestGame(unittest.TestCase):

    def test_selected_word_is_from_list(self):
        word = select_word()

        self.assertIn(word, word_list)

    def test_correct_guess(self):
        result = check_guess("p", "python")

        self.assertTrue(result)

    def test_incorrect_guess(self):
        result = check_guess("x", "python")

        self.assertFalse(result)

    def test_repeated_letter(self):
        result = check_guess("p", "programming")

        self.assertTrue(result)

    def test_letter_not_in_word(self):
        result = check_guess("z", "computer")

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
