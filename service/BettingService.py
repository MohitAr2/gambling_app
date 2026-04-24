from service.WinLossCalculator import WinLossCalculator
from enums.OddsType import OddsType
from service.StakeManagementService import StakeManagementService
import uuid

class BettingService:

    def __init__(self):
        self.stake_service = StakeManagementService()
        self.calc = WinLossCalculator()
    def place_bet(self, gid, amount, probability=0.5):
        current = self.stake_service.get_current_balance(gid)

        if amount > current:
            raise Exception("Insufficient stake")

        bet_id = str(uuid.uuid4())

        odds = 1 / probability

        result_obj = self.calc.process(
            bet_id,
            amount,
            probability,
            odds,
            "FIXED",
            current
        )

        if result_obj.result == "win":
            new_balance = self.stake_service.process_bet(
                gid, result_obj.winnings, "win"
            )
        else:
            new_balance = self.stake_service.process_bet(
                gid, amount, "loss"
            )

        result_obj.stake_after = new_balance

        result_obj.bet_id = bet_id

        return result_obj