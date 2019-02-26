import sys
import asyncio

from client.game import Game

if __name__ == '__main__':
    if sys.argv[1] == "s":
        pass
    elif sys.argv[1] == "c":
        ip = sys.argv[2]
        username = sys.argv[3]
        game = Game(ip, username)
        asyncio.get_event_loop().run_until_complete(game.start())