# import uuid
# from enums.AccountStatus import AccountStatus
# from datetime import datetime

# class GamblerProfile:
#     # init override to the making of the json with default values init ???
#     id = str(uuid.uuid4) # random one that is preset 
#     name = "" # init str
#     email = ""
#     phone = "" # validators later
#     init_stake = 0 # default for DB creation
#     curr_stake = 0
#     win_threshold = 0
#     loss_threshold = 0
#     account_status = AccountStatus.CREATED # enum of three 
#     created_at = datetime.timestamp
#     def __init__():
#         # make the file .json here 
#         return 


import uuid
from datetime import datetime
from enums.AccountStatus import AccountStatus

class GamblerProfile:
    def __init__(self, name, email, phone, initial_stake, win_threshold, loss_threshold):
        self.gambler_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone

        self.initial_stake = initial_stake
        self.current_stake = initial_stake

        self.win_threshold = win_threshold
        self.loss_threshold = loss_threshold

        self.account_status = AccountStatus.CREATED.value

        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def to_dict(self):
        return self.__dict__