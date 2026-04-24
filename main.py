from service.GamblerProfileService import GamblerProfileService
from service.StakeManagementService import StakeManagementService
from service.BettingService import BettingService
from strategy.MartingaleStrategy import MartingaleStrategy

gambler = GamblerProfileService()
stake = StakeManagementService()
betting = BettingService()

gid = gambler.create_gambler(
    "Mo Jo", "mo@email.com", "999",
    1000, 2000, 200
)

stake.initialize_stake(gid, 1000)

# single bet
bet = betting.place_bet(gid, 100)
print(bet.to_dict())

# strategy betting
strategy = MartingaleStrategy(50)
session = betting.place_with_strategy(gid, strategy, 5)

for b in session:
    print(b.to_dict())