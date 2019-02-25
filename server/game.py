from datamuse import Datamuse

class Game:
    def __init__(self):
        self.correct = 0
        self.incorrect = 0
        self.players = dict()
        self.correct_guesses = set()
        self.incorrect_guessed = set()

    def generate_word(self):
        """Generates a word to use in the game"""
        pass

    def guess(self, letter):
        """Checks if a guess in correct. Increments counters and returns True or False """
        pass

    def has_ended(self):
        """Checks if a game has ended"""
        pass

    def get_score(self):
        """Gets the full scoreboard of guess for each player"""
        pass

    def get_guessed(self):
        """Gets the list of guessed letters formatted as a string"""
        pass