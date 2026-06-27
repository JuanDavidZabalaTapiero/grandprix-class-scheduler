from app.core.exceptions import AppError


class BlockedDayError(AppError):
    pass


class BlockedDayNotFound(BlockedDayError):
    default_message = "No existe el día bloqueado"
    status_code = 404


class BlockedDayAlreadyExists(BlockedDayError):
    default_message = "Ya existe este día bloqueado"
    status_code = 409
