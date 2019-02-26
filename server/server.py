import websockets
import asyncio
import json
import uuid

from player import Player
from game import Game

PLAYERS = dict()
game = None

async def register(websocket):
    """Associates socket with a particular user"""
    pass

async def unregister(websocket):
    """removes user from PLAYERS"""
    pass

async def notify_players():
    """Sends message to allgame = None players in PLAYERS"""
    pass

async def update_game_state():
    """"""
    pass

async def handler(websocket, path):
    """handler function for incoming messages"""
    pass

if __name__ == "__main__":
    start_server = websockets.serve(hello, 'localhost', 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()