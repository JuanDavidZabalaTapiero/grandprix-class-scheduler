from app.core.exceptions import AppError


class LessonError(AppError):
    pass


# === COMMON ===
class LessonNotFound(LessonError):
    default_message = "La clase no existe"
    status_code = 404


# === CREATE / UPDATE ===
class LessonAlreadyExists(LessonError):
    default_message = "La clase ya está registrada"
    status_code = 409
