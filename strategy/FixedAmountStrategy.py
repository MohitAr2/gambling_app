from strategy.BaseStrategy import BaseStrategy

class FixedAmountStrategy(BaseStrategy):
    def __init__(self, amount):
        self.amount = amount

    def next_bet(self, current_stake, last_result):
        return self.amount