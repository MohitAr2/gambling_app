import uuid
from datetime import datetime

class StakeTransaction:
    def __init__(self, gambler_id, t_type, amount, balance_after, bet_id=None):
        self.transaction_id = str(uuid.uuid4())
        self.gambler_id = gambler_id
        self.type = t_type
        self.amount = amount
        self.balance_after = balance_after
        self.bet_id = bet_id

        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__