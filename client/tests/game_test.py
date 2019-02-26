import unittest
from unittest import mock
from client.body import *
from client.bodyparts import *
from client.game import *
import json

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.username = "Bob"
        self.ip = "localhost"
        self.game = Game(self.ip, self.username)

    def tearDown(self):
        self.game = None
        self.username = None
        self.ip = None

    def test_send_username(self):
        expectedMessage = dict()
        expectedMessage["type"] = "SET_NAME"
        expectedMessage["data"] = self.username

        with mock.patch("client.game.websockets") as mockWebSockets:
            self.game.send_username()
            mockWebSockets.send.assert_called_once_with(json.dumps(expectedMessage))
        
    def test_send_letter(self):
        letter = "a"
        expectedMessage = dict()
        expectedMessage["type"] = "GUESS"
        expectedMessage["data"] = letter

        with mock.patch("client.game.websockets") as mockWebSockets:
            self.game.send_letter(letter)
            mockWebSockets.send.assert_called_once_with(json.dumps(expectedMessage))

    def test_send_long_letters(self):
        letter = "abc"

        with mock.patch("client.game.websockets") as mockWebSockets:
            self.game.send_letter(letter)
            mockWebSockets.send.assert_not_called()

    def test_send_invalid_letter(self):
        letter = "?"

        with mock.patch("client.game.websockets") as mockWebSockets:
            self.game.send_letter(letter)
            mockWebSockets.send.assert_not_called()

    def test_receive_message_state(self):
        expectedMessage = """{
            "type": "UPDATE_STATE",
            "data": {
                "word": "_ _ a",
                "correct": ["a"],
                "incorrect": ["d", "e"]
            }
        }
        """
        receiveStateMock = mock.Mock()
        receiveTerminationMock = mock.Mock()
        self.game.receive_state = receiveStateMock
        self.game.receive_termination = receiveTerminationMock

        self.game.receive_message(expectedMessage)

        receiveStateMock.assert_called_once()
        receiveTerminationMock.assert_not_called()

    def test_receive_message_termination(self):
        expectedMessage = """{
            "type": "GAMEOVER",
            "data": {
                "win": "True",
                "score": {
                    "Alice": {
                        "correct": 1,
                        "incorrect": 2
                    } 
                }
            }
        }
        """
        receiveStateMock = mock.Mock()
        receiveTerminationMock = mock.Mock()
        self.game.receive_state = receiveStateMock
        self.game.receive_termination = receiveTerminationMock

        self.game.receive_message(expectedMessage)

        receiveStateMock.assert_not_called()
        receiveTerminationMock.assert_called_once()

    def test_receive_state(self):
        expectedMessage = """{
            "type": "UPDATE_STATE",
            "data": {
                "word": "_ _ a",
                "correct": ["a"],
                "incorrect": ["d", "e"]
            }
        }
        """
        result = self.game.receive_state(json.loads(expectedMessage))
        self.assertEqual(result, "Word: _ _ A\nCorrect: [a]\nIncorrect: [d, e]")

    def test_receive_termination(self):
        expectedMessage = """{
            "type": "GAMEOVER",
            "data": {
                "win": "True",
                "score": {
                    "Alice": {
                        "correct": 1,
                        "incorrect": 2
                    } 
                }
            }
        }
        """
        result = self.game.receive_state(json.loads(expectedMessage))
        self.assertEqual(result, "You Won!\nScore: Correct:Incorrect\nAlice: 1:2")

    def test_add_body_part(self):
        for i in range(7):
            self.game.add_body_part()
            self.assertIs(self.game.get_body().get_part_count(), i)

if __name__ == '__main__':
    unittest.main()