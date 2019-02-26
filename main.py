import sys
import asyncio
import websockets
from client.game import Game
import server.server as server

if __name__ == '__main__':
    if sys.argv[1] == "s":
        server.game = server.Game()
        start_server = websockets.serve(server.handler, 'localhost', 8080)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    elif sys.argv[1] == "c":
        ip = sys.argv[2]
        username = sys.argv[3]
        game = Game(ip, username)
        asyncio.get_event_loop().run_until_complete(game.start())