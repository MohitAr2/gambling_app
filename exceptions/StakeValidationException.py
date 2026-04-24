from exceptions.ValidationException import ValidationException
from enums.ValidationErrorType import ValidationErrorType

class StakeValidationException(ValidationException):
    def __init__(self, message, field="stake", value=None):
        super().__init__(
            message,
            ValidationErrorType.STAKE_ERROR.value,
            field,
            value
        )