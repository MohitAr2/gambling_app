import random
import pandas as pd

from entity.Bet import Bet
from utils.db import load, save
from service.StakeManagementService import StakeManagementService

class BettingService:

    def __init__(self):
        self.stake_service = StakeManagementService()
    def place_bet(self, gid, amount, probability=0.5):
        current = self.stake_service.get_current_balance(gid)

        if amount > current:
            raise Exception("Insufficient stake")

        odds = 1 / probability

        bet = Bet(gid, amount, probability, odds, current)

        result = self.determine_outcome(probability)

        if result == "win":
            new_balance = self.stake_service.process_bet(gid, bet.potential_win, "win")
        else:
            new_balance = self.stake_service.process_bet(gid, amount, "loss")

        bet.settle(result, new_balance)

        df = load("bets.json")
        df = pd.concat([df, pd.DataFrame([bet.to_dict()])])
        save(df, "bets.json")

        return bet
    def determine_outcome(self, probability):
        return "win" if random.random() < probability else "loss"
    def place_with_strategy(self, gid, strategy, rounds=5, probability=0.5):
        session = []

        last_result = None

        for _ in range(rounds):
            current = self.stake_service.get_current_balance(gid)

            amount = strategy.next_bet(current, last_result)

            if amount > current:
                break

            bet = self.place_bet(gid, amount, probability)
            last_result = bet.result

            session.append(bet)

        return session
    def place_consecutive_bets(self, gid, amount, rounds):
        results = []
        for _ in range(rounds):
            results.append(self.place_bet(gid, amount))
        return results