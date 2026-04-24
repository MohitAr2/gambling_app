import pandas as pd
from utils.db import load, save
from entity.StakeTransaction import StakeTransaction
from enums.TransactionType import TransactionType
from entity.StakeBoundary import StakeBoundary
from entity.StakeMonitor import StakeMonitor

class StakeManagementService:

    def __init__(self, min_stake=100, max_stake=10000):
        self.boundary = StakeBoundary(min_stake, max_stake)

    # ✅ INITIALIZE
    def initialize_stake(self, gid, amount):
        status = self.boundary.validate(amount)
        if status != "OK":
            raise ValueError(status)

        tx = StakeTransaction(
            gid,
            TransactionType.INITIAL_STAKE.value,
            amount,
            amount
        )

        df = load("transactions.json")
        df = pd.concat([df, pd.DataFrame([tx.to_dict()])])
        save(df, "transactions.json")

    # 📊 TRACK (current balance)
    def get_current_balance(self, gid):
        df = load("transactions.json")
        user = df[df["gambler_id"] == gid]

        if user.empty:
            return 0

        return user.iloc[-1]["balance_after"]

    # 🧮 CALCULATE (bet outcome)
    def process_bet(self, gid, amount, result, bet_id=None):
        df = load("transactions.json")
        current = self.get_current_balance(gid)

        if result == "win":
            new_balance = current + amount
            t_type = TransactionType.BET_WIN.value
        else:
            new_balance = current - amount
            t_type = TransactionType.BET_LOSS.value

        tx = StakeTransaction(gid, t_type, amount, new_balance, bet_id)

        df = pd.concat([df, pd.DataFrame([tx.to_dict()])])
        save(df, "transactions.json")

        return new_balance

    # 📉 MONITOR
    def monitor(self, gid):
        df = load("transactions.json")
        user = df[df["gambler_id"] == gid]

        monitor = StakeMonitor(user)

        return {
            "peak": monitor.peak(),
            "lowest": monitor.lowest(),
            "volatility": monitor.volatility(),
            "changes": monitor.changes()
        }

    # 🚧 VALIDATE
    def validate_boundaries(self, gid):
        current = self.get_current_balance(gid)

        status = self.boundary.validate(current)
        warning = self.boundary.warning(current)

        return {
            "status": status,
            "warning": warning,
            "balance": current
        }

    # 📄 REPORT
    def generate_report(self, gid):
        df = load("transactions.json")
        user = df[df["gambler_id"] == gid]

        if user.empty:
            return None

        total_tx = len(user)

        breakdown = user["type"].value_counts().to_dict()

        net = user.iloc[-1]["balance_after"] - user.iloc[0]["balance_after"]

        monitor = StakeMonitor(user)

        return {
            "total_transactions": total_tx,
            "breakdown": breakdown,
            "net_profit_loss": net,
            "peak": monitor.peak(),
            "lowest": monitor.lowest(),
            "volatility": monitor.volatility(),
            "history": user.to_dict(orient="records")
        }

    # 💰 DEPOSIT / WITHDRAW
    def adjust_balance(self, gid, amount, t_type):
        df = load("transactions.json")
        current = self.get_current_balance(gid)

        if t_type == TransactionType.DEPOSIT.value:
            new_balance = current + amount
        elif t_type == TransactionType.WITHDRAWAL.value:
            new_balance = current - amount
        else:
            new_balance = current

        tx = StakeTransaction(gid, t_type, amount, new_balance)

        df = pd.concat([df, pd.DataFrame([tx.to_dict()])])
        save(df, "transactions.json")