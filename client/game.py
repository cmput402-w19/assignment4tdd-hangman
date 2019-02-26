import sys
import asyncio
import websockets

class Game:
    def __init__(self, ip, username):
        pass

    def start(self):
        pass

    def send_username(self):
        pass

    def send_letter(self, letter):
        pass

    def receive_message(self, messageDict):
        pass

    def receive_state(self, messageDict):
        pass

    def receive_termination(self, messageDict):
        pass

    def draw(self):
        pass

    def add_body_part(self):
        pass

    def get_body(self):
        pass


if __name__ == '__main__':
    ip = sys.argv[0]
    username = sys.argv[1]
    game = Game(ip, username)
    asyncio.get_event_loop().run_until_complete(game.start())