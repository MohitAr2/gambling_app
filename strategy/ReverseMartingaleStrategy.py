class ReverseMartingaleStrategy:
    def __init__(self, base):
        self.base = base
        self.current = base

    def next_bet(self, current_stake, last_result):
        if last_result == "win":
            self.current *= 2
        else:
            self.current = self.base
        return self.current