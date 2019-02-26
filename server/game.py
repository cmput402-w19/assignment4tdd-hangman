from datamuse import Datamuse

from random import choice

class Game:
    def __init__(self):
        self.correct = []
        self.incorrect = []
        self.word = self.generate_word()

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

        if letter in self.correct or letter in self.incorrect:
            raise ValueError("Letter already guessed")

        if letter in self.word:
            self.correct.append(letter)
            return True

        else:
            self.incorrect.append(letter)
            return False

    def has_ended(self):
        if len(self.incorrect) < 6:
            return False
        return True

    def get_score(self):
        """Gets the full scoreboard of guess for each player"""
        scores = {key: p.get_score() for key, p in self.players.items()}
        return {"total": (self.correct, self.incorrect) , "players": scores}

    def get_game_state(self):
        blanks = ['_']  * len(self.word)
        for i in range(len(self.word)):
            if self.word[i] in self.correct:
                blanks[i] = self.word[i]

        state = {
            "word": " ".join(blanks),
            "correct": self.correct,
            "incorrect": self.incorrect
        }

        return {"type": "UPDATE_STATE", "data": state}