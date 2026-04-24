from datetime import datetime

class BettingSession:
    def __init__(self, gambler_id, strategy_name):
        self.gambler_id = gambler_id
        self.strategy = strategy_name

        self.start_time = datetime.now().isoformat()
        self.end_time = None

        self.bets = []

    def add_bet(self, bet):
        self.bets.append(bet)

    def close(self):
        self.end_time = datetime.now().isoformat()

    def summary(self):
        total = len(self.bets)
        wins = len([b for b in self.bets if b.result == "win"])

        return {
            "total_bets": total,
            "wins": wins,
            "losses": total - wins
        }