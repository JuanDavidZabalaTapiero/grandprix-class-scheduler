from app.core.exceptions import AppError


class InstructorError(AppError):
    pass


# === COMMON ===
class InstructorNotFound(InstructorError):
    default_message = "El instructor no existe"
    status_code = 404


# === DELETE ===
class InstructorHasVehicles(InstructorError):
    default_message = (
        "No se puede eliminar al instructor porque tiene vehículos asociados"
    )
    status_code = 409
