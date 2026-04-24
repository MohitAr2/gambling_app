class BaseStrategy:
    def next_bet(self, current_stake, last_result):
        raise NotImplementedError