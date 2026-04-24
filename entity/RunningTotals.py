class RunningTotals:
    def __init__(self):
        self.total_wins = 0
        self.total_losses = 0

        self.total_win_amount = 0
        self.total_loss_amount = 0

        self.balance_history = []

    def update(self, result_obj):
        if result_obj.result == "win":
            self.total_wins += 1
            self.total_win_amount += result_obj.winnings
        else:
            self.total_losses += 1
            self.total_loss_amount += result_obj.loss

        self.balance_history.append(result_obj.stake_after)

    def net_profit(self):
        return self.total_win_amount - self.total_loss_amount