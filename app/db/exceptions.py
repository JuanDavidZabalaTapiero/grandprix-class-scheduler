from app.core.exceptions import AppError


class DatabaseConnectionError(AppError):
    default_message = "No hay conexión con la base de datos"
