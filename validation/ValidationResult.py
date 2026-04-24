class ValidationResult:
    def __init__(self):
        self.is_valid = True
        self.errors = []
        self.warnings = []

    def add_error(self, error):
        self.is_valid = False
        self.errors.append(error)

    def add_warning(self, warning):
        self.warnings.append(warning)

    def summary(self):
        return {
            "valid": self.is_valid,
            "errors": self.errors,
            "warnings": self.warnings
        }