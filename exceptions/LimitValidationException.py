from exceptions.ValidationException import ValidationException
from enums.ValidationErrorType import ValidationErrorType

class LimitValidationException(ValidationException):
    def __init__(self, message, field="limits", value=None):
        super().__init__(
            message,
            ValidationErrorType.LIMIT_ERROR.value,
            field,
            value
        )