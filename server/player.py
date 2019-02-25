class Player:
    def __init__(self, name):
        self.name = name
        self.correct = 0
        self.incorrect = 0

    def get_score(self):
        return (self.correct, self.incorrect)

    def increment_correct(self):
        self.correct += 1

    def increment_incorrect(self):
        self.incorrect += 1

