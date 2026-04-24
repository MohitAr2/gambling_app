import random

class WeightedProbabilityStrategy:
    def __init__(self, house_edge=0.05):
        self.house_edge = house_edge

    def determine(self, probability):
        adjusted = probability * (1 - self.house_edge)
        return "win" if random.random() < adjusted else "loss"