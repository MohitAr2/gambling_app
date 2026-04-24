class SessionParameters:
    def __init__(self, win_limit, loss_limit, min_bet, max_bet, max_games, max_duration, probability=0.5):
        self.win_limit = win_limit
        self.loss_limit = loss_limit

        self.min_bet = min_bet
        self.max_bet = max_bet

        self.max_games = max_games
        self.max_duration = max_duration

        self.default_probability = probability