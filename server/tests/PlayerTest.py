from unittest import TestCase, mock
import server.game as game

class TestGame(TestCase):
    def setUp(self):
        self.game = game.Game()

    def test_generate_word(self):
        with mock.patch(game.__name__ + ".Datamuse.words", return_value=[{'score': 1, 'word':'orange'}]) as MockDatamuseAPI:
            word = self.game.generate_word()
            self.assertEqual(word, "orange")

    def test_generate_word_greater_than_5(self):
        with mock.patch(game.__name__ + ".Datamuse.words", return_value=[{'score': 1, 'word': 'orange'}, {'score': 1, 'word': 'the'}]):
            word = self.game.generate_word()

            self.assertEqual(word, "orange")
            self.assertTrue(len(word) > 5)

    def test_guess_correct_lowercase(self):
        self.game.word = "test"

        self.assertTrue(self.game.guess("t"))
        self.assertEqual(self.game.correct, 1)

    def test_guess_correct_uppercase(self):
        self.game.word = "test"

        self.assertTrue(self.game.guess("T"))
        self.assertEqual(self.game.correct, 1)

    def test_guess_incorrect(self):
        self.game.word = "test"

        self.assertFalse(self.game.guess("a"))
        self.assertEqual(self.game.incorrect, 1)

    def test_has_ended_max_incorrect(self):

        self.game.incorrect = 6

        self.assertTrue(self.game.has_ended())

    def test_has_ended_zero(self):
        self.assertFalse(self.game.has_ended())

    def test_has_ended_other(self):
        self.game.incorrect = 2

        self.assertFalse(self.game.has_ended())
