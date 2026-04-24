from exceptions.ValidationException import ValidationException
from enums.ValidationErrorType import ValidationErrorType

class BetValidationException(ValidationException):
    def __init__(self, message, field="bet", value=None):
        super().__init__(
            message,
            ValidationErrorType.BET_ERROR.value,
            field,
            value
        )