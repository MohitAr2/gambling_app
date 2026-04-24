import uuid
from datetime import datetime

class GameRecord:
    def __init__(self, session_id, bet_id, amount, result, stake_before, stake_after):
        self.game_id = str(uuid.uuid4())
        self.session_id = session_id
        self.bet_id = bet_id

        self.amount = amount
        self.result = result

        self.stake_before = stake_before
        self.stake_after = stake_after

        self.timestamp = datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__