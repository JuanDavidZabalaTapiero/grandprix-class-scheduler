class AppError(Exception):
    default_message = "Ocurrió un error inesperado. Vuelva a intentar más tarde."

    def __init__(self, message=None):
        super().__init__(message or self.default_message)
