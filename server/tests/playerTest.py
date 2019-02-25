from unittest import TestCase, mock
from server.player import Player

class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("test")

    def test_get_score_zero(self):
        self.assertEqual(self.player.get_score(), (0,0))

    def test_get_score_nonzero(self):
        self.player.correct = 1
        self.player.incorrect = 2

        self.assertEqual(self.player.get_score(), (1, 2))

    def test_increment_correct(self):
        self.player.increment_correct()
        self.assertEqual(self.player.correct, 1)

        self.player.increment_correct()
        self.assertEqual(self.player.correct, 2)

    def test_increment_incorrect(self):
        self.player.increment_incorrect()
        self.assertEqual(self.player.incorrect, 1)

        self.player.increment_incorrect()
        self.assertEqual(self.player.incorrect, 2)