from datetime import datetime

class PauseRecord:
    def __init__(self, reason):
        self.pause_time = datetime.now()
        self.resume_time = None
        self.reason = reason

    def resume(self):
        self.resume_time = datetime.now()

    def duration(self):
        if self.resume_time:
            return (self.resume_time - self.pause_time).total_seconds()
        return 0