from service.GamblerProfileService import GamblerProfileService
from service.StakeManagementService import StakeManagementService

gambler_svc = GamblerProfileService()
stake_svc = StakeManagementService()
gid = gambler_svc.create_gambler(
    "Mo Jo",
    "mo@email.com",
    "9999999999",
    1000,
    2000,
    200
)
stake_svc.initialize_stake(gid, 1000)
stake_svc.process_bet(gid, 200, "win")
stake_svc.process_bet(gid, 100, "loss")
stats = gambler_svc.get_statistics(gid)
print(vars(stats))

print("Balance:", stake_svc.get_current_balance(gid))

print("Valid:", stake_svc.validate_boundaries(gid))

print("Monitor:", stake_svc.monitor(gid))