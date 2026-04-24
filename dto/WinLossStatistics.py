class WinLossStatistics:
    def __init__(self, totals, streaks):
        total_games = totals.total_wins + totals.total_losses

        self.total_games = total_games
        self.wins = totals.total_wins
        self.losses = totals.total_losses

        self.win_rate = totals.total_wins / total_games if total_games else 0

        self.total_winnings = totals.total_win_amount
        self.total_losses_amount = totals.total_loss_amount

        self.net_profit = totals.net_profit()

        self.current_streak = streaks["current"]
        self.longest_win_streak = streaks["max_win"]
        self.longest_loss_streak = streaks["max_loss"]