class GamblerStatistics:
    def __init__(self, total_bets, wins, losses, win_rate, net_profit, avg_bet, status):
        self.total_bets = total_bets
        self.wins = wins
        self.losses = losses
        self.win_rate = win_rate
        self.net_profit = net_profit
        self.avg_bet = avg_bet
        self.threshold_status = status