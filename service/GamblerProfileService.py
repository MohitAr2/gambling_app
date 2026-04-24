import pandas as pd
from utils.db import load, save
from entity.GamblerProfile import GamblerProfile
from entity.BettingPreferences import BettingPreferences
from entity.Bet import Bet
from dto.GamblerStatistics import GamblerStatistics

class GamblerProfileService:

    # ✅ CREATE
    def create_gambler(self, name, email, phone, stake, win_t, loss_t):
        if stake <= 0:
            raise ValueError("Stake must be > 0")
        if win_t <= stake:
            raise ValueError("Win threshold must exceed stake")
        if loss_t >= stake:
            raise ValueError("Loss threshold must be less than stake")

        gambler = GamblerProfile(name, email, phone, stake, win_t, loss_t)

        df = load("gamblers.json")
        df = pd.concat([df, pd.DataFrame([gambler.to_dict()])])
        save(df, "gamblers.json")

        return gambler.gambler_id

    # ✏️ UPDATE
    def update_gambler(self, gid, updates: dict):
        df = load("gamblers.json")

        idx = df[df["gambler_id"] == gid].index
        if len(idx) == 0:
            raise Exception("Gambler not found")

        for key, value in updates.items():
            df.loc[idx, key] = value

        save(df, "gamblers.json")

    # 📊 RETRIEVE STATS
    def get_statistics(self, gid):
        bets = load("bets.json")
        gambler = load("gamblers.json")

        g = gambler[gambler["gambler_id"] == gid]
        if g.empty:
            raise Exception("Not found")

        user_bets = bets[bets["gambler_id"] == gid]

        total = len(user_bets)
        wins = len(user_bets[user_bets["result"] == "win"])
        losses = total - wins

        win_rate = wins / total if total else 0
        net_profit = user_bets["payout"].sum() - user_bets["bet_amount"].sum() if total else 0
        avg_bet = user_bets["bet_amount"].mean() if total else 0

        current = float(g.iloc[0]["current_stake"])
        win_t = float(g.iloc[0]["win_threshold"])
        loss_t = float(g.iloc[0]["loss_threshold"])

        if current >= win_t:
            status = "WIN_REACHED"
        elif current <= loss_t:
            status = "LOSS_REACHED"
        else:
            status = "SAFE"

        return GamblerStatistics(total, wins, losses, win_rate, net_profit, avg_bet, status)

    # ✅ VALIDATE
    def validate_gambler(self, gid):
        df = load("gamblers.json")
        g = df[df["gambler_id"] == gid]

        if g.empty:
            return False

        g = g.iloc[0]

        if g["account_status"] != "ACTIVE" and g["account_status"] != "CREATED":
            return False

        if g["current_stake"] <= 0:
            return False

        if g["current_stake"] <= g["loss_threshold"]:
            return False

        return True

    # 🔄 RESET
    def reset_gambler(self, gid):
        df = load("gamblers.json")

        idx = df[df["gambler_id"] == gid].index
        if len(idx) == 0:
            raise Exception("Not found")

        g = df.loc[idx].iloc[0]

        init = g["initial_stake"]

        win_ratio = g["win_threshold"] / init
        loss_ratio = g["loss_threshold"] / init

        df.loc[idx, "current_stake"] = init
        df.loc[idx, "win_threshold"] = init * win_ratio
        df.loc[idx, "loss_threshold"] = init * loss_ratio

        save(df, "gamblers.json")

    # 🎲 RECORD BET
    def record_bet(self, gid, amount, result, payout):
        gdf = load("gamblers.json")
        bdf = load("bets.json")

        idx = gdf[gdf["gambler_id"] == gid].index
        if len(idx) == 0:
            raise Exception("Gambler not found")

        current = gdf.loc[idx, "current_stake"].values[0]

        if result == "win":
            current += payout
        else:
            current -= amount

        gdf.loc[idx, "current_stake"] = current

        bet = Bet(gid, amount, result, payout, current)
        bdf = pd.concat([bdf, pd.DataFrame([bet.to_dict()])])

        save(gdf, "gamblers.json")
        save(bdf, "bets.json")