from app.core.exceptions import AppError


class LessonTypeError(AppError):
    pass


# === COMMON ===
class LessonTypeNotFound(LessonTypeError):
    default_message = "El tipo de clase no existe"
    status_code = 404


# === CREATE / UPDATE ===
class LessonTypeAlreadyExists(LessonTypeError):
    default_message = "Ya existe un tipo de clase con ese nombre"
    status_code = 409
