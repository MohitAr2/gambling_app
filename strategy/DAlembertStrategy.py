class DAlembertStrategy:
    def __init__(self, base):
        self.base = base
        self.current = base

    def next_bet(self, current_stake, last_result):
        if last_result == "loss":
            self.current += self.base
        else:
            self.current = max(self.base, self.current - self.base)

        return self.current