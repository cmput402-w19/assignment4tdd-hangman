from unittest import TestCase, mock
import server.game as game

class TestGame(TestCase):
    def setUp(self):
        with mock.patch(game.__name__ + ".Datamuse.words", return_value=[{'score': 1, 'word': 'orange'}, {'score': 1, 'word': 'the'}]):
            self.game = game.Game()

    def test_generate_word(self):
        with mock.patch(game.__name__ + ".Datamuse.words", return_value=[{'score': 1, 'word': 'orange'}, {'score': 1, 'word': 'the'}]):
            word = self.game.generate_word()

        self.assertEqual(word, "orange")
        self.assertTrue(len(word) > 5)

    def test_guess_correct_lowercase(self):
        self.game.word = "test"

        self.assertTrue(self.game.guess("t"))
        self.assertEqual(self.game.correct, ["t"])

    def test_guess_correct_uppercase(self):
        self.game.word = "test"

        self.assertTrue(self.game.guess("T"))
        self.assertEqual(self.game.correct, ["t"])

    def test_guess_incorrect(self):
        self.game.word = "test"

        self.assertFalse(self.game.guess("a"))
        self.assertEqual(self.game.incorrect, ["a"])

    def test_guess_already_guessed(self):
        self.game.word = "test"

        self.game.correct = ["a"]

        with self.assertRaises(ValueError):
            self.game.guess("a")

    def test_has_ended_max_incorrect(self):

        self.game.incorrect = [1,2,3,4,5,6]

        self.assertTrue(self.game.has_ended())

    def test_has_ended_zero(self):
        self.assertEqual(self.game.has_ended(), False)

    def test_has_ended_other(self):
        self.game.incorrect = [1,2]

        self.assertEqual(self.game.has_ended(), False)

    def test_get_game_state_new(self):
        self.game.word = "sleeping"
        self.assertEqual(self.game.get_game_state(), {"word": "_ _ _ _ _ _ _ _", "correct": [], "incorrect": []})

    def test_get_game_state(self):
        self.game.word = "sleeping"
        self.game.correct = ['e']
        self.game.incorrect = ['t', 'a']

        self.assertEqual(self.game.get_game_state(), {"word": "_ _ e e _ _ _ _", "correct": ['e'], "incorrect": ['t', 'a']} )