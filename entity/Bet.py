import uuid
from datetime import datetime

class Bet:
    def __init__(self, gambler_id, amount, probability, odds, stake_before):
        self.bet_id = str(uuid.uuid4())
        self.gambler_id = gambler_id

        self.amount = amount
        self.win_probability = probability
        self.odds = odds

        self.potential_win = amount * odds

        self.result = None
        self.stake_before = stake_before
        self.stake_after = None

        self.timestamp = datetime.now().isoformat()

    def settle(self, result, stake_after):
        self.result = result
        self.stake_after = stake_after

    def to_dict(self):
        return self.__dict__