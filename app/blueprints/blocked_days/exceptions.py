from app.core.exceptions import AppError


class BlockedDayError(AppError):
    pass


class BlockedDayNotFound(BlockedDayError):
    default_message = "No existe el día bloqueado"
    status_code = 404


class BlockedDayAlreadyExists(BlockedDayError):
    default_message = "Ya existe este día bloqueado"
    status_code = 409


class BlockedSlotNotFound(BlockedDayError):
    default_message = "No existe el bloque horario bloqueado"
    status_code = 404


class BlockedSlotAlreadyExists(BlockedDayError):
    default_message = "Ese bloque horario ya está bloqueado para este instructor"
    status_code = 409
