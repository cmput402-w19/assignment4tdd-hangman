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

    def test_guess_already_guessed(self):
        self.game.word = "test"

        self.game.correct_guesses = {"a"}

        with self.assertRaises(ValueError):
            self.game.guess("a")

    def test_has_ended_max_incorrect(self):

        self.game.incorrect = 6

        self.assertTrue(self.game.has_ended())

    def test_has_ended_zero(self):
        self.assertEqual(self.game.has_ended(), False)

    def test_has_ended_other(self):
        self.game.incorrect = 2

        self.assertEqual(self.game.has_ended(), False)

    def test_get_guessed_empty(self):
        self.assertEqual(self.game.get_guessed(), {"correct": [], "incorrect": []})

    def test_get_guessed_nonempty_correct(self):
        self.game.correct_guesses.append("a")
        self.assertEqual(self.game.get_guessed(), {"correct": ["a"], "incorrect": []})

    def test_get_guessed_non_empty_incorrect(self):
        self.game.incorrect_guesses.append("a")
        self.game.incorrect_guesses.append("b")
        self.assertEqual(self.game.get_guessed(), {"correct": [] , "incorrect": ["a", "b"]})

    def test_add_player_empty_name(self):
        with self.assertRaises(ValueError):
            self.game.add_player("")

    def test_add_player(self):
        self.game.add_player("test")
        self.assertIn("test", self.game.players)

    def test_get_score_no_players(self):
        self.assertEqual(self.game.get_score(), {"total": (0, 0), "players": {}})

    def test_get_score_one_player(self):
        mock_player = mock.MagicMock()
        mock_player.get_score = mock.MagicMock()
        mock_player.get_score.return_value = (1, 2)

        self.game.players["test"] = mock_player

        self.game.correct = 1
        self.game.incorrect = 2

        self.assertEqual(self.game.get_score(), {"total": (1, 2), "players":{"test": (1,2)}})

    def test_get_score_multi_player(self):
        mock_player1 = mock.MagicMock()

        mock_player1.get_score = mock.MagicMock()
        mock_player1.get_score.return_value = (1, 2)

        mock_player2 = mock.MagicMock()
        mock_player2.get_score = mock.MagicMock()
        mock_player2.get_score.return_value = (3, 1)

        self.game.players["alice"] = mock_player1
        self.game.players["bob"] = mock_player2

        self.game.correct = 4
        self.game.incorrect = 3

        self.assertEqual(self.game.get_score(), {"total": (4, 3), "players": {"alice": (1, 2), "bob": (3, 1)}})