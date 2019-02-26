import websockets
import asyncio
import json

from server.game import Game
from server.player import Player

PLAYERS = dict()
game = None

async def register(websocket):
    """Associates socket with a particular user"""

    PLAYERS[websocket] = Player()
    print(PLAYERS)

    await notify_players()

async def unregister(websocket):
    """removes user from PLAYERS"""
    del PLAYERS[websocket]


async def notify_players():
    """Sends message to allgame = None players in PLAYERS"""
    if PLAYERS:
        message = json.dumps(game.get_game_state())
        print(PLAYERS.keys())
        await asyncio.wait([player.send(message) for player in PLAYERS.keys()])

async def handler(websocket, path):
    """handler function for incoming messages"""
    await register(websocket)
    try:
        await websocket.send(json.dumps(game.get_game_state()))
        while True:
            async for message in websocket:
                print(message)
                data = json.loads(message)
                if data["type"] == "GUESS":
                    res = game.guess(data["data"])
                    if res:
                        PLAYERS[websocket].increment_correct()
                    else:
                        PLAYERS[websocket].increment_incorrect()

                    await notify_players()
                elif data["type"] == "SET_NAME":
                    PLAYERS[websocket].set_name(data["data"])

    finally:
        await unregister(websocket)

if __name__ == "__main__":
    game = Game()
    start_server = websockets.serve(handler, 'localhost', 8080)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()