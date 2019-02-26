import sys
import asyncio
import websockets
import json
from client.body import *
from client.bodyparts import *
import threading

class Game:
    def __init__(self, ip, username):
        self.ip = ip
        self.username = username
        self._parts = [Noose(), Head(), Torso(), LeftArm(), RightArm(), LeftLeg(), RightLeg()]
        self.setup()
        self._inputThread = threading.Thread(target=self.read_input, args=[])

    def setup(self):
        self._body = Body()
        self._partIndex = 0
        self._incorrectCount = 0

    async def start(self):
        async with websockets.connect("ws://" + self.ip + ":8080") as self.websocket:
            self.send_username()
            self._inputThread.start()
            while True:
                message = await self.websocket.recv()
                print(self.receive_message(message))
                print(self._body.get_drawable())
                if self._body.is_dead():
                    self.setup()

    def read_input(self):
        while True:
            letter = ""
            while len(letter) != 1:
                letter = input("Enter a letter:")
            self.send_letter(letter)
            
    def send_username(self):
        self.websocket.send(json.dumps({"type": "SET_NAME", "data": self.username}))

    def send_letter(self, letter):
        if len(letter) > 1:
            return
        if not letter.isalpha():
            return
        data = json.dumps({"type": "GUESS", "data": letter})
        self.websocket.send(data)

    def receive_message(self, message):
        messageDict = json.loads(message)
        if messageDict["type"] == "UPDATE_STATE":
            return self.receive_state(messageDict)
        elif messageDict["type"] == "GAMEOVER":
            return self.receive_termination(messageDict)

    def receive_state(self, messageDict):
        data = messageDict["data"]
        result = "Word: " + data["word"] + "\n"
        result += "Correct: " + str(data["correct"]) + "\n"
        result += "Incorrect: " + str(data["incorrect"])
        incorrectCount = len(data["incorrect"])
        delta = incorrectCount - self._incorrectCount
        for i in range(delta):
            self.add_body_part()
        return result


    def receive_termination(self, messageDict):
        data = messageDict["data"]
        if data["win"] == "True":
            result = "You Won!\n"
        elif data["win"] == "False":
            result = "You Lost!\n"
        result += "Score: Correct:Incorrect\n"
        for key, value in data["score"].items():
            result += key + ": " + str(value["correct"]) + ":" + str(value["incorrect"])
        return result

    def add_body_part(self):
        self._body.add_part(self._parts[self._partIndex])
        self._partIndex += 1

    def get_body(self):
        return self._body