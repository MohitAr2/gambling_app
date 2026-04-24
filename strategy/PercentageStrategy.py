class PercentageStrategy:
    def __init__(self, percent):
        self.percent = percent

    def next_bet(self, current_stake, last_result):
        return current_stake * self.percent