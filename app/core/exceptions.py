class AppError(Exception):
    default_message = "Ocurrió un error inesperado."

    def __init__(self, message=None):
        super().__init__(message or self.default_message)
