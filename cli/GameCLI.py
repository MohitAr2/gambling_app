from service.GamblerProfileService import GamblerProfileService
from service.StakeManagementService import StakeManagementService
from service.GameSessionManager import GameSessionManager
from entity.SessionParameters import SessionParameters
from validation.InputValidator import InputValidator
from validation.ValidationConfig import ValidationConfig


class GameCLI:

    def __init__(self):
        self.gambler_service = GamblerProfileService()
        self.stake_service = StakeManagementService()
        self.session_manager = GameSessionManager()

        self.validator = InputValidator(ValidationConfig())

        self.current_gambler = None
        self.current_session = None

    # ---------------------------
    # MAIN MENU
    # ---------------------------
    def run(self):
        while True:
            print("\n===== GAMBLING SYSTEM =====")
            print("1. Create Gambler")
            print("2. Start Session")
            print("3. Continue Session")
            print("4. View Status")
            print("5. End Session")
            print("6. Exit")

            choice = input("Select option: ")

            if choice == "1":
                self.create_gambler()

            elif choice == "2":
                self.start_session()

            elif choice == "3":
                self.play_session()

            elif choice == "4":
                self.view_status()

            elif choice == "5":
                self.end_session()

            elif choice == "6":
                print("Exiting system...")
                break

    # ---------------------------
    # CREATE GAMBLER
    # ---------------------------
    def create_gambler(self):
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        stake = float(input("Initial stake: "))

        result = self.validator.validate_initial_stake(stake)
        if not result.is_valid:
            print(result.errors)
            return

        gid = self.gambler_service.create_gambler(
            name, email, phone, stake, 2000, 200
        )

        self.stake_service.initialize_stake(gid, stake)

        self.current_gambler = gid

        print("Gambler created:", gid)

    # ---------------------------
    # START SESSION
    # ---------------------------
    def start_session(self):
        if not self.current_gambler:
            print("Create gambler first")
            return

        params = SessionParameters(
            win_limit=2000,
            loss_limit=200,
            min_bet=10,
            max_bet=500,
            max_games=20,
            max_duration=3600,
            probability=0.5
        )

        sid = self.session_manager.start_session(
            self.current_gambler,
            params
        )

        self.current_session = sid

        print("Session started:", sid)

    # ---------------------------
    # PLAY SESSION
    # ---------------------------
    def play_session(self):
        if not self.current_session:
            print("No active session")
            return

        rounds = int(input("How many rounds: "))

        self.session_manager.continue_session(
            self.current_session,
            rounds
        )

        print("Session updated")

    # ---------------------------
    # VIEW STATUS
    # ---------------------------
    def view_status(self):
        if not self.current_gambler:
            print("No gambler")
            return

        stake = self.stake_service.get_current_balance(self.current_gambler)

        print("\n--- STATUS ---")
        print("Gambler:", self.current_gambler)
        print("Current Stake:", stake)

        if self.current_session:
            summary = self.session_manager.get_session_summary(
                self.current_session
            )

            print("Games Played:", summary["games_played"])
            print("Wins:", summary["wins"])
            print("Losses:", summary["losses"])
            print("Win Rate:", summary["win_rate"])

    # ---------------------------
    # END SESSION
    # ---------------------------
    def end_session(self):
        if not self.current_session:
            print("No session active")
            return

        summary = self.session_manager.get_session_summary(
            self.current_session
        )

        print("\n--- SESSION SUMMARY ---")
        print(summary)

        self.session_manager.end_session(
            self.current_session,
            "MANUAL"
        )

        self.current_session = None