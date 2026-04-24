from service.GamblerProfileService import GamblerProfileService
from service.StakeManagementService import StakeManagementService
from service.GameSessionManager import GameSessionManager
from entity.SessionParameters import SessionParameters

gambler = GamblerProfileService()
stake = StakeManagementService()
session_mgr = GameSessionManager()

gid = gambler.create_gambler("Mo", "m@mail.com", "123", 1000, 2000, 200)
stake.initialize_stake(gid, 1000)

params = SessionParameters(
    win_limit=2000,
    loss_limit=200,
    min_bet=50,
    max_bet=200,
    max_games=10,
    max_duration=3600
)

sid = session_mgr.start_session(gid, params)

session_mgr.continue_session(sid, 5)

print(session_mgr.get_session_summary(sid))