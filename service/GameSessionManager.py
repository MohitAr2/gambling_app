import pandas as pd
from utils.db import load, save

from entity.GamingSession import GamingSession
from entity.GameRecord import GameRecord
from entity.PauseRecord import PauseRecord
from entity.SessionParameters import SessionParameters

from service.BettingService import BettingService
from service.StakeManagementService import StakeManagementService

from enums.SessionStatus import SessionStatus
from enums.SessionEndReason import SessionEndReason

class GameSessionManager:

    def __init__(self):
        self.bet_service = BettingService()
        self.stake_service = StakeManagementService()

    # START SESSION
    def start_session(self, gid, params: SessionParameters):
        sessions = load("sessions.json")
        sessions = load("sessions.json")

        if sessions.empty or "gambler_id" not in sessions.columns:
            sessions = pd.DataFrame(columns=[
                "session_id",
                "gambler_id",
                "status",
                "params",
                "start_time",
                "end_time",
                "games_played",
                "pause_time",
                "end_reason"
            ])
        active = sessions[
            (sessions["gambler_id"] == gid) &
            (sessions["status"] == SessionStatus.ACTIVE.value)
        ]

        if not active.empty:
            raise Exception("Active session already exists")

        session = GamingSession(gid, params)
        session.start()

        sessions = pd.concat([sessions, pd.DataFrame([session.to_dict()])])
        save(sessions, "sessions.json")

        return session.session_id

    # CONTINUE SESSION
    def continue_session(self, session_id, rounds=1):
        sessions = load("sessions.json")
        games = load("game_records.json")

        s = sessions[sessions["session_id"] == session_id]
        if s.empty:
            raise Exception("Session not found")

        s = s.iloc[0]

        if s["status"] != SessionStatus.ACTIVE.value:
            raise Exception("Session not active")

        params = s["params"]
        gid = s["gambler_id"]

        for _ in range(rounds):
            current = self.stake_service.get_current_balance(gid)

            # boundary checks
            if current >= params["win_limit"]:
                self.end_session(session_id, SessionEndReason.WIN_LIMIT.value)
                break

            if current <= params["loss_limit"]:
                self.end_session(session_id, SessionEndReason.LOSS_LIMIT.value)
                break

            bet_amount = min(max(params["min_bet"], 1), params["max_bet"])

            bet = self.bet_service.place_bet(gid, bet_amount, params["default_probability"])

            record = GameRecord(
                session_id,
                bet.bet_id,
                bet.amount,
                bet.result,
                bet.stake_before,
                bet.stake_after
            )

            games = pd.concat([games, pd.DataFrame([record.to_dict()])])

        save(games, "game_records.json")

    # PAUSE
    def pause_session(self, session_id, reason="manual"):
        sessions = load("sessions.json")

        idx = sessions[sessions["session_id"] == session_id].index
        if len(idx) == 0:
            raise Exception("Session not found")

        sessions.loc[idx, "status"] = SessionStatus.PAUSED.value
        save(sessions, "sessions.json")

    # RESUME
    def resume_session(self, session_id):
        sessions = load("sessions.json")

        idx = sessions[sessions["session_id"] == session_id].index
        sessions.loc[idx, "status"] = SessionStatus.ACTIVE.value

        save(sessions, "sessions.json")

    # END
    def end_session(self, session_id, reason):
        sessions = load("sessions.json")

        idx = sessions[sessions["session_id"] == session_id].index

        sessions.loc[idx, "status"] = SessionStatus.ENDED.value
        sessions.loc[idx, "end_reason"] = reason

        save(sessions, "sessions.json")

    # SUMMARY
    def get_session_summary(self, session_id):
        sessions = load("sessions.json")
        games = load("game_records.json")

        s = sessions[sessions["session_id"] == session_id].iloc[0]
        g = games[games["session_id"] == session_id]

        total = len(g)
        wins = len(g[g["result"] == "win"])

        return {
            "games_played": total,
            "wins": wins,
            "losses": total - wins,
            "win_rate": wins / total if total else 0,
            "status": s["status"]
        }