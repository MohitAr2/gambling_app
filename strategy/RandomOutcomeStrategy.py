import random

class RandomOutcomeStrategy:
    def determine(self, probability):
        return "win" if random.random() < probability else "loss"