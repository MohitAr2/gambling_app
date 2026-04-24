import uuid
from datetime import datetime

class Bet:
    def __init__(self, gambler_id, amount, result, payout, balance_after):
        self.bet_id = str(uuid.uuid4())
        self.gambler_id = gambler_id

        self.bet_amount = amount
        self.result = result  # win / loss
        self.payout = payout
        self.balance_after = balance_after

        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__