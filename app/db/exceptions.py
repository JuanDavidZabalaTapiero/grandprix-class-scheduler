from app.core.exceptions import AppError


class DatabaseConnectionError(AppError):
    default_message = "No hay conexión con la base de datos"
    status_code = 503


class DatabaseOperationError(AppError):
    default_message = "Ocurrió un error inesperado en la base de datos"
    status_code = 500
