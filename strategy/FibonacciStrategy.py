class FibonacciStrategy:
    def __init__(self):
        self.seq = [1, 1]
        self.index = 0

    def next_bet(self, current_stake, last_result):
        if last_result == "loss":
            self.index += 1
            if self.index >= len(self.seq):
                self.seq.append(self.seq[-1] + self.seq[-2])
        else:
            self.index = max(0, self.index - 2)

        return self.seq[self.index]