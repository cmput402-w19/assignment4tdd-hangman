from unittest import TestCase, mock
import server.server as server
import asyncio

class TestServer(TestCase):
    def setUp(self):
        self.mockSocket = mock.MagicMock()
        self.mockSocket.send = mock.MagicMock()

        self.mockPlayer = mock.MagicMock()
        self.mockPlayer.increment_correct = mock.MagicMock()
        self.mockPlayer.increment_incorrect = mock.MagicMock()

        self.mockGame = mock.MagicMock()
        self.mockGame.guess = mock.MagicMock()
        self.mockGame.guess.return_value = True
        self.mockGame.get_game_state = mock.MagicMock()
        self.mockGame.get_game_state.return_value = {"type": "UPDATE_STATE", "data": {"word": "_ e _ _ _ e _", "correct": ["e"], "incorrect": ["y"]}}

    # def test_register(self):
    #     server.register(self.mockSocket)
    #     self.assertIn(self.mockSocket, server.PLAYERS)

    # def test_unregister(self):
    #     server.PLAYERS = {self.mockSocket: self.mockPlayer}
    #     server.unregister(self.mockSocket)

    #     self.assertNotIn(self.mockSocket, server.PLAYERS)

    # def test_notify_players(self):
    #     server.PLAYERS = {self.mockSocket: self.mockPlayer}
    #     server.notify_players()
    #     self.assertTrue(self.mockSocket.send.called)

    # def test_update_game_state_guess(self):
    #     # server.game = self.mockGame

    #     # server.handler(self.mockSocket)
    #     pass

    # def test_update_game_state_fail(self):
    #     pass

    # def test_handler(self):
    #     pass