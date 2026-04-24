class StakeBoundary:
    def __init__(self, min_stake, max_stake):
        self.min_stake = min_stake
        self.max_stake = max_stake

        self.warning_low = min_stake * 1.2
        self.warning_high = max_stake * 0.8

    def validate(self, amount):
        if amount < self.min_stake:
            return "BELOW_MIN"
        if amount > self.max_stake:
            return "ABOVE_MAX"
        return "OK"

    def warning(self, amount):
        if amount <= self.warning_low:
            return "LOW_WARNING"
        if amount >= self.warning_high:
            return "HIGH_WARNING"
        return "SAFE"