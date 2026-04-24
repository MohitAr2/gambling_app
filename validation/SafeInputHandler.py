from validation.InputValidator import InputValidator

class SafeInputHandler:

    def __init__(self, validator):
        self.validator = validator

    def get_valid_number(self, prompt):
        while True:
            value = input(prompt)

            num, result = self.validator.parse_and_validate_numeric(value)

            if result.is_valid:
                return num

            print("Invalid input:", result.errors)