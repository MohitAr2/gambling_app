from service.GamblerProfileService import GamblerProfileService

svc = GamblerProfileService()

gid = svc.create_gambler( # pseudo one 
    "Mo Jo",
    "mojo@mail.com",
    "99999999999",
    10000,
    15000,
    2000
)

# sample records for a game
svc.record_bet(gid, 100, "win", 200)
svc.record_bet(gid, 50, "loss", 0)

stats = svc.get_statistics(gid)
print(vars(stats))

print("Valid:", svc.validate_gambler(gid))

svc.reset_gambler(gid)