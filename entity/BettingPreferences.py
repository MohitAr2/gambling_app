import uuid

class BettingPreferences:
    def __init__(self, gambler_id, min_bet, max_bet, game, auto_play, session_limit):
        self.preference_id = str(uuid.uuid4())
        self.gambler_id = gambler_id

        self.min_bet = min_bet
        self.max_bet = max_bet
        self.preferred_game = game
        self.auto_play = auto_play
        self.session_limit = session_limit

    def to_dict(self):
        return self.__dict__