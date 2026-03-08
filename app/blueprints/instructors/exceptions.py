from app.core.exceptions import AppError


class InstructorError(AppError):
    pass


# === COMMON ===
class InstructorNotFound(InstructorError):
    default_message = "El instructor no existe"
    status_code = 404
