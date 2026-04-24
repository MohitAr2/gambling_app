class GameResult:
    def __init__(self, bet_id, amount, odds, odds_type, result, stake_before):
        self.bet_id = bet_id
        self.amount = amount
        self.odds = odds
        self.odds_type = odds_type
        self.result = result

        self.stake_before = stake_before

        self.winnings = self.calculate_winnings()
        self.loss = amount if result == "loss" else 0

        self.stake_after = None

    def calculate_winnings(self):
        if self.result != "win":
            return 0

        if self.odds_type == "FIXED":
            return self.amount * self.odds

        if self.odds_type == "PROBABILITY":
            return self.amount * self.odds

        if self.odds_type == "DECIMAL":
            return self.amount * self.odds

        if self.odds_type == "AMERICAN":
            if self.odds > 0:
                return self.amount * (self.odds / 100)
            else:
                return self.amount / (abs(self.odds / 100))

        return 0