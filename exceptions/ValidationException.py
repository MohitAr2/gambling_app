class ValidationException(Exception):
    def __init__(self, message, error_type=None, field=None, value=None):
        super().__init__(message)
        self.error_type = error_type
        self.field = field
        self.value = value

    def to_dict(self):
        return {
            "message": str(self),
            "error_type": self.error_type,
            "field": self.field,
            "value": self.value
        }