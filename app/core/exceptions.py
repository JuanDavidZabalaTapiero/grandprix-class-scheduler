class AppError(Exception):
    default_message = "Ocurrió un error inesperado. Vuelva a intentar más tarde."
    status_code = 400

    def __init__(self, message=None):
        super().__init__(message or self.default_message)
