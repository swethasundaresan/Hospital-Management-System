class PatientNumberNotFoundException(Exception):
    """Exception raised when a patient number is not found in the database."""
    def __init__(self, message="Patient number not found in the database."):
        self.message = message
        super().__init__(self.message)
