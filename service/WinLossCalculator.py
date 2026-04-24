from strategy.RandomOutcomeStrategy import RandomOutcomeStrategy
from entity.GameResult import GameResult

class WinLossCalculator:

    def __init__(self, outcome_strategy=None):
        self.strategy = outcome_strategy or RandomOutcomeStrategy()

        self.current_streak = 0
        self.max_win_streak = 0
        self.max_loss_streak = 0
        self.last_result = None

    # determine outcome
    def determine_outcome(self, probability):
        return self.strategy.determine(probability)

    # process full result
    def process(self,bet_id,bet_amount, probability, odds, odds_type, stake_before):
        result = self.determine_outcome(probability)

        game = GameResult(
            bet_id,
            bet_amount,
            odds,
            odds_type,
            result,
            stake_before
        )

        self.update_streak(result)

        return game

    # streak logic
    def update_streak(self, result):
        if result == self.last_result:
            self.current_streak += 1
        else:
            self.current_streak = 1

        if result == "win":
            self.max_win_streak = max(self.max_win_streak, self.current_streak)
        else:
            self.max_loss_streak = max(self.max_loss_streak, self.current_streak)

        self.last_result = result

    def get_streaks(self):
        return {
            "current": self.current_streak,
            "max_win": self.max_win_streak,
            "max_loss": self.max_loss_streak
        }