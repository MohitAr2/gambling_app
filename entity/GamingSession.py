import uuid
from datetime import datetime
from enums.SessionStatus import SessionStatus

class GamingSession:
    def __init__(self, gambler_id, params):
        self.session_id = str(uuid.uuid4())
        self.gambler_id = gambler_id

        self.params = params.__dict__

        self.status = SessionStatus.INITIALIZED.value

        self.start_time = datetime.now()
        self.end_time = None

        self.games_played = 0
        self.pauses = []

    def start(self):
        self.status = SessionStatus.ACTIVE.value

    def pause(self, pause_record):
        self.status = SessionStatus.PAUSED.value
        self.pauses.append(pause_record)

    def resume(self):
        self.status = SessionStatus.ACTIVE.value

    def end(self):
        self.status = SessionStatus.ENDED.value
        self.end_time = datetime.now()

    def total_pause_time(self):
        return sum(p.duration() for p in self.pauses)

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "gambler_id": self.gambler_id,
            "status": self.status,
            "params": self.params,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "games_played": self.games_played,
            "pause_time": self.total_pause_time()
        }