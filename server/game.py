from datamuse import Datamuse
from server.player import Player

from random import choice

class Game:
    def __init__(self):
        self.correct = 0
        self.incorrect = 0
        self.players = dict()
        self.correct_guesses = []
        self.incorrect_guesses = []

    def generate_word(self):
        """Generates a word to use in the game"""
        topics = ["animals", "plants", "buildings", "places", "farming", "school", "food"]
        api = Datamuse()
        result = api.words(topics = choice(topics))
        words = [res["word"] for res in result]

        return choice(list(filter(lambda x: (len(x) > 5), words)))

    def guess(self, letter):
        """Checks if a guess in correct. Increments counters and returns True or False """
        letter = letter.lower()

        if letter in self.correct_guesses or letter in self.incorrect_guesses:
            raise ValueError("Letter already guessed")

        if letter in self.word:
            self.correct_guesses.append(letter)
            self.correct += 1
            return True

        else:
            self.incorrect_guesses.append(letter)
            self.incorrect += 1
            return False

    def has_ended(self):
        if self.incorrect < 6:
            return False
        return True

    def get_score(self):
        """Gets the full scoreboard of guess for each player"""
        scores = {key: p.get_score() for key, p in self.players.items()}
        return {"total": (self.correct, self.incorrect) , "players": scores}


    def get_guessed(self):
        """Gets the list of guessed letters formatted as a string"""
        return {"correct": self.correct_guesses, "incorrect": self.incorrect_guesses}

    def add_player(self, name):
        """Adds a player to the game"""
        if name in self.players:
            raise ValueError("Name Taken")

        if not name.strip():
            raise ValueError("Name cannot be empty")

        self.players[name] = Player(name)
