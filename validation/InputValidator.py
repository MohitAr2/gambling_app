import math
from validation.ValidationResult import ValidationResult
from exceptions.ValidationException import ValidationException

class InputValidator:

    def __init__(self, config):
        self.config = config

    # -------------------------
    # SAFE NUMBER PARSING
    # -------------------------
    def parse_and_validate_numeric(self, value):
        result = ValidationResult()

        if value is None:
            result.add_error("NULL value")
            return None, result

        try:
            num = float(value)

            if math.isnan(num) or math.isinf(num):
                result.add_error("Invalid numeric value (NaN/Inf)")
                return None, result

            return num, result

        except:
            result.add_error("Invalid numeric format")
            return None, result

    # -------------------------
    # STAKE VALIDATION
    # -------------------------
    def validate_initial_stake(self, stake):
        result = ValidationResult()

        if stake <= 0:
            result.add_error("Stake must be positive")

        if stake < self.config.min_stake:
            result.add_error("Stake below minimum")

        if stake > self.config.max_stake:
            result.add_error("Stake exceeds maximum")

        return result

    def validate_stake_non_negative(self, stake):
        result = ValidationResult()

        if stake < 0:
            result.add_error("Negative stake not allowed")

        return result

    # -------------------------
    # BET VALIDATION
    # -------------------------
    def validate_bet_amount(self, bet, stake):
        result = ValidationResult()

        if bet <= 0:
            result.add_error("Bet must be positive")

        if bet > stake:
            result.add_error("Bet exceeds current stake")

        if bet < self.config.min_bet:
            result.add_error("Bet below minimum")

        if bet > self.config.max_bet:
            result.add_error("Bet exceeds maximum")

        return result

    # -------------------------
    # LIMIT VALIDATION
    # -------------------------
    def validate_limits(self, lower, upper, stake):
        result = ValidationResult()

        if lower >= upper:
            result.add_error("Lower limit must be less than upper limit")

        if stake < lower or stake > upper:
            result.add_warning("Stake outside limits")

        if lower < 0 or upper < 0:
            result.add_error("Limits cannot be negative")

        return result

    # -------------------------
    # PROBABILITY VALIDATION
    # -------------------------
    def validate_probability(self, p):
        result = ValidationResult()

        if p < self.config.min_probability or p > self.config.max_probability:
            result.add_error("Probability must be between 0 and 1")

        if math.isnan(p) or math.isinf(p):
            result.add_error("Invalid probability value")

        return result