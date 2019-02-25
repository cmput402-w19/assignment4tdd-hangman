from unittest import TestCase, mock
import game

class TestGame(TestCase):

    def test_generate_word(self):
        with mock.patch(game.__name__ + ".Datamuse.words", return_value=[{'score': 1, 'word':'orange'}]) as MockDatamuseAPI:
            g = game.Game()
            word = g.generate_word()
            self.assertEqual(word, "orange")

    def test_gernate_word_greater_than_5(self):
        pass

    def test_guess_correct_lowercase(self):
        g = game.Game()
        g.word = "test"

        self.assertTrue(g.guess("t"))
        self.assertEqual(g.correct, 1)

    def test_guess_correct_uppercase(self):
        g = game.Game()
        g.word = "test"

        self.assertTrue(g.guess("T"))
        self.assertEqual(g.correct, 1)

    def test_guess_incorrect(self):
        g = game.Game()
        g.word = "test"

        self.assertFalse(g.guess("a"))
        self.assertEqual(g.incorrect, 1)

    def test_has_ended_max_incorrect(self):
        g = game.Game()

        g.incorrect = 6

        self.assertTrue(g.has_ended())

    def test_has_ended_zero(self):
        g = game.Game()
        self.assertFalse(g.has_ended())

    def test_has_ended_other(self):
        g = game.Game()
        g.incorrect = 2

        self.assertFalse(g.has_ended())
