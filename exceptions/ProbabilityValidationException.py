from exceptions.ValidationException import ValidationException
from enums.ValidationErrorType import ValidationErrorType

class ProbabilityValidationException(ValidationException):
    def __init__(self, message, field="probability", value=None):
        super().__init__(
            message,
            ValidationErrorType.PROBABILITY_ERROR.value,
            field,
            value
        )